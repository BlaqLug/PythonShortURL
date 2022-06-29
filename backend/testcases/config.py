import pytest
from backend import main
from starlette.testclient import TestClient


@pytest.fixture(scope="module")
def test_app():
    # set up
    with TestClient(main.app) as test_client:

        # testing
        yield test_client
