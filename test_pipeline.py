import pytest
from fastapi.testclient import TestClient
from api import app
from pipeline import DataPipelineEngine

client = TestClient(app)

def test_analyze_valid_csv():
    csv_content = b"col1,col2\n1,2\n3,4"
    result = DataPipelineEngine.process_dataset(csv_content)
    import asyncio
    if asyncio.iscoroutine(result):
        result = asyncio.run(result)
        
    assert result["status"] == "success"
    assert "data" in result

def test_analyze_malformed_csv():
    bad_content = b""
    result = DataPipelineEngine.process_dataset(bad_content)
    import asyncio
    if asyncio.iscoroutine(result):
        result = asyncio.run(result)
        
    assert result["status"] == "error" or "message" in result