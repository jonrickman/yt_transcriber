from fastapi import FastAPI, HTTPException, Response,status
from typing import List
import motor.motor_asyncio
from yt_transcriber import MONGODB_URL, YoutubeAPIKey

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.college


# @app.get("/")
# def home():
#     return "Works."



@app.get(
    "/", response_description="List all youtube api keys", response_model=List[YoutubeAPIKey]
)
async def list_youtube_api_keys():
    youtube_api_keys = await db["youtube_api_keys"].find().to_list(1000)
    return youtube_api_keys


@app.get(
    "/{id}", response_description="Get key with _id", response_model=YoutubeAPIKey
)
async def show_youtube_api_key(id: str):
    if (youtube_api_key := await db["youtube_api_keys"].find_one({"_id": id})) is not None:
        return youtube_api_key

    raise HTTPException(status_code=404, detail=f"API Key {id} not found")


@app.delete("/{id}", response_description="Delete a youtube api key")
async def delete_youtube_api_key(id: str):
    delete_result = await db["youtube_api_keys"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"API Key {id} not found")

