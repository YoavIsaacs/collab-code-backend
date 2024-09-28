from app.database.connection import mongodb

def get_user_collection() -> None:
    return mongodb.db.get_collection("users")

def get_projects_collection() -> None:
    return mongodb.db.get_collection("projects")
