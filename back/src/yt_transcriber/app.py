from fastapi import FastAPI
from yt_transcriber.routers import *


app = FastAPI()

app.include_router(youtube_api_keys_router)

