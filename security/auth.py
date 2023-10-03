# IMPORTING PACKAGES
from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from database.models import Account, User, Company, Location, Social
from datetime import datetime, timedelta
from typing import Annotated
from database.crud import db_dependency, check_email, check_username
from database.schemas import Token, UserModel, CompanyModel, ValidateRequest


# DECLARING THE ROUTER
router = APIRouter(
    prefix="/auth"
)


# SET UP PASSWORD HASHING USING PASSLIB[BCRYPT]
SECRET_KEY = '6d1ba59df65e0b50d80219b8588f25b8616615b0984da0c606f275d74de020e0'
ALGORITHM = 'HS256'
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


# SET UP JWT USING PYTHON JOSE
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')


# FUNCTION FOR HASHING AND VERIFYING PASSWORD
def hash_password(password: str):
    return bcrypt_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return bcrypt_context.verify(password, hashed_password)


# FUNCTION FOR AUTHENTICATE USER
def authenticate_user(username: str, password: str, db_session):
    user = db_session.query(Account).filter(Account.login_name == username).first()

    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    
    return user


# FUNCTION FOR GENERATE JWT TOKEN
def create_access_token(username: str, user_email: str, user_role: str, expires_delta: timedelta):
    to_encode = {'sub': username, 'email': user_email, 'role': user_role}
    expires = datetime.now() + expires_delta
    to_encode.update({'exp': expires})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# FUNCTION FOR GET CURRENT USER
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')
        email = payload.get('email')
        role = payload.get('role')

        if username is None or email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized User')
        
        return {'username': username, 'email': email, 'role': role}
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized User')
    

# CREATING AUTHENTICATION ROUTE FOR LOGIN AND CREATE ACCOUNT
# FORM DEPENDENCY FOR OAUTH2PASSWORDREQUESTFORM
form_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]


# LOGIN ROUTES FOR USER AND COMPANY
@router.post('/login', response_model=Token)
async def login_for_access_token(db: db_dependency, form_data: form_dependency):
    account_model = authenticate_user(username=form_data.username, password=form_data.password, db_session=db)
    if not account_model:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Couldn't validate the credentials")
    
    token = create_access_token(username=account_model.login_name, user_email=account_model.login_email, user_role=account_model.role, expires_delta=timedelta(days=7))
    return {'access_token': token, 'token_type': 'bearer', 'login_data': {'username': account_model.login_name, 'email': account_model.login_email, 'role': account_model.role}}


# CREATE A USER ACCOUNT
@router.post('/user/register', status_code=status.HTTP_201_CREATED)
async def create_user_account(db: db_dependency, create_user_request: UserModel):

    if check_username(create_user_request.username, db):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Username {create_user_request.username} is already in use.")

    if check_email(create_user_request.email, db):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Email {create_user_request.email} is already in use.")
    
    if create_user_request.location:
        location_id = f'loc{datetime.now().strftime("%y%m%d%H%M%S")}'
        location_model = Location(data_id=location_id, **create_user_request.location.model_dump())
        
        db.add(location_model)
        db.commit()
        db.refresh(location_model)

    user_model = User(
        first_name=create_user_request.first_name.casefold(),
        last_name=create_user_request.last_name.casefold(),
        username=create_user_request.username,
        email=create_user_request.email,
        birth_date=create_user_request.birth_date,
        location=location_model.data_id,
        is_refugee=create_user_request.is_refugee
    )

    db.add(user_model)
    db.commit()
    db.refresh(user_model)

    account_model = Account(
        login_name=create_user_request.username,
        login_email=create_user_request.email,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        role=create_user_request.role
    )

    db.add(account_model)
    db.commit()
    db.refresh(account_model)
    

# CREATE A COMPANY ACCOUNT
@router.post('/company/register', status_code=status.HTTP_201_CREATED)
async def create_company_account(db: db_dependency, create_company_request: CompanyModel):

    if check_username(create_company_request.c_name, db):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Company c_name/username {create_company_request.c_name} is already in use.")

    if check_email(create_company_request.c_mail, db):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Company c_mail/email {create_company_request.c_mail} is already in use.")
    
    if create_company_request.location:
        location_id = f'loc{datetime.now().strftime("%y%m%d%H%M%S")}'
        location_model = Location(data_id=location_id, **create_company_request.location.model_dump())
        
        db.add(location_model)
        db.commit()
        db.refresh(location_model)

    if create_company_request.social:
        social_id = f'media{datetime.now().strftime("%y%m%d%H%M%S")}'
        social_model = Social(data_id=social_id, **create_company_request.social.model_dump())

        db.add(social_model)
        db.commit()
        db.refresh(social_model)

    company_model = Company(
        name=create_company_request.name.casefold(),
        c_name=create_company_request.c_name,
        c_mail=create_company_request.c_mail,
        social=social_model.data_id,
        location=location_model.data_id,
        website=create_company_request.website
    )

    db.add(company_model)
    db.commit()
    db.refresh(company_model)

    account_model = Account(
        login_name=create_company_request.c_name,
        login_email=create_company_request.c_mail,
        hashed_password=bcrypt_context.hash(create_company_request.password),
        role=create_company_request.role
    )

    db.add(account_model)
    db.commit()
    db.refresh(account_model)
    

# CREATING A USER DEPENDENCY
account_dependency = Annotated[dict, Depends(get_current_user)]


# UNIQUE USERNAME AND EMAIL VALIDATION ROUTE
@router.post("/validate/", status_code=status.HTTP_200_OK)
async def account_validation(db: db_dependency, validate_request: ValidateRequest):
    if validate_request.username:
        user_exist = check_username(validate_request.username, db)
        return  {"status": "exist", "message": f"{validate_request.username} is not available"} if user_exist else {"status": "not exist", "message": f"{validate_request.username} is available"}
    if validate_request.email:
        email_exist = check_email(validate_request.email, db)
        return {"status": "exist", "message": f"{validate_request.email} is not available"} if email_exist else {"status": "not exist", "message": f"{validate_request.email} is available"}
