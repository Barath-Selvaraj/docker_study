from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    dept: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    salary: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )