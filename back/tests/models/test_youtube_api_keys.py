from httpx import AsyncClient
from yt_transcriber import API_URL
from yt_transcriber.routers.youtube_api_keys import PREFIX

BASE_URL = f"{API_URL}{PREFIX}"


async def test_delete_key(client: AsyncClient, sample_youtube_api_key):
    # Create a key to test deleting it before doing other tests
    res = await client.post(f"{BASE_URL}/", json=sample_youtube_api_key)
    assert res.status_code == 201

    # Try to delete the created key
    key = f"{sample_youtube_api_key['_id']}"
    res = await client.delete(f"{BASE_URL}/{key}")
    assert res.status_code == 204


async def test_get_all_keys(client: AsyncClient):
    res = await client.get(f"{BASE_URL}/")
    assert res.status_code == 200
    assert res.content


async def test_create_key(client: AsyncClient, sample_youtube_api_key):
    res = await client.post(f"{BASE_URL}/", json=sample_youtube_api_key)
    assert res.status_code == 201


async def test_get_key(client: AsyncClient):
    res = await client.get(f"{BASE_URL}/")
    assert res.status_code == 200


async def test_get_random_key(client: AsyncClient):
    res = await client.get(f"{BASE_URL}/random/")
    assert res.status_code == 200


async def test_find_key(client: AsyncClient, sample_youtube_api_key):
    key = sample_youtube_api_key["key"]
    res = await client.get(f"{BASE_URL}/find/{key}")
    assert res.status_code == 200


async def test_find_and_delete_key(client: AsyncClient, sample_youtube_api_key):
    key = sample_youtube_api_key["key"]
    res = await client.get(f"{BASE_URL}/delete/{key}")
    assert res.status_code == 204
