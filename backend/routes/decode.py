from fastapi import APIRouter
from models.schema import UrlSchema, ResponseUrlSchema
from models import url_shortner

router = APIRouter(
    prefix="/decode",
    tags=["urlshortner"],
)

@router.get("/",response_model=ResponseUrlSchema)
def decode_url(url: str):
    """
    Desc: Decodes a shortened URL to its original URL
    Input: Short URL starting with 'https://short.est/'
    Output: Original URL
    
    """
    url = UrlSchema(url=url)

    decoded_url = url_shortner.decode(url.url)

    return {"Original url": decoded_url}