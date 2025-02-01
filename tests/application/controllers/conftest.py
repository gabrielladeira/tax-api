import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def api_client() -> TestClient:
    test_client = TestClient(app)
    return test_client
