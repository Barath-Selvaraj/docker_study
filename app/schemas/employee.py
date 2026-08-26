from pydantic import BaseModel, ConfigDict


class EmployeeCreate(BaseModel):
    name: str
    dept: str
    salary: float


class EmployeeResponse(BaseModel):
    id: int
    name: str
    dept: str
    salary: float

    model_config = ConfigDict(
        from_attributes=True
    )