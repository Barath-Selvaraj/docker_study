from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.repositories import employee_repository
from app.schemas.employee import EmployeeCreate


def create_employee(
    db: Session,
    employee_data: EmployeeCreate
) -> Employee:

    employee = Employee(
        name=employee_data.name,
        dept=employee_data.dept,
        salary=employee_data.salary
    )

    return employee_repository.create_employee(
        db,
        employee
    )


def get_all_employees(
    db: Session
) -> list[Employee]:

    return employee_repository.get_all_employees(db)