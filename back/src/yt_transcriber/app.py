from fastapi import FastAPI
from yt_transcriber.routers import youtube_api_keys_router


app = FastAPI()

app.include_router(youtube_api_keys_router)
