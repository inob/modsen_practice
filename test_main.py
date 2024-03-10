 
import pytest
from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)

def test_search():
    response = client.get("/search/test")
    assert response.status_code == 200

def test_delete():
    response = client.delete("/delete/1")
    assert response.status_code == 200
