from fastapi import FastAPI, HTTPException
from database import boards_collection
from bson import ObjectId
from schemas import Task

app = FastAPI()

def fix_id(item):
    item["id"] = str(item["_id"])
    del item["_id"]
    return item

@app.get("/boards")
async def get_all_project_boards():
    boards = []
    cursor = boards_collection.find({})  
    async for doc in cursor:
        boards.append(fix_id(doc))
    return boards
@app.get("/boards/{board_name}")
async def get_board_tasks(board_name: str):
    board = await boards_collection.find_one({"name": board_name})
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    
    result = {
        "name": board["name"],
        "lists": board["lists"]}
    
    
    return result
@app.get("/boards/{board_name}/lists/{list_id}")
async def get_tasks_from_board_list(board_name: str, list_id: str):
    board = await boards_collection.find_one({"name": board_name})
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    
    for lst in board["lists"]:
        if lst["id"] == list_id:
            return {
                "name": lst["name"],
                "tasks": lst["tasks"]
            }
        
    raise HTTPException(status_code=404, detail="List not found")   
    
@app.post("/boards/{board_name}/lists/{list_id}")
async def add_task_to_board(board_name: str, list_id: str, task: Task):
    result = await boards_collection.update_one(
        {"name": board_name, "lists.id": list_id},
        {"$push": {"lists.$.tasks": task.dict()}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Board or list not found")

    return {"message": "Task added successfully", "task": task}

@app.put("/boards/{board_name}/tasks/{task_id}/move")
async def move_task(board_name: str, task_id: str, source_list_id: str, dest_list_id: str):
    board = await boards_collection.find_one({"name": board_name})
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")

    task_to_move = None
    for lst in board["lists"]:
        if lst["id"] == source_list_id:
            for task in lst["tasks"]:
                if task["id"] == task_id:
                    task_to_move = task
                    lst["tasks"].remove(task)
                    break

    if not task_to_move:
        raise HTTPException(status_code=404, detail="Task not found in source list")

    for lst in board["lists"]:
        if lst["id"] == dest_list_id:
            lst["tasks"].append(task_to_move)
            break
    else:
        raise HTTPException(status_code=404, detail="Destination list not found")

    await boards_collection.update_one(
        {"name": board_name},
        {"$set": {"lists": board["lists"]}}
    )

    return {"message": "Task moved successfully", "task": task_to_move}

@app.delete("/boards/{board_name}/tasks/{task_id}")
async def delete_task(board_name: str, task_id: str):
    board = await boards_collection.find_one({"name": board_name})
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")

    task_found = False
    for lst in board["lists"]:
        for task in lst["tasks"]:
            if task["id"] == task_id:
                lst["tasks"].remove(task)
                task_found = True
                break
        if task_found:
            break

    if not task_found:
        raise HTTPException(status_code=404, detail="Task not found")

    await boards_collection.update_one(
        {"name": board_name},
        {"$set": {"lists": board["lists"]}}
    )

    return {"message": "Task deleted successfully"}