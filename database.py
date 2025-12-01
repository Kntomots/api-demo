# database.py
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://kostasntomotsidis_db_user:dh33AlV646AVzzVJ@cluster0.nrbrten.mongodb.net/Taskmanager?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_URL)

db = client["Taskmanager"]   # database name
boards_collection = db["Boards"]  # collection

