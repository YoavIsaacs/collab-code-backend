from datetime import datetime

from bson import ObjectId

from app.database.collections import get_projects_collection
from app.models.project import ProjectModel

async def create_project(project: ProjectModel) -> ProjectModel:
    project_collection = get_projects_collection()

    project.created_at = datetime.now()
    project.updated_at = project.created_at

    project_dict = project.model_dump()

    result = await project_collection.insert_one(project_dict)

    project.id = str(result.inserted_id)
    return project

async def get_project_by_id(project_id: str):
    project_collection = get_projects_collection()
    project_dict = project_collection.find_one({"_id": ObjectId(project_id)})
    if project_dict:
        project_dict["id"] = str(project_dict["_id"])
        return ProjectModel(**project_dict)
    return None

async def update_project(project_id: str, update_data: dict):
    project_collection = get_projects_collection()
    update_data["updated_at"] = datetime.now()

    result = await project_collection.update_one(
        {"_id": ObjectId(project_id)},
        {"$set": update_data}
    )

    if result.modified_count:
        return await get_project_by_id(project_id)
    return None

async def delete_project(project_id: str) -> bool:
    project_collection = get_projects_collection()
    result = await project_collection.delete_one({"_id": ObjectId(project_id)})
    return result.deleted_count > 0
