# IMPORTING LOCAL PACKAGES
from fastapi import APIRouter, HTTPException, status, Path
from security.auth import account_dependency, hash_password
from database.crud import db_dependency
from database.schemas import AccountModelCreate
from database.models import User, Account, Application, Company, Job, Location, Social



# DECLARING THE ROUTER
router = APIRouter(
    prefix="/admin"
)


# CREATING ROUTES FOR ADMIN

# ALL DATA GETTING ROUTE
@router.get('/user', status_code=status.HTTP_200_OK)
async def get_all_users(account: account_dependency, db: db_dependency):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")

    return db.query(User).all()


@router.get('/company', status_code=status.HTTP_200_OK)
async def get_all_companies(account: account_dependency, db: db_dependency):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")

    return db.query(Company).all()


@router.get('/job', status_code=status.HTTP_200_OK)
async def get_all_companies(account: account_dependency, db: db_dependency):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")

    return db.query(Job).all()


@router.get('/application', status_code=status.HTTP_200_OK)
async def get_all_applications(account: account_dependency, db: db_dependency):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")

    return db.query(Application).all()


@router.get('/account', status_code=status.HTTP_200_OK)
async def get_all_accounts(account: account_dependency, db: db_dependency):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")

    return db.query(Account).all()


@router.get('/location', status_code=status.HTTP_200_OK)
async def get_all_locations(account: account_dependency, db: db_dependency):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")

    return db.query(Location).all()


@router.get('/social', status_code=status.HTTP_200_OK)
async def get_all_social_accounts(account: account_dependency, db: db_dependency):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")

    return db.query(Social).all()


# ALL DATA DELETING ROUTE
@router.delete('/user/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(account: account_dependency, db: db_dependency, user_id: int = Path(gt=0)):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")
    
    user_model = db.query(User).filter(User.id == user_id).first()

    if not user_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    db.query(User).filter(User.id == user_id).delete()
    db.commit()


@router.delete('/company/{company_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_company(account: account_dependency, db: db_dependency, company_id: int = Path(gt=0)):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")
    
    company_model = db.query(Company).filter(Company.id == company_id).first()

    if not company_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    
    db.query(Company).filter(Company.id == company_id).delete()
    db.commit()


@router.delete('/job/{job_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_job(account: account_dependency, db: db_dependency, job_id: int = Path(gt=0)):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")
    
    job_model = db.query(Job).filter(Job.id == job_id).first()

    if not job_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    
    db.query(Job).filter(Job.id == job_id).delete()
    db.commit()


@router.delete('/application/{application_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_application(account: account_dependency, db: db_dependency, application_id: int = Path(gt=0)):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")
    
    application_model = db.query(Application).filter(Application.id == application_id).first()

    if not application_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    
    db.query(Application).filter(Application.id == application_id).delete()
    db.commit()


@router.delete('/account/{account_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_application(account: account_dependency, db: db_dependency, account_id: int = Path(gt=0)):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")
    
    account_model = db.query(Account).filter(Account.id == account_id).first()

    if not account_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    
    db.query(Account).filter(Account.id == account_id).delete()
    db.commit()


@router.delete('/location/{location_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_location(account: account_dependency, db: db_dependency, location_id: int = Path(gt=0)):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")
    
    location_model = db.query(Location).filter(Location.id == location_id).first()

    if not location_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Location not found")
    
    db.query(Location).filter(Location.id == location_id).delete()
    db.commit()


@router.delete('/social/{social_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_social(account: account_dependency, db: db_dependency, social_id: int = Path(gt=0)):

    if account.get('role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not an Admin")
    
    social_model = db.query(Social).filter(Social.id == social_id).first()

    if not social_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Location not found")
    
    db.query(Social).filter(Social.id == social_id).delete()
    db.commit()


# ROUTES FOR CREATING ADMIN ACCOUNT
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_admin_account(db: db_dependency, create_admin_request: AccountModelCreate):

    account_model = Account(
        login_name=create_admin_request.login_name,
        login_email=create_admin_request.login_email,
        hashed_password=hash_password(create_admin_request.password),
        role=create_admin_request.role
    )

    db.add(account_model)
    db.commit()
