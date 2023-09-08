import random
from yt_transcriber import db, YoutubeAPIKey


def random_youtube_api_key() -> YoutubeAPIKey:
    key = random.choice(db.query(YoutubeAPIKey).all())
    return key