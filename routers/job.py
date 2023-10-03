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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No jobs found")
    
    job_id_list_desc = [job.id for job in db.query(Job).order_by(desc(Job.posted_on)).all()]
    
    return [get_job_data_for_dashboard(job_id, db_session=db) for job_id in job_id_list_desc]


@router.get('/{job_id}', status_code=status.HTTP_200_OK)
async def get_job(db: db_dependency, job_id: int = Path(gt=0)):
    job_model = get_job_data(job_id, db)

    if not job_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    
    return job_model
