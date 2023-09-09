from fastapi import HTTPException, status, Body, APIRouter
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
import random
import motor.motor_asyncio
from yt_transcriber import MONGODB_URL, YoutubeAPIKey


PREFIX = "/yt/api_keys"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.yt
router = APIRouter(prefix=PREFIX)


@router.get(
    "/", response_description="List all youtube api keys", response_model=List[YoutubeAPIKey]
)
async def list_youtube_api_keys():
    youtube_api_keys = await db["youtube_api_keys"].find().to_list(1000)
    return youtube_api_keys


@router.get(
    "/{id}", response_description="Get key with _id", response_model=YoutubeAPIKey
)
async def get_youtube_api_key(id: str):
    if (youtube_api_key := await db["youtube_api_keys"].find_one({"_id": id})) is not None:
        return youtube_api_key

    raise HTTPException(status_code=404, detail=f"API Key {id} not found")


@router.post("/", response_description="Add new youtube api key", response_model=YoutubeAPIKey)
async def create_youtube_api_key(youtube_api_key: YoutubeAPIKey = Body(...)):
    youtube_api_key = jsonable_encoder(youtube_api_key)
    new_youtube_api_key = await db["youtube_api_keys"].insert_one(youtube_api_key)
    created_youtube_api_key = await db["youtube_api_keys"].find_one({"_id": new_youtube_api_key.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_youtube_api_key)


@router.delete("/{id}", response_description="Delete a youtube api key")
async def delete_youtube_api_key(id: str):
    delete_result = await db["youtube_api_keys"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"API Key {id} not found")


@router.get("/random/", response_description="Get a random youtube api key", response_model=YoutubeAPIKey)
async def get_random_youtube_api_key():
    # TODO: Improve this... gross
    keys = await db["youtube_api_keys"].aggregate([{'$sample': {'size': 100}}]).to_list(100)
    key = random.choice(keys)
    return Response(status_code=status.HTTP_200_OK,
                    content=str(key))


@router.get("/find/{key}", response_description="Get a youtube api key by key value", response_model=YoutubeAPIKey)
async def find_youtube_api_key(key: str):
    found_key = await db["youtube_api_keys"].find_one({"key": key})
    if found_key:
        return Response(status_code=status.HTTP_200_OK,
                        content=str(found_key))

    return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/delete/{key}", response_description="Delete a youtube api key by key value", response_model=YoutubeAPIKey)
async def find_and_delete_youtube_api_key(key: str):
    found_key = await db["youtube_api_keys"].find_one_and_delete({"key": key})
    if found_key:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return Response(status_code=status.HTTP_404_NOT_FOUND)
