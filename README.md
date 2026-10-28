# nexus-query

A lightweight and robust FastAPI service designed for processing and validating tabular CSV data pipelines, backed by automated Pytest coverage and strict Ruff formatting standards.

## Architecture & Project Structure

The project follows a clean, modular structure separating API routing from core data pipeline logic:

- **`api.py`**: Handles incoming HTTP requests, file upload validation (`UploadFile`), and FastAPI endpoint routing (`/health`, `/api/v1/analyze`).
- **`pipeline.py`**: Encapsulates data processing logic utilizing Pandas, handling CSV ingestion, empty dataset checks, and custom `PipelineError` exceptions.
- **`models.py`**: Defines strict Pydantic data models (`AnalyzeResponse`) for request/response serialization and validation.
- **`test_main.py` & `test_pipeline.py`**: Comprehensive integration and unit test suites ensuring high code quality.

## Features

- **FastAPI Endpoints:** RESTful endpoints with robust error handling and response validation.
- **Data Pipeline:** Efficient Pandas-powered tabular data parsing and metrics extraction.
- **Quality Assurance:** Enforces 94%+ automated test coverage (`pytest-cov`) and strict formatting gates via Ruff and GitHub Actions CI/CD pipelines.

## Environment Configuration

Copy `.env.example` to `.env` to configure environment variables for local development or Docker deployment:

```env
PORT=8000
LOG_LEVEL=info