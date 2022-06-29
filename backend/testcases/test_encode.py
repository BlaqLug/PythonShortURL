# importing files
from backend.models import url_shortner
from backend.routes.encode import router
from backend.testcases.config import test_app
from fastapi.testclient import TestClient


def test_decode_url():
    url = "https://fastapi.tiangolo.com/tutorial/"
    client = TestClient(router)
    response = client.get("/{url}")
    encoded_url = url_shortner.encode(url)
    assert response.status_code == 200
    assert response.json() == {"Short URL": encoded_url}

def test_decode_invalid_url(test_app):

    url = "www.google.com"
    response = test_app.get(f"/urlshortner/encode?url={url}")
    print(response.json())
    assert response.status_code == 500
    assert (
        response.json()["detail"]
        == "A URL should start with http:// or https://"
    )