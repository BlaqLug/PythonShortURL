# importing files

# import sys

# sys.path.insert(0,'/PythonDocker/backend/')

from backend.main import app

from fastapi.testclient import TestClient


def test_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "URL Shortner"}