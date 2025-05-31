from beanie import Document
from pydantic import BaseModel
from pymongo import IndexModel


class TaskModel(BaseModel):
    task_name: str
    task_type: str
    model_config = {
        "from_attributes": True
    }


class Task(Document):
    task_name: str
    task_type: str

    class Settings:
        name = "demo_tasks" # Collection name in MongoDB
        indexes = [
            IndexModel([("task_name", 1)], unique=True)
        ]
