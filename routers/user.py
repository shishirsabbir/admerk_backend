# IMPORTING LOCAL PACKAGES
from fastapi import APIRouter, HTTPException, status
from security.auth import account_dependency, hash_password, verify_password
from database.crud import db_dependency, get_location, get_appliation_data
from database.schemas import ChangePasswordRequest, ApplicationModel
from database.models import User, Account, Application
from datetime import datetime
from sqlalchemy import desc


# DECLARING THE ROUTER
router = APIRouter(
    prefix="/user"
)


# CREATING ROUTES FOR USER'S
@router.post('/application', status_code=status.HTTP_201_CREATED)
async def apply_to_job(account: account_dependency, db: db_dependency, application_request: ApplicationModel):

    application_model = Application(
        application_id=f'app{datetime.now().strftime("%y%m%d%H%M%S")}',
        user_acc=account.get('username'),
        job_id=application_request.job_id,
    )

    db.add(application_model)
    db.commit()


@router.get('/application', status_code=status.HTTP_200_OK)
async def get_all_application(account: account_dependency, db: db_dependency):
    application_list = db.query(Application).filter(Application.user_acc == account.get('username')).all()

    if account.get('role') != 'user':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"{account.get('role')} is not allowed for this route")

    if len(application_list) < 1:
        return None
    
    application_id_list_desc = [application_model.application_id for application_model in db.query(Application).filter(Application.user_acc == account.get('username')).order_by(desc(Application.applied_on)).all()]
    
    return [get_appliation_data(apply_id, db) for apply_id in application_id_list_desc]


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
    