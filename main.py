# IMPORTING PACKAGES
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database.dbconfig import Base, Engine
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from security import auth
from routers import user, company, job, public
from administration import admin


# API INFORMATION
api_meta_desc = """
### Overview:

**AdmerkCorp.com** is a forward-thinking technology company at the forefront of the job application and recruitment industry. Our FastAPI-powered central API application serves as the backbone for all our innovative projects, seamlessly connecting job seekers with opportunities and empowering companies to find the perfect candidates. With **AdmerkCorp**, we're redefining the future of job search and recruitment, one API at a time.

**Central API Application: Powering Opportunities**

Our central API application, built on the robust FastAPI framework, serves as the backbone for all our ventures. It's the digital conduit connecting job seekers to their dream careers and enabling companies to find their perfect match. Through seamless integration and unparalleled functionality, we're revolutionizing how people apply for jobs and how organizations source top talent.

**Unmatched Innovation**

AdmerkCorp.com is synonymous with innovation. Our API application continually evolves, harnessing the latest advancements in technology to provide a user-friendly, efficient, and secure experience. Whether you're a job seeker looking for your next big break or a company seeking exceptional talent, our API is the gateway to your success.

**Your Future Starts Here**

Join us at AdmerkCorp.com and experience the future of job application and recruitment. With our central API at the heart of our operations, we're shaping a world where opportunities abound and businesses thrive. Your journey to success begins with us.
"""


tags_metadata = [
    {
        "name": "Homepage",
        "description": "Root Address of the API application"
    },
    {
        "name": "Terms of Services",
        "description": "Terms of Service for the API"
    },
    {
        "name": "Authentication",
        "description": "API Endpoints for Login and Register"
    },
    {
        "name": "User",
        "description": "API Endpoints for User"
    },
    {
        "name": "Company",
        "description": "API Endpoints for Company"
    },
    {
        "name": "Job",
        "description": "API Endpoints for Job"
    },
    {
        "name": "Public",
        "description": "API Endpoints for Public Routes"
    },
    {
        "name": "Admin",
        "description": "API Endpoints for Admin/System"
    }
]


app = FastAPI(
    title = "AdmerkCorp API",
    description=api_meta_desc,
    summary = "Central API for Admerk Corp.",
    version = "1.0.0",
    terms_of_service = "/terms",
    openapi_tags= tags_metadata,
    contact={
        "name": "Shishir Sabbir",
        "url": "http://www.shishirsabbir.com",
        "email": "shishir.sabbir@gmail.com"
    },
    license_info = {
        "name": "MIT License",
        "url": "https://github.com/shishirsabbir/admerkcorp_api/blob/main/LICENSE"
    }
)


# CORS ADDED FOR LOCAL CONNECTION OF CLIENT
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# SETTING UP THE DATABASE CONNECTION
Base.metadata.create_all(bind=Engine)


# DEFINING TEMPLATE DIRECTORY
templates = Jinja2Templates(directory="templates")


# MOUNTING STATIC FILES
app.mount('/static', StaticFiles(directory="static"), name="static")


# API HOME PAGE ROUTE
@app.get('/', response_class=HTMLResponse, tags=["Homepage"])
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# TERMS ROUTE
@app.get('/terms', response_class=HTMLResponse, tags=["Terms of Services"])
async def terms_of_services(request: Request):
    return templates.TemplateResponse("terms.html", {"request": request})


# USERS ROUTE
app.include_router(auth.router, tags=['Authentication'])
app.include_router(user.router, tags=['User'])
app.include_router(company.router, tags=['Company'])
app.include_router(job.router, tags=['Job'])
app.include_router(public.router, tags=['Public'])
app.include_router(admin.router, tags=['Admin'])
