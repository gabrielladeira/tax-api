import pytest


class TestHealthCheckController:
    @pytest.fixture(autouse=True)
    def setup(self, api_client) -> None:
        self._api_client = api_client

    def test_health_check_success(self) -> None:
        response = self._api_client.get("/health-check")

        assert response.status_code == 200
        assert response.json() == {"success": True, "message": "Service is running successfully"}
