from fastapi import FastAPI

from app.api.routes.employees import router as employee_router
from app.db.base import Base
from app.db.database import engine

# Import models so SQLAlchemy knows about them
from app.models.employee import Employee


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Employee Management API"
)


app.include_router(employee_router)