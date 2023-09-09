import pytest_asyncio
import asyncio
from httpx import AsyncClient
from pytest import fixture
from yt_transcriber import app, API_URL

@fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@fixture
def sample_youtube_api_key():
    return {"fake_id":"64fb11bc6f584e990812fc78", "key": "some_fake_api_key"}


@fixture
async def client():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        print("Client is ready")
        yield client


# @fixture
# async def async_app_client():
#     async with AsyncClient(app=app, base_url='http://localhost:27017yt/api_keys') as client:
#         yield client
