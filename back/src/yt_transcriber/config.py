yt_dl_opts = {
			"convert": {
				"format": "bestaudio/best",
				"ffmpeg_location": "/Users/dev/code/git/pyt/venv/bin/ffmpeg",
				"postprocessors": [
					{
						"key": "FFmpegExtractAudio",
						"preferredcodec": "wav",
						"preferredquality": "192"
					}
				]
			},
			"download": {
				"format": "bestaudio/best",
				"outtmpl": "/Users/dev/code/git/pyt/downloads/%(title)s.mp4",
				"postprocessors": []
			}
		}

MONGO_USER = "admin"
MONGO_PASSWORD = "pass"
MONGO_PORT = 27017
MONGO_URL = "localhost"
MONGO_DB = "yt"

MONGODB_URL=f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_URL}/{MONGO_DB}?retryWrites=true&w=majority"
