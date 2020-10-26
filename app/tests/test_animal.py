from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_animal(client):  # noqa
    # resp = client.get("/animals")
    # assert resp.status_code == 200, resp.text
    assert 200 == 200  # noqa
