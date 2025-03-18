from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from {{ cookiecutter.project_slug }}.app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        # Uncomment to create tables on startup (for dev)
        # await conn.run_sync(Base.metadata.create_all)
        pass

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session