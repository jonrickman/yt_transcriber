## Some general functionalities 
- Lock behind logins
- Add API Keys (required for getting manifests, etc.)
- Download Youtube Videos
- Get manifest information for video ids, playlists
- Convert (any) Video into audio files
- Extract voice from audio files
    - should be searchable
- Search YouTube (behavior TBD) 
- Alter Metadata of downloaded files
- Maybe OCR of videos to gain more data?

## Eventual Tech Stack
### FARM Stack
- FastAPI - Backend  
- React - Frontend  
- Mongodb - db  

### Utilities
- ffmpeg - transcoder  
- TBD - audio transcriber  
- TBD - OCR  

### Docker Containers  
- Mongodb 
- ffmpeg+downloader+converter
- react


#### General Models
TODO
