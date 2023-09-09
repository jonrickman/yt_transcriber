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
    return {"_id": "c5743bf5-5c2f-48c4-b31f-3499dc8b9b3e", "key": "some_fake_api_key"}


@fixture
async def client():
    async with AsyncClient(app=app, base_url=API_URL) as client:
        print("Client is ready")
        yield client
