import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="API Service",
    description="A sample API service for demonstration purposes",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def read_root():
    return {"message": "Welcome to API Service"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    logger.info(f"Fetching item with ID: {item_id}")
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    logger.info(f"Creating item: {item.name}")
    return {"item_name": item.name, "item_price": item.price}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f"Updating item with ID: {item_id}")
    if item_id == 999:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "updated_item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f"Deleting item with ID: {item_id}")
    return {"message": "Item deleted successfully"}