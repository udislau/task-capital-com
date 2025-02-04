import os
import logging
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.storage import get_storage

# Set up basic logging.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app_logger")
logging.getLogger("uvicorn").propagate = False
logging.getLogger("fastapi").propagate = False

app = FastAPI(
    title="Simple Web Api",
    description="A simple API for storing and retrieving a string.",
    version="1.0.0",
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE_PATH = os.path.join(BASE_DIR, "static", "index.html")


@app.get("/", response_class=FileResponse)
async def index():
    """
    Serve the static HTML file as the documentation page.
    """
    return FileResponse(HTML_FILE_PATH, media_type="text/html")


class StringPayload(BaseModel):
    value: str


@app.post("/store", status_code=201)
async def store_string(payload: StringPayload, storage=Depends(get_storage)):
    """
    Store a string passed in the JSON payload.
    """
    storage.value = payload.value
    logger.info("Stored value: %s", payload.value)
    return {"message": "Value stored successfully."}


@app.get("/store")
async def get_string(storage=Depends(get_storage)):
    """
    Retrieve the stored string.
    """
    if not storage.value:
        logger.info("Attempt to retrieve value, but no value stored.")
        raise HTTPException(status_code=404, detail="No value stored.")
    logger.info("Retrieved value: %s", storage.value)
    return {"value": storage.value}
