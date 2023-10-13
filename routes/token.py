from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=['Token']
)


@router.post('/token', status_code=status.HTTP_201_CREATED)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return 'token'