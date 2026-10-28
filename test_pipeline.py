from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_analyze_endpoint_happy_path():
    csv_data = "name,age,city\nAlice,30,New York\nBob,25,London"
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("test.csv", csv_data.encode("utf-8"), "text/csv")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "success"
    assert data.get("row_count") == 2
    assert data.get("column_count") == 3


def test_analyze_endpoint_malformed_csv():
    # إرسال CSV بتنسيق تالف (علامة تنصيص غير مغلقة) لتفعيل ParserError داخل الـ pipeline وإرجاع status: error
    bad_csv_data = 'col1,col2\n"unclosed_quote,val2'
    response = client.post(
        "/api/v1/analyze",
        files={"file": ("bad.csv", bad_csv_data.encode("utf-8"), "text/csv")},
    )
    data = response.json()
    assert data.get("status") == "error"
