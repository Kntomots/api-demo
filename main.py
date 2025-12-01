from fastapi import FastAPI
from database import boards_collection
from bson import ObjectId
from schemas import Task

app = FastAPI()

def fix_id(item):
    item["id"] = str(item["_id"])
    del item["_id"]
    return item

@app.get("/boards")
async def get_boards():
    boards = []
    cursor = boards_collection.find({})  
    async for doc in cursor:
        boards.append(fix_id(doc))
    return boards
@app.get("/boards/{board_id}")
async def get_board_tasks(board_id: str):
    board = await boards_collection.find_one({"id": board_id})
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    
    result = {"lists": board["lists"]}
    
    
    return result
@app.get("/boards/{board_id}/lists/{list_id}")
async def get_tasks_from_list(board_id: str, list_id: str):
    board = await boards_collection.find_one({"id": board_id})
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    
    for lst in board["lists"]:
        if lst["id"] == list_id:
            return {
                "name": lst["name"],
                "tasks": lst["tasks"]
            }
        
    raise HTTPException(status_code=404, detail="List not found")
    
    
    return result
@app.post("/boards/{board_id}/lists/{list_id}")
async def add_task(board_id: str, list_id: str, task: Task):
    result = await boards_collection.update_one(
        {"id": board_id, "lists.id": list_id},
        {"$push": {"lists.$.tasks": task.dict()}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Board or list not found")

    return {"message": "Task added successfully", "task": task}