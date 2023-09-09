import pytest_asyncio
import pytest
from httpx import AsyncClient
from starlette.testclient import TestClient
from yt_transcriber import API_URL, YoutubeAPIKey
from yt_transcriber.routers.youtube_api_keys import PREFIX, db
from fastapi.exceptions import HTTPException
from yt_transcriber import app

BASE_URL = f"{API_URL}{PREFIX}"


async def test_delete_key(client: AsyncClient, sample_youtube_api_key):
    key_id = "TODO"
    res = await client.delete(f"{BASE_URL}/{key_id}")
    assert res.status_code == 404


async def test_get_all_keys(client: AsyncClient):
    res = await client.get(f"{BASE_URL}/")
    assert res.status_code == 200
    assert res.content


async def test_create_key(client: AsyncClient, sample_youtube_api_key):
    res = await client.post(f"{BASE_URL}/", json=sample_youtube_api_key)
    assert res.status_code == 201


async def test_get_key(client: AsyncClient, sample_youtube_api_key):
    res = await client.get(f"{BASE_URL}/")
    assert res.status_code == 200








# @pytest.mark.asyncio
# def test_create_youtube_key(test_client, sample_youtube_api_key):
#     db["youtube_api_keys"].post({"_id": sample_youtube_api_key['fake_id']})


# @pytest.mark.anyio
# async def test_delete_youtube_api_keys(sample_youtube_api_key):
#     with pytest.raises(HTTPException):
#         async with AsyncClient(app=app, base_url=f"{API_URL}{PREFIX}") as client:
#             response = await client.delete(sample_youtube_api_key['fake_id'])
#         # await requests.delete(f"{API_URL}{PREFIX}/{sample_youtube_api_key['fake_id']}")



# async def test_insert_youtube_api_key(sample_youtube_api_key):
#     await requests.post(f"{API_URL}{PREFIX}/{sample_youtube_api_key}")
