from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from backend.models.schema import UrlSchema, ResponseUrlSchema
from backend.models import url_shortner

def test_encode_url():
    router = APIRouter(
        prefix="/encode",
        tags=["urlshortner"],
    )

    @router.get("/",response_model=ResponseUrlSchema)
    def encode_url(url: str):
        """
        Encodes a URL to a shortened URL
        """
        url = UrlSchema(url=url)
        try:
            encoded_url = url_shortner.encode(url.url)
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"{url} is an invalid url")

        return {"short URL": encoded_url}