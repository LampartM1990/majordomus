from bson.errors import InvalidId
from bson import ObjectId
from typing import List
from fastapi import APIRouter, Response, HTTPException
from app.models.demo import Task, TaskModel

demo_router = APIRouter()

# helper functions for task management
# TODO: Move helper function to tolls or services module


def validate_object_id(task_id: str) -> str:
    try:
        ObjectId(task_id)
        return task_id
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")


async def get_by_id_or_404(task_id: str) -> Task:
    task_id = validate_object_id(task_id)
    task = await Task.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


async def get_by_name_or_404(task_name: str) -> Task:
    task = await Task.find_one(Task.task_name == task_name)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


async def check_if_name_exists(task_name: str, exclude_task: Task = None) -> None:
    existing_task = await Task.find_one(Task.task_name == task_name)
    if existing_task and (not exclude_task or existing_task.id != exclude_task.id):
        raise HTTPException(status_code=400, detail="Task with this name already exists")


async def update_data(task: Task, task_data: TaskModel) -> Task:
    await check_if_name_exists(task_data.task_name, exclude_task=task)
    task.task_name = task_data.task_name
    task.task_type = task_data.task_type
    await task.save()
    return task

# API endpoints for demo tasks


@demo_router.get("/get-all", response_model=List[Task])
async def get_all() -> List[Task]:
    return await Task.find_all().to_list()


@demo_router.get("/get-all-pydantic", response_model=List[TaskModel])
async def get_all_pydantic() -> List[TaskModel]:
    tasks = await Task.find_all().to_list()
    return [TaskModel.model_validate(task) for task in tasks]


@demo_router.post("/create", response_model=Task)
async def create(task: TaskModel) -> Task:
    await check_if_name_exists(task.task_name)
    task_db = Task(**task.model_dump())
    return await task_db.insert()


@demo_router.get("/get/{task_id}", response_model=Task)
async def get_by_id(task_id: str) -> Task:
    return await get_by_id_or_404(task_id)


@demo_router.get("/get-by-name/{task_name}", response_model=Task)
async def get_by_name(task_name: str) -> Task:
    return await get_by_name_or_404(task_name)


@demo_router.put("/update/{task_id}", response_model=Task)
async def update_by_id(task_id: str, task_data: TaskModel) -> Task:
    existing_task = await get_by_id_or_404(task_id)
    return await update_data(existing_task, task_data)


@demo_router.put("/update-by-name/{task_name}", response_model=Task)
async def update_by_name(task_name: str, task_data: TaskModel) -> Task:
    existing_task = await get_by_name_or_404(task_name)
    return await update_data(existing_task, task_data)


@demo_router.delete("/delete/{task_id}", status_code=204)
async def delete(task_id: str) -> None:
    task = await get_by_id_or_404(task_id)
    await task.delete()


@demo_router.delete("/delete-by-name/{task_name}", status_code=204)
async def delete_by_name(task_name: str) -> None:
    task = await get_by_name_or_404(task_name)
    await task.delete()
