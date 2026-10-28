# NexusQuery

A high-performance FastAPI backend service designed for automated CSV data ingestion, validation, and querying pipelines with full CI/CD compliance and 100% test coverage.

---

## 🚀 What It Does
NexusQuery provides robust API endpoints to upload, validate, and process structured datasets (CSV format). It performs real-time data transformations, handles malformed inputs gracefully, and exposes health-check and analysis endpoints for enterprise-grade data management.

---

## 📂 Architecture
The project follows a clean separation of concerns split into two core layers:
* **`api.py` (FastAPI Layer):** Manages the web routing, HTTP request validation, file upload handlers, and response serialization.
* **`pipeline.py` (DataPipelineEngine Layer):** Implements the data processing logic, Pandas-based dataframe transformations, cleaning routines, and rigorous error-handling mechanisms.

---

## ⚙️ Installation
Clone the repository and install the required dependencies within your active Python virtual environment:

```bash
pip install -r requirements.txt