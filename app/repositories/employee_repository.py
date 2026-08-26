from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.employee import Employee


def create_employee(
    db: Session,
    employee: Employee
) -> Employee:

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


def get_all_employees(
    db: Session
) -> list[Employee]:

    statement = select(Employee)

    return list(db.scalars(statement).all())