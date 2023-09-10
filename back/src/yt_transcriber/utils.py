import json
import requests
from yt_transcriber import API_URL, YoutubeVideoManifest
from yt_transcriber.routers.youtube_api_keys import PREFIX


def get_video_manifest(video_id: str) -> YoutubeVideoManifest:
    # TODO: Check db for manifest by video_id

    # if it wasn't in the database then get it
    response = requests.get(f"{API_URL}{PREFIX}/random/")
    api_key = json.loads(response.content.decode('utf8').replace("'", '"'))
    key_value = api_key["key"]

    # get the manifest from the google api
    api_url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={key_value}&part=snippet"
    manifest = json.loads(requests.get(api_url).content)

    # save manifest

    # return the manifest
    return manifest


if __name__ == "__main__":
    # sample video id
    get_video_manifest("qlZ74NTSaAc")
