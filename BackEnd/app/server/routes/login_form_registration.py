from fastapi import APIRouter,
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.citizen import * 

from app.db import User, db
from app.schemas import UserCreate, UserRead, UserUpdate
from app.users import auth_backend, current_active_user, fastapi_users

router = APIRouter 
@router.get("/", response_description="citizens retrieved")
async def get_citizens():
    citizens = await retrieve_citizens()
    if citizens:
        return ResponseModel(citizens, "citizens data retrieved successfully")
    return ResponseModel(citizens, "Empty list returned")
@router.get("/{id}", response_description="citizen data retrieved")
async def get_citizen_data(id):
    citizen = await retrieve_citizen(id)
    if citizen:
        return ResponseModel(citizen, "citizen data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "citizen doesn't exist.")

@router.post("/", response_description="citizen data added into the database")
async def add_citizen_data(citizen: citizenSchema = Body(...)):
    citizen = jsonable_encoder(citizen)
    new_citizen = await add_citizen(citizen)
    return ResponseModel(new_citizen, "citizen added successfully.")

@router.delete("/{id}", response_description="citizen data deleted from the database")
async def delete_citizen_data(id: str):
    deleted_citizen = await delete_citizen(id)
    if deleted_citizen:
        return ResponseModel(
            "citizen with ID: {} removed".format(id), "citizen deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "citizen with id {0} doesn't exist".format(id)
    )
)
@router.put("/{id}")
async def update_citizen_data(id: str, req: UpdatecitizenModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_citizen = await update_citizen(id, req)
    if updated_citizen:
        return ResponseModel(
            "citizen with ID: {} name update is successful".format(id),
            "citizen name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the citizen data.",
    )