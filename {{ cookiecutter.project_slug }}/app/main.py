from fastapi import FastAPI
from contextlib import asynccontextmanager
from {{ cookiecutter.project_slug }}.app.core import config, logging
from {{ cookiecutter.project_slug }}.app.db.database import init_db
from {{ cookiecutter.project_slug }}.app.routers.v1 import users, items

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.setup_logging()
    await init_db()
    yield

app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.description }}",
    lifespan=lifespan
)

app.include_router(users.router, prefix="/api/v1")
app.include_router(items.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to {{ cookiecutter.project_name }}!"}