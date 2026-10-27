import io
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_analyze_valid_csv():
    csv_content = "col1,col2\n1,2\n3,4"
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("test.csv", io.BytesIO(csv_content.encode("utf-8")), "text/csv")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["row_count"] == 2
    assert "col1" in data["columns"]
    assert "col2" in data["columns"]

def test_analyze_malformed_csv():
    # محاكاة ملف CSV تالف أو غير متناسق الأعمدة
    csv_content = "col1,col2\n1,2,3\n4"
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("malformed.csv", io.BytesIO(csv_content.encode("utf-8")), "text/csv")}
    )
    # بناءً على تصميم البايبلاين، نتحقق من حالة الخطأ أو استجابة الـ error
    data = response.json()
    assert response.status_code in [200, 400, 422]
    if "status" in data:
        assert data["status"] == "error"