# IMPORTING LOCAL PACKAGES
from fastapi import APIRouter, HTTPException, status, Path
from security.auth import account_dependency, hash_password, verify_password
from database.crud import db_dependency, get_location
from database.schemas import ChangePasswordRequest, ApplicationModel
from database.models import User, Account, Application, Cover
from datetime import datetime
from sqlalchemy import desc


# DECLARING THE ROUTER
router = APIRouter(
    prefix="/user"
)


# CREATING ROUTES FOR USER'S
@router.post('/application', status_code=status.HTTP_201_CREATED)
async def apply_to_job(account: account_dependency, db: db_dependency, application_request: ApplicationModel):

    cover_model = Cover(**application_request.cover_letter.model_dump())
    db.add(cover_model)
    db.commit()
    db.refresh(cover_model)

    application_model = Application(
        user_acc=account.get('username'),
        job_id=application_request.job_id,
        cover_letter=cover_model.id
    )

    db.add(application_model)
    db.commit()
    db.refresh(application_model)


@router.get('/application', status_code=status.HTTP_200_OK)
async def get_all_application(account: account_dependency, db: db_dependency):

    if account.get('role') != 'user':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"{account.get('role')} is not allowed for this route")

    application_list = db.query(Application).filter(Application.user_acc == account.get('username')).all()
    if len(application_list) < 1:
        return None
    
    return db.query(Application).filter(Application.user_acc == account.get('username')).order_by(desc(Application.applied_on)).all()
    

@router.get('/application/{application_id}', status_code=status.HTTP_200_OK)
async def get_single_application(account: account_dependency, db: db_dependency, application_id: int = Path(gt=0)):
    if account.get('role') != 'user':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"{account.get('role')} is not allowed for this route")

    application_one = db.query(Application).filter(Application.id == application_id).first()
    
    if not application_one:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    
    cover_model = db.query(Cover).filter(Cover.id == application_one.cover_letter).first()

    return {
        "id": application_one.id,
        "user_acc": application_one.user_acc,
        "job_id": application_one.job_id,
        "applied_on": application_one.applied_on,
        "cover_letter": cover_model
    }


@router.put('/password', status_code=status.HTTP_204_NO_CONTENT)
async def change_password(account: account_dependency, db: db_dependency, change_password_requst: ChangePasswordRequest):
    if account is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    
    account_model = db.query(Account).filter(Account.login_name == account.get("username")).first()
    if not verify_password(change_password_requst.password, account_model.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password doesn't match")
    
    account_model.hashed_password = hash_password(change_password_requst.new_password)

    db.add(account_model)
    db.commit()


@router.get('/account', status_code=status.HTTP_200_OK)
async def get_account_info(account: account_dependency, db: db_dependency):
    if account is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    
    account_model = db.query(User).filter(User.username == account.get('username')).first()

    return {
            "first_name": account_model.first_name,
            "last_name": account_model.last_name,
            "birth_date": account_model.birth_date,
            "username": account_model.username,
            "email": account_model.email,
            "location": get_location(account_model.location, db),
            "is_refugee": account_model.is_refugee
    }
    