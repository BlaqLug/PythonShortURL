# importing files
from backend.testcases.config import test_app

def test_main():
    
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "URL Shortner"}