import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_home_page_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"GCP CI/CD Flask Pipeline" in response.data


def test_health_endpoint_returns_healthy(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404