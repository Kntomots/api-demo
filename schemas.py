from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str

class Task(BaseModel):
    id: str
    title: str
    description: str | None = None
