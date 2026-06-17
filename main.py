from fastapi import FastAPI, HTTPException, status

from routers.artists import router as artists_router
from routers.auth import router as auth_router
from routers.files import router as files_router
from routers.tracks import router as tracks_router
from settings.db import ping
from utils.security import security

app = FastAPI()

app.include_router(auth_router)
app.include_router(artists_router)
app.include_router(files_router)

security.handle_errors(app)


app.include_router(tracks_router)


@app.get("/")
def index_root():
    return {"message": "Hello World!"}


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
async def db_healthcheck():
    is_alive = await ping()

    if not is_alive:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed",
        )

    return {
        "status": "healthy",
        "database": "connected",
    }
