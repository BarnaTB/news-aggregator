from main.app import app

from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_news():
    """Test that a user can fetch news successfully
    """
    response = client.get("/news/")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json())

def test_search_news():
    """Test that a user can search for news
    """
    response = client.get("/news?query=bitcoin")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json())
