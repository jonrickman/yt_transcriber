# from yt_dlp import YoutubeDL
import uuid
from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional


# class PyObjectId(ObjectId):
    # @classmethod
    # def __get_validators__(cls):
    #     yield cls.validate

    # @classmethod
    # def validate(cls, v):
    #     if not ObjectId.is_valid(v):
    #         raise ValueError("Invalid objectid")
    #     return ObjectId(v)

    # @classmethod
    # def __modify_schema_json_schema__(cls, field_schema):
    #     field_schema.update(type="string")


class YoutubeAPIKey(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    key: str = Field(...)


    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "key": "foobarbaz_id"
            }
        }


class UpdateYoutubeAPIKey(BaseModel):
    key: Optional[str]


    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "key": "foobarbaz_id"
            }
        }
