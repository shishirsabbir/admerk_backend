# IMPORTING MODULES
from .dbconfig import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends
from .models import Account, Job, Location, Social, Company, Application, User
from datetime import datetime


# FUNCTION FOR DATABASE CONNECTION AND DEPENDENCY INJECTION
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


# FUNCTION FOR CHECKING UNIQUE USERNAME
def check_username(username: str, db_session):
    user_model = db_session.query(Account).filter(Account.login_name == username).first()
    if user_model:
        return True
    # IF USER EXIST
    return False


# FUNCTION FOR CHECKING UNIQUE EMAIL
def check_email(email: str, db_session):
    user_model = db_session.query(Account).filter(Account.login_email == email).first()
    if user_model:
        return True
    # IF USER EXIST
    return False


# FUNCTION FOR GET LOCATION
def get_location(loc_id, db_session):
    return db_session.query(Location).filter(Location.id == loc_id).first()


# FUNCTION FOR GET SOCIAL
def get_social(social_id, db_session):
    return db_session.query(Social).filter(Social.id == social_id).first()


# FUNCTION FOR GET COMPANY INFO
def get_company_data(company_username, db_session):
    company_model = db_session.query(Company).filter(Company.c_name == company_username).first()
    
    # if not company_model:
    #     return None
    
    return {
        "id": company_model.id,
        "name": company_model.name,
        "c_name": company_model.c_name,
        "c_mail": company_model.c_mail,
        "social": get_social(company_model.social, db_session),
        "location": get_location(company_model.location, db_session),
        "website": company_model.website
    }


# FUNCTION FOR GET JOB DATA FOR COMPANY
def get_job_data_for_company(job_id: int, db_session):
    job_model = db_session.query(Job).filter(Job.id == job_id).first()

    # if not job_model:
    #     return None

    return {
        "id": job_model.id,
        "company": get_company_data(job_model.company, db_session),
        "job_type": job_model.job_type,
        "posted_on": job_model.posted_on,
        "job_title": job_model.job_title,
        "location": get_location(job_model.location, db_session),
        "salary_amount": job_model.salary_amount,
        "salary_duration": job_model.salary_duration,
        "experience": job_model.experience,
        "overview": job_model.overview,
        "job_description": job_model.job_description,
        "category": job_model.category,
        "responsibility": job_model.responsibility,
        "required_skills": job_model.required_skills,
        "benefits": job_model.benefits,
        "job_url": job_model.job_url
    }


# FUNCTION FOR GET JOB DATA FOR EVERYONE FOR DASHBOARD
def get_job_data_for_dashboard(job_id: int, db_session):
    job_model = db_session.query(Job).filter(Job.id == job_id).first()

    if not job_model:
        return None

    return {
        "id": job_model.id,
        "job_title": job_model.job_title,
        "company": get_company_data(job_model.company, db_session),
        "job_type": job_model.job_type,
        "posted_on": job_model.posted_on,
        "location": get_location(job_model.location, db_session),
        "salary_amount": job_model.salary_amount,
        "salary_duration": job_model.salary_duration,
        "experience": job_model.experience,
        "category": job_model.category,
        "sub_category": job_model.sub_category,
        "job_url": job_model.job_url
    }


# FUNCTION FOR GET JOB DATA FOR EVERYONE
def get_job_data(job_id: int, db_session):
    job_model = db_session.query(Job).filter(Job.id == job_id).first()

    if not job_model:
        return None

    return {
        "id": job_model.id,
        "company": get_company_data(job_model.company, db_session),
        "job_type": job_model.job_type,
        "posted_on": job_model.posted_on,
        "job_title": job_model.job_title,
        "location": get_location(job_model.location, db_session),
        "salary_amount": job_model.salary_amount,
        "salary_duration": job_model.salary_duration,
        "experience": job_model.experience,
        "overview": job_model.overview,
        "job_description": job_model.job_description,
        "category": job_model.category,
        "responsibility": job_model.responsibility,
        "required_skills": job_model.required_skills,
        "benefits": job_model.benefits,
        "job_url": job_model.job_url
    }


###############################################################################

# FUNCTION FOR CREATE JOB NAME ID
# def generate_job_name_id(company_name: str):
#     return company_name + datetime.now().strftime("%y%H%M%S")


# FUNCTION FOR GET JOB NAME ID LIST
def get_job_name_id_list(company_username, db_session):
    job_list = db_session.query(Job).filter(Job.company == company_username).all()

    if len(job_list) == 0:
        return None

    return [job.name_id for job in job_list]


# FUNCTION FOR GET USER DATA
def get_user_data(username, db_session):
    user_model = db_session.query(User).filter(User.username == username).first()

    if not user_model:
        return None

    return {
        "first_name": user_model.first_name,
        "last_name": user_model.last_name,
        "birth_date": user_model.birth_date,
        "username": user_model.username,
        "email": user_model.email,
        "location": get_location(user_model.location, db_session),
        "is_refugee": user_model.is_refugee
    }


# FUNCTION FOR GET JOB DATA USING NAME ID
def get_job_data_by_name_id(job_id: int, db_session):
    job_model = db_session.query(Job).filter(Job.id == job_id).first()

    if not job_model:
        return None

    return {
        "id": job_model.id,
        "company": get_company_data(job_model.company, db_session),
        "job_type": job_model.job_type,
        "posted_on": job_model.posted_on,
        "job_title": job_model.job_title,
        "location": get_location(job_model.location, db_session),
        "salary_amount": job_model.salary_amount,
        "salary_duration": job_model.salary_duration,
        "experience": job_model.experience,
        "overview": job_model.overview,
        "job_description": job_model.job_description,
        "category": job_model.category,
        "responsibility": job_model.responsibility,
        "required_skills": job_model.required_skills,
        "benefits": job_model.benefits,
        "job_url": job_model.job_url
    }


# FUNCTION FOR GET APPLICATION MODEL
def get_appliation_data(apply_id, db_session):
    application_model = db_session.query(Application).filter(Application.application_id == apply_id).first()

    return {
        "id": application_model.id,
        "application_id": application_model.application_id,
        "user_info": get_user_data(application_model.user_acc, db_session),
        "job_info": get_job_data_by_name_id(application_model.job_id, db_session),
        "applied_on": application_model.applied_on
    }


# FUNCTION FOR GET APPLICATION MODEL BY JOB NAME ID
def get_appliation_data_by_job_name_id(job_name_id, db_session):
    application_model = db_session.query(Application).filter(Application.job_id == job_name_id).first()
    
    return {
        "id": application_model.id,
        "application_id": application_model.application_id,
        "user_info": get_user_data(application_model.user_acc, db_session),
        "job_info": get_job_data_by_name_id(application_model.job_id, db_session),
        "applied_on": application_model.applied_on
    }
        