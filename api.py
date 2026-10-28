import os
from fastapi import FastAPI, File, HTTPException, UploadFile
from models import AnalyzeResponse
from pipeline import PipelineError, process_pipeline

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to Nexus Query API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_data(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400, detail="Invalid file type. Only CSV files are allowed."
        )

    temp_file_path = f"temp_{file.filename}"
    try:
        contents = await file.read()
        with open(temp_file_path, "wb") as f:
            f.write(contents)

        result = process_pipeline(temp_file_path)
        return AnalyzeResponse(**result)

    except PipelineError as e:
        return AnalyzeResponse(
            status="error", row_count=None, column_count=None, message=str(e)
        )
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
