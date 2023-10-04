# IMPORTING MODULES
from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .dbconfig import Base


# CREATING CLASSES FOR SQL TABLE

# LOCATION TABLE
class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    data_id = Column(String(30), unique=True, nullable=False)
    country = Column(String(20), nullable=False)
    state = Column(String(20), nullable=True)
    map_url = Column(String(500), nullable=True)

    loc_user = relationship('User', back_populates='sec_loc')
    loc_company = relationship('Company', back_populates='sec_loc')
    loc_job = relationship('Job', back_populates='sec_loc')


# SOCIAL MEDIA TABLE
class Social(Base):
    __tablename__ = 'socials'

    id = Column(Integer, primary_key=True, index=True)
    data_id = Column(String(30), unique=True, nullable=False)
    facebook = Column(String(100), nullable=True)
    linkedin = Column(String(100), nullable=True)
    twitter = Column(String(100), nullable=True)
    instagram = Column(String(100), nullable=True)
    whatsapp = Column(String(100), nullable=True)

    soc_company = relationship('Company', back_populates='sec_social')


# USERS TABLE
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(20), nullable=True)
    last_name = Column(String(20), nullable=True)
    birth_date = Column(DateTime, nullable=False)
    email = Column(String(30), unique=True, index=True, nullable=False)
    location = Column(String(30), ForeignKey('locations.data_id', ondelete='SET NULL'), nullable=True)
    username = Column(String(30), unique=True, index=True, nullable=False)
    is_refugee = Column(Boolean, default=False, nullable=False)

    sec_loc = relationship('Location', back_populates='loc_user')
    apply_to = relationship('Application', back_populates='applicant')


# COMPANY TABLE
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    c_name = Column(String(30), unique=True, nullable=False, index=True)
    c_mail = Column(String(30), unique=True, nullable=False, index=True)
    social = Column(String(30), ForeignKey('socials.data_id', ondelete='SET NULL'), nullable=True)
    location = Column(String(30), ForeignKey('locations.data_id', ondelete='SET NULL'), nullable=True)
    website = Column(String(100), nullable=True)

    job = relationship('Job', back_populates='owner')
    sec_loc = relationship('Location', back_populates='loc_company')
    sec_social = relationship('Social', back_populates='soc_company')


# JOB TABLE
class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    name_id = Column(String(50), unique=True, nullable=False)
    job_title = Column(String(500), nullable=False)
    company = Column(String(30), ForeignKey('companies.c_name'))
    job_type = Column(Enum("fixed_price", "full_time", "part_time", "freelance", name="job type"))
    posted_on = Column(DateTime, server_default=func.now())
    location = Column(String(30), ForeignKey('locations.data_id'))
    salary_amount = Column(Float(precision=2))
    salary_duration = Column(Enum("weekly", "monthly", "hourly", name="salary type"))
    category = Column(Enum("accounting", "administration", "advertising", "agriculture", "arts and design", "banking", "biotechnology", "business development", "consulting", "customer service", "education", "engineering", "finance", "healthcare", "human resource", "information technology", "legal", "manufacturing", "marketing", "media and communication", "nonprofit", "retail", "sales", "science", "sports and recreation", "telecommunications", "transportation and logistics", "travel and tourism", "utilities", name="job category"))
    overview = Column(String(1500), nullable=True)
    job_description = Column(String(3000))
    experience = Column(Enum("fresher", "no_experience", "expert", "internship", "intermediate", name="experience level"))
    responsibility = Column(String(2000), nullable=True)
    required_skills = Column(String(500), nullable=True)
    benefits = Column(String(1500), nullable=True)
    job_url = Column(String(100), nullable=True)

    owner = relationship('Company', back_populates='job')
    sec_loc = relationship('Location', back_populates='loc_job')
    application = relationship('Application', back_populates='')
    


# ACCOUNT TABLE
class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    login_name = Column(String(30), unique=True, nullable=False, index=True)
    login_email = Column(String(30), unique=True, nullable=False, index=True)
    hashed_password = Column(String(100), nullable=False)
    role = Column(Enum("user", "company", "developer", "admin", name="account role"), nullable=False)


# JOB APPLY TABLE
class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(String(30), unique=True, nullable=False, index=True)
    user_acc = Column(String(30), ForeignKey('users.username'))
    job_id = Column(String(50), ForeignKey('jobs.name_id'))
    applied_on = Column(DateTime, server_default=func.now())

    applicant = relationship('User', back_populates='apply_to')
    applied_job = relationship('Job', back_populates='application')
