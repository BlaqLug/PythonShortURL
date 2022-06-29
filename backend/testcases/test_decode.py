# importing files
from backend.models import url_shortner
from backend.routes.encode import router
from backend.testcases.config import test_app
from fastapi.testclient import TestClient

def test_encode_url():
    url = "https://fastapi.tiangolo.com/tutorial/"
    client = TestClient(router)
    response = client.get("/{url}")
    decoded_url = url_shortner.decode(url)
    assert response.status_code == 200
    assert response.json() == {"Original URL": decoded_url}

def test_decode_invalid_url(test_app):

    url = "https://betterprogramming.pub/"
    response = test_app.get(f"/urlshortner/decode?url={url}")
    print(response.json())
    assert response.status_code == 500
    assert (
        response.json()["detail"]
        == "A URL should start with http:// or https://"
    )

def test_decode_url_not_found(test_app):

    url = "https://betterprogramming.pub/"
    response = test_app.get(f"/urlshortner/decode?url={url}")
    print(response.json())
    assert response.status_code == 404
    assert (
        response.json()["detail"]
        == "URL not found""
    )
