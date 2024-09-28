from app.database.connection import mongodb

def get_user_collection():
    return mongodb.db.get_collection("users")

def get_projects_collection():
    return mongodb.db.get_collection("projects")
