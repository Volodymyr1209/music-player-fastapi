import logging

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from schemas.user import UserRegister
from services.users import UserService, get_user_service
from utils.security import security, verify_password

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
async def register(
    user_data: UserRegister,
    user_service: UserService = Depends(get_user_service),
):
    existing_user = await user_service.get_by_email(
        user_data.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    user = await user_service.create(user_data)

    return {
        "id": user.id,
        "email": user.email,
        "message": "User created",
    }


@router.post("/login")
async def login(
    credentials: OAuth2PasswordRequestForm = Depends(),
    user_service: UserService = Depends(get_user_service),
):
    user = await user_service.get_by_email(
        credentials.username,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    if not verify_password(
        credentials.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = security.create_access_token(
        uid=user.id,
        data={
            "role": user.role,
        },
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
