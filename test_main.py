from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_analyze_invalid_file_format():
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("test.txt", b"some random text data", "text/plain")}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Only CSV file formats are supported."