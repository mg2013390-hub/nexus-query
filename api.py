from fastapi import FastAPI, File, UploadFile, HTTPException
from pipeline import DataPipelineEngine

app = FastAPI(title="Nexus Query API")


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/api/v1/analyze")
async def analyze_data(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400, detail="Only CSV file formats are supported."
        )

    content = await file.read()

    # استدعاء دالة المعالجة بشكل صحيح بدون await لأنها دالة عادية (Sync)
    result = DataPipelineEngine.process_dataset(content)

    return result
