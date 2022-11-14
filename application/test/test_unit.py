import re

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

import re


class pytest_regex:
    """Assert that a given string meets some expectations."""

    def __init__(self, pattern, flags=0):
        self._regex = re.compile(pattern, flags)

    def __eq__(self, actual):
        return bool(self._regex.match(actual))

    def __repr__(self):
        return self._regex.pattern

regex = pytest_regex('^[0-9a-fA-F]{12}\b')

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": regex ,"version":app.versionpi}

def test_pi_200():
    response = client.get("/pi/200")
    assert response.status_code == 200
    assert response.json() == {"runtime: 0:00:00 or 0.02 seconds.",f"running version 0.1.0 on container {regex}"}

def test_pi_limit():
    response = client.get("/pi/50001")
    assert response.status_code == 403
    assert response.json() == {"detail":"it's to much for a test"}