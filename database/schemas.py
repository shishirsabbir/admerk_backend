# IMPORTING MODULES
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


# CREATING PYDANTIC CLASSES FOR LOCATION MODEL
class LocationModel(BaseModel):
    # data_id: str
    country: str = Field(max_length=20)
    state: str | None = Field(max_length=20)
    map_url: str | None = Field(max_length=500)


# CREATING PYDANTIC CLASSES FOR SOCIAL MODEL
class SocialModel(BaseModel):
    # data_id: str
    facebook: str | None = Field(max_length=100)
    linkedin: str | None = Field(max_length=100)
    twitter: str | None = Field(max_length=100)
    instagram: str | None = Field(max_length=100)
    whatsapp: str | None = Field(max_length=100)



# CREATING PYDANTIC CLASSES FOR USER'S ACCOUNT MODEL
class UserModel(BaseModel):
    first_name: str | None = Field(max_length=20, default=None)
    last_name: str | None = Field(max_length=20, default=None)
    birth_date: datetime = Field(default=datetime(year=1996, month=5, day=8))
    email: str = Field(max_length=30)
    location: LocationModel | None = None
    username: str = Field(max_length=30)
    password: str = Field(min_length=8)
    is_refugee: bool = Field(default=False)
    role: str = Field(default="user")

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "arno",
                    "last_name": "liono",
                    "birth_date": "1999-05-08T00:00:00",
                    "email": "arnoliono@gmail.com",
                    "location": {
                        "country": "bangladesh",
                        "state": "",
                        "map_url": "https://maps.app.goo.gl/LVEb1R1NJk2LYgS89"
                    },
                    "username": "arnoliono",
                    "password": "test1234",
                    "is_refugee": False
                }
            ]
        }
    }


# CREATE PYDANTIC CLASS FOR COMPANY'S ACCOUNT MODEL
class CompanyModel(BaseModel):
    name: str = Field(max_length=30)
    c_name: str = Field(max_length=30)
    c_mail: str = Field(max_length=30)
    password: str = Field(min_length=8)
    social: SocialModel | None = None
    location: LocationModel | None = None
    website: str = Field(max_length=100)
    role: str = Field(default='company')

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "pepsico",
                    "c_name": "pepsicouk",
                    "c_mail": "company@pepsico.co.uk",
                    "password": "test1234",
                    "social": {
                        "facebook": "https://www.facebook.com",
                        "linkedin": "https://www.pepsicouk.com",
                        "twitter": "https://www.twitter.com",
                        "instagram": "https://www.instagram.com",
                        "whatsapp": "https://wa.me/message/2UQHWE2LXVUDF1"
                    },
                    "location": {
                        "country": "united kingdom",
                        "state": "greater manchester",
                        "map_url": "https://maps.app.goo.gl/LVEb1R1NJk2LYgS89"
                    },
                    "website": "https://www.pepsicouk.com"
                }
            ]
        }
    }


# PYDANTIC CLASSES FOR JWT TOKEN, CREATE ACCOUNT, PASSWORD CHANGE REQUEST
class Token(BaseModel):
    access_token: str
    token_type: str
    login_data: dict | None = None


# PYDANTIC CLASSES PASSWORD CHANGE REQUEST
class ChangePasswordRequest(BaseModel):
    password: str
    new_password: str

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "password": "test1234",
                    "new_password": "@test123"
                }
            ]
        }
    }


# PYDANTIC CLASS FOR LOGIN ACCOUNT MODEL
class AccountModel(BaseModel):
    login_name: str = Field(max_length=30)
    login_email: str = Field(max_length=30)
    hashed_password: str
    role: Literal["user", "company", "developer", "admin"]


class ValidateRequest(BaseModel):
    username: str | None = None
    email: str | None = None

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "username/email": "username/user@mail.com"
                }
            ]
        }
    }


# PYDANTIC CLASS FOR JOB MODEL
class JobModel(BaseModel):
    # name_id: str = Field(max_length=50)
    job_title: str = Field(max_length=500)
    # company: str = Field(max_length=30)
    job_type: Literal["fixed_price", "full_time", "part_time", "freelance"]
    # posted_on: datetime
    location: LocationModel | None = None
    salary_amount: float | None = None
    salary_duration: Literal["weekly", "monthly", "hourly"]
    category: Literal["accounting", "administration", "advertising", "agriculture", "arts and design", "banking", "biotechnology", "business development", "consulting", "customer service", "education", "engineering", "finance", "healthcare", "human resource", "information technology", "legal", "manufacturing", "marketing", "media and communication", "nonprofit", "retail", "sales", "science", "sports and recreation", "telecommunications", "transportation and logistics", "travel and tourism", "utilities"]
    overview: str | None = Field(max_length=1500)
    job_description: str = Field(3000)
    experience: Literal["fresher", "no_experience", "expert", "internship", "intermediate"]
    responsibility: str | None = Field(max_length=2000)
    required_skills: str | None = Field(500)
    benefits: str | None = Field(1500)
    job_url: str | None = Field(100)

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "job_type": "full_time",
                    "job_title": "Software Engineer",
                    "location": {
                        "country": "united kingdom",
                        "state": "greater manchester",
                        "map_url": "https://maps.app.goo.gl/LVEb1R1NJk2LYgS89"
                    },
                    "salary_amount": 7500.00,
                    "salary_duration": "monthly",
                    "experience": "fresher",
                    "overview": "This is a great opportunity for a software engineer.",
                    "job_description": "Responsible for developing and maintaining software applications.",
                    "category": "information technology",
                    "responsibility": "Write clean, maintainable code.",
                    "required_skills": "Python, JavaScript, SQL",
                    "benefits": "Healthcare, 401(k), flexible hours",
                    "job_url": "https://hellojob24.com/todays/job/234234/getsoftwarejob/noapplicaton/2"
                }
            ]
        }
    }


# PYDANTIC CLASS FOR JOB RESPONSE MODEL
class JobResponseModel(BaseModel):
    id: int
    name_id: str
    company: str
    job_type: Literal["fixed_price", "full_time", "part_time", "freelance"]
    posted_on: datetime
    job_title: str
    location: LocationModel | None = None
    salary_amount: float | None = None
    salary_duration: str
    experience: str
    overview: str | None = None
    job_description: str
    category: str
    responsibility: str | None = None
    required_skills: str | None = None
    benefits: str | None = None
    job_url: str | None = None


# PYDANTIC CLASS FOR JOB APPLICATION
class ApplicationModel(BaseModel):
    # application_id: str = Field(max_length=15)
    job_id: str = Field(max_length=50)
    
    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "job_id": "enter_the_job_name_id"
                }
            ]
        }
    }


# PYDANTIC CLASS FOR CREATE ACCOUNT MODEL
class AccountModelCreate(BaseModel):
    login_name: str = Field(max_length=30)
    login_email: str = Field(max_length=30)
    password: str
    role: Literal["user", "company", "developer", "admin"]

    model_config= {
            "json_schema_extra": {
                "examples": [
                    {
                        "login_name": "shishirsabbir",
                        "login_email": "shishir.sabbir@gmail.com",
                        "password": "test1234",
                        "role": "admin"
                    }
                ]
            }
        }
