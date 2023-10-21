# IMPORTING LOCAL PACKAGES
from fastapi import APIRouter, HTTPException, status
from security.auth import account_dependency, hash_password, verify_password
from database.models import User, Account, Application, Cover


# DECLARING THE ROUTER
router = APIRouter(
    prefix='/public'
)

