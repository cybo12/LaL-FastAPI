import re

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["version"] == app.version

#def test_pi_200():
#    response = client.get("/pi/200")
#    assert response.status_code == 200

def test_pi_limit():
    response = client.get("/pi/50001")
    assert response.status_code == 403
    assert response.json() == {"detail":"it's to much for a test"}