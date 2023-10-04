# IMPORTING MODULES
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# DATABASE URL (FOR SQLITE)
# SQL_DATABASE_URL = "sqlite:///admerkcorpDB.db"

# DATABASE URL (FOR POSTGRES)
# SQL_DATABASE_URL = "postgresql+psycopg2://postgres:shishir0077@localhost:5432/JobForGlobeDB"

# DATABASE URL (FOR MYSQL)
SQL_DATABASE_URL = "mysql+mysqlconnector://arnoliono:shishir0077@localhost:3306/AdmerkCorpDB"


# CREATING ENGINE FOR THE DATABASE (FOR SQLITE)
# Engine = create_engine(SQL_DATABASE_URL, connect_args={"check_same_thread": False})

# CREATING ENGINE FOR THE DATABASE (FOR MYSQL AND POSTGRES)
Engine = create_engine(SQL_DATABASE_URL)


# CREATE DATABASE SESSION
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


# CREATING BASE FOR TABLE CLASSES
Base = declarative_base()
