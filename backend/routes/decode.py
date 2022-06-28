from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from models.schema import UrlSchema, ResponseUrlSchema
from models import url_shortner

router = APIRouter(
    prefix="/decode",
    tags=["urlshortner"],
)

@router.get("/",response_model=ResponseUrlSchema)
def decode_url(url: str):
    """
    Decodes a shortened URL to its original URL
    """
    url = UrlSchema(url=url)

    decoded_url = url_shortner.decode(url.url)

    return {"url": decoded_url}

# add exception for decode