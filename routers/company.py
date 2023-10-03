# IMPORTING LOCAL PACKAGES
from fastapi import APIRouter, HTTPException, status
from security.auth import account_dependency, hash_password, verify_password
from database.crud import db_dependency, generate_job_name_id, get_location, get_social, get_job_name_id_list, get_job_data_for_company, get_appliation_data_by_job_name_id
from database.schemas import ChangePasswordRequest, JobModel
from database.models import Account, Company, Job, Location
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You haven't posted any jobs to us")
    
    return [get_job_data_for_company(job_model.id, db_session=db) for job_model in db.query(Job).filter(Job.company == account.get('username')).order_by(desc(Job.posted_on)).all()]


@router.post('/job', status_code=status.HTTP_201_CREATED)
async def create_new_job(account: account_dependency, db: db_dependency, create_job_request: JobModel):

    if account.get('role') == 'user':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"{account.get('role')} is not allowed to create job")
    
    job_name_id = generate_job_name_id(account.get('username'))

    if create_job_request.location:
        location_id = f'loc{datetime.now().strftime("%y%m%d%H%M%S")}'
        location_model = Location(data_id=location_id, **create_job_request.location.model_dump())
        
        db.add(location_model)
        db.commit()
        db.refresh(location_model)

    job_model = Job(
        name_id=job_name_id,
        company=account.get('username'),
        job_type=create_job_request.job_type,
        job_title=create_job_request.job_title,
        location=location_model.data_id,
        salary_amount=create_job_request.salary_amount,
        salary_duration=create_job_request.salary_duration,
        experience=create_job_request.experience,
        overview=create_job_request.overview,
        job_description=create_job_request.job_description,
        category=create_job_request.category,
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
    company_job_name_id_list = get_job_name_id_list(account.get('username'), db)

    if account.get('role') != 'company':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"{account.get('role')} is not allowed for this route")

    if len(company_job_name_id_list) < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No application found on your posted jobs')
    
    return [get_appliation_data_by_job_name_id(job_name_id, db) for job_name_id in company_job_name_id_list]

    # return [db.query(Application).filter(Application.job_id == job_name_id).order_by(desc(Application.applied_on)).first() for job_name_id in company_job_name_id_list]


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
