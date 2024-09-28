from app.database.collections import get_user_collection
from app.models.user import UserModel
from datetime import datetime
from bson import ObjectId

async def create_user(user: UserModel) -> UserModel:
    user_collection = get_user_collection()

    user.created_at = datetime.now()
    user.updated_at = user.created_at

    user_dict = user.model_dump()
    result = await user_collection.insert_one(user_dict)

    user.id = str(result.inserted_id)
    return user

async def get_user_by_id(user_id: str):
    user_collection = get_user_collection()
    user_dict = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user_dict:
        user_dict["id"] = str(user_dict["_id"])
        return UserModel(**user_dict)
    return None

async def update_user(user_id: str, update_data: dict):
    user_collection = get_user_collection()
    update_data["updated_at"] = datetime.now()
    result = await user_collection.update_one(
        {"id": ObjectId(user_id)},
        {"$set": update_data}
    )

    if result.modified_count:
        return await get_user_by_id(user_id)
    return None

async def delete_user(user_id: str) -> bool:
    user_collection = get_user_collection()
    result = await user_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0
