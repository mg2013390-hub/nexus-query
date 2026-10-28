from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_analyze_invalid_file_format():
    response = client.post(
        "/api/v1/analyze", files={"file": ("test.txt", b"some,data", "text/plain")}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Only CSV file formats are supported."}


def test_analyze_endpoint_empty_csv():
    empty_csv = "col1,col2\n"
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("empty.csv", empty_csv.encode("utf-8"), "text/csv")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "error"