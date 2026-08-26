from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse
)
from app.services import employee_service


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post(
    "",
    response_model=EmployeeResponse
)
def create_employee(
    employee_data: EmployeeCreate,
    db: Session = Depends(get_db)
):

    return employee_service.create_employee(
        db,
        employee_data
    )


@router.get(
    "",
    response_model=list[EmployeeResponse]
)
def get_all_employees(
    db: Session = Depends(get_db)
):

    return employee_service.get_all_employees(db)