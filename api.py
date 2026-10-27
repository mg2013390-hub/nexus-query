from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from pipeline import DataPipelineEngine

app = FastAPI(
    title="NexusQuery Analytics API",
    description="High-performance Asynchronous Data Pipeline & Analytics Engine",
    version="1.0.0"
)

class HealthResponse(BaseModel):
    status: str
    message: str

@app.get("/", response_model=HealthResponse)
async def health_check():
    return {"status": "healthy", "message": "NexusQuery Engine is running successfully."}

@app.post("/api/v1/analyze")
async def analyze_data(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV file formats are supported.")
    
    content = await file.read()
    result = await DataPipelineEngine.process_dataset(content)
    
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
        
    return result