from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from models.schema import UrlSchema
from models import url_shortner

router = APIRouter(
    prefix="/encode",
    tags=["urlshortner"],
)


@router.get("/")
def encode_url(url: str):
    """
    DESC: Encodes a URL to a shortened URL
    Input: URL that starts with http:// or https://
    Output: shortened URL
    
    """
    url = UrlSchema(url=url)
    try:
        encoded_url = url_shortner.encode(url.url)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"{url} is an invalid url")

    return {"short URL": encoded_url}