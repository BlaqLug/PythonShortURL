import os
from fastapi import HTTPException

import uuid # contains letters and integers
import json

#Add urls.json file path
url_json_path = os.path.abspath("models/urls.json")


def get_url_id(id: str) -> dict:
    """
    DESC: Gets the urls in the urls.json file
    """
    urls = {}
    with open(url_json_path, "r") as f:
        urls = json.load(f)
    return urls[id]


def write_to_urls(id: str, url: str) -> None:
    """
    DESC: Writes the id and the url to the urls.json file
    """
    urls = {}
    with open(url_json_path, "r") as f:
        urls = json.load(f)
    urls[id] = url
    with open(url_json_path, "w") as f:
        json.dump(urls, f)


cache = {}


def encode(url: str) -> str:
    """
    DESC: Encodes a URL to a shortened URL
    INPUT: URL
    OUTPUT: shortened URL

    """
    # encode url 6 characters
    id = str(uuid.uuid3(uuid.NAMESPACE_URL, url))[:6]
    
    # check url in cache
    if id not in cache:
        cache[id] = url

        # store the url and the shortened url in a dictionary
        write_to_urls(id=id, url=url)

    shortened_url = f"https://short.est/{id}"

    return shortened_url


def decode(url: str) -> str:
    """
    DESC: Decodes a shortened URL to its original URL
    INPUT: shortened URL
    OUTPUT: original URL
    """
    
    # break down the url
    id = url.split("/")[-1]

    # find url in cache
    print(f"cache: {cache}")
    if id in cache:
        return cache[id]

    try:
        url = get_url_id(id)
        return url
    except Exception as e:
        raise HTTPException(status_code=404, detail="URL not found")
