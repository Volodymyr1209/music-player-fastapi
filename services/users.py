from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from schemas.user import UserRegister
from settings.db import get_db
from utils.security import get_password_hash


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(
        self,
        email: str,
    ) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalars().first()

    async def create(
        self,
        data: UserRegister,
    ) -> User:
        user = User(
            username=data.username,
            email=data.email,
            password_hash=get_password_hash(data.password),
        )

        self.db.add(user)

        await self.db.commit()
        await self.db.refresh(user)

        return user


async def get_user_service(
    db: AsyncSession = Depends(get_db),
) -> UserService:
    return UserService(db)
