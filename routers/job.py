# IMPORING LOCAL PACKAGES
from fastapi import APIRouter, status, HTTPException, Path
from database.crud import db_dependency
from database.models import Job
from database.crud import get_job_data, get_job_data_for_dashboard
from sqlalchemy import desc


# DECLARING THE ROUTER
router = APIRouter(
    prefix='/job'
)


# CREATING ROUTES FOR JOBS
@router.get('/', status_code=status.HTTP_200_OK)
async def get_all_jobs(db: db_dependency):

    if not db.query(Job).all():
        return None
    
    job_id_list_desc = [job.id for job in db.query(Job).order_by(desc(Job.posted_on)).all()]
    
    return [get_job_data_for_dashboard(job_id, db_session=db) for job_id in job_id_list_desc]


# @router.get('/category', status_code=status.HTTP_200_OK)
# async def get_category():
#     category_list = ["accounting", "administration", "advertising", "agriculture", "arts and design", "banking", "biotechnology", "business development", "consulting", "customer service", "education", "engineering", "finance", "healthcare", "human resource", "information technology", "legal", "manufacturing", "marketing", "media and communication", "nonprofit", "retail", "sales", "science", "sports and recreation", "telecommunications", "transportation and logistics", "travel and tourism", "utilities"]
    
#     return category_list


@router.get('/{job_id}', status_code=status.HTTP_200_OK)
async def get_job(db: db_dependency, job_id: int = Path(gt=0)):
    job_model = get_job_data(job_id, db)

    if not job_model:
        return None
    
    return job_model
