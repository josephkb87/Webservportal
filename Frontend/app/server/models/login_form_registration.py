from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class citizenSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    city_of_birth: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "city_of_birth": "Water resources engineering",
                "year": 2,
                "gpa": "3.0",
            }
        }


class UpdatecitizenModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    city_of_birth: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Clyde King Kid",
                "email": "clydekingkid@gmail.com",
                "city_of_birth": "Computer Science",
                "year": 4,
                "gpa": "4.0",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}