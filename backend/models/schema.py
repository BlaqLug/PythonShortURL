from pydantic import BaseModel, HttpUrl, validator
from fastapi import HTTPException


class UrlSchema(BaseModel):
    url: str

    @validator("url")
    def validate_url(cls, value):
        if not value.startswith("http://") and not value.startswith("https://"):
            raise HTTPException(
                status_code=500,
                detail="A URL should start with http:// or https://",
            )
        return value


class ResponseUrlSchema(BaseModel):
    url: HttpUrl