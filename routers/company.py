# IMPORTING LOCAL PACKAGES
from fastapi import APIRouter, HTTPException, status
from security.auth import account_dependency, hash_password, verify_password
from database.crud import db_dependency, get_location, get_social, get_job_data_for_company
from database.schemas import ChangePasswordRequest, JobModel
from database.models import Account, Company, Job, Location, Application
from datetime import datetime
from sqlalchemy import desc


# DECLARING THE ROUTER
router = APIRouter(
    prefix="/company"
)


# CREATING ROUTES FOR USER'S
@router.get('/job', status_code=status.HTTP_200_OK)
async def get_all_jobs_by_company(account: account_dependency, db: db_dependency):

    if account.get('role') != 'company':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"{account.get('role')} is not allowed for this route")

    if len(db.query(Job).filter(Job.company == account.get('username')).all()) < 1:
        return None
    
    return [get_job_data_for_company(job_model.id, db_session=db) for job_model in db.query(Job).filter(Job.company == account.get('username')).order_by(desc(Job.posted_on)).all()]


@router.post('/job', status_code=status.HTTP_201_CREATED)
async def create_new_job(account: account_dependency, db: db_dependency, create_job_request: JobModel):

    if account.get('role') == 'user':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"{account.get('role')} is not allowed to create job")

    location_model = Location(**create_job_request.location.model_dump())
    db.add(location_model)
    db.commit()
    db.refresh(location_model)

    job_model = Job(
        job_title=create_job_request.job_title,
        company=account.get('username'),
        job_type=create_job_request.job_type,
        location=location_model.id,
        salary_amount=create_job_request.salary_amount,
        salary_duration=create_job_request.salary_duration,
        category=create_job_request.category,
        sub_category=create_job_request.sub_category,
        overview=create_job_request.overview,
        job_description=create_job_request.job_description,
        experience=create_job_request.experience,
        responsibility=create_job_request.responsibility,
        required_skills=create_job_request.required_skills,
        benefits=create_job_request.benefits,
        job_url=create_job_request.job_url
    )

    db.add(job_model)
    db.commit()
    db.refresh(job_model)


@router.get('/application', status_code=status.HTTP_200_OK)
async def get_all_application(account: account_dependency, db: db_dependency):
    
    if account.get('role') != 'company':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"{account.get('role')} is not allowed for this route")

    job_id_list = [job.id for job in db.query(Job).filter(Job.company == account.get('username')).all()]

    if len(job_id_list) < 1:
        return None

    return [{"job_id": single_job, "application": db.query(Application).filter(Application.job_id == single_job).all()} for single_job in job_id_list if db.query(Application).filter(Application.job_id == single_job).all()]
    

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

    account_model = db.query(Company).filter(Company.c_name == account.get('username')).first()

    return {
        "name": account_model.name,
        "c_name": account_model.c_name,
        "c_mail": account_model.c_mail,
        "social": get_social(account_model.social, db),
        "location": get_location(account_model.location, db),
        "website": account_model.website
    }
