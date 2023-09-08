from fastapi import FastAPI, HTTPException, status, Body
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
import motor.motor_asyncio
from yt_transcriber import MONGODB_URL, YoutubeAPIKey, UpdateYoutubeAPIKey

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.yt


@app.get(
    "/", response_description="List all youtube api keys", response_model=List[YoutubeAPIKey]
)
async def list_youtube_api_keys():
    youtube_api_keys = await db["youtube_api_keys"].find().to_list(1000)
    return youtube_api_keys


@app.get(
    "/{id}", response_description="Get key with _id", response_model=YoutubeAPIKey
)
async def get_youtube_api_key(id: str):
    if (youtube_api_key := await db["youtube_api_keys"].find_one({"_id": id})) is not None:
        return youtube_api_key

    raise HTTPException(status_code=404, detail=f"API Key {id} not found")


@app.post("/", response_description="Add new youtube api key", response_model=YoutubeAPIKey)
async def create_youtube_api_key(youtube_api_key: YoutubeAPIKey = Body(...)):
    youtube_api_key = jsonable_encoder(youtube_api_key)
    new_youtube_api_key = await db["youtube_api_keys"].insert_one(youtube_api_key)
    created_youtube_api_key = await db["youtube_api_keys"].find_one({"_id": new_youtube_api_key.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_youtube_api_key)


# @app.put("/{id}", response_description="Update a YoutubeAPIKey", response_model=YoutubeAPIKey)
# async def update_youtube_api_key(id: str, api_key: UpdateYoutubeAPIKey = Body(...)):
#     api_key = {k: v for k, v in api_key.dict().items() if v is not None}

#     if len(api_key) >= 1:
#         update_result = await db["youtube_api_keys"].update_one({"_id": id}, {"$set": api_key})

#         if update_result.modified_count == 1:
#             if (
#                 updated_youtube_api_key := await db["youtube_api_keys"].find_one({"_id": id})
#             ) is not None:
#                 return updated_youtube_api_key

#     if (existing_api_key := await db["youtube_api_keys"].find_one({"_id": id})) is not None:
#         return existing_api_key

#     raise HTTPException(status_code=404, detail=f"Youtube API Key {id} not found")


@app.delete("/{id}", response_description="Delete a youtube api key")
async def delete_youtube_api_key(id: str):
    delete_result = await db["youtube_api_keys"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"API Key {id} not found")
