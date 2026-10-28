import pandas as pd


class PipelineError(Exception):
    """Custom exception raised for pipeline data processing errors."""

    pass


def process_pipeline(file_path: str):
    try:
        df = pd.read_csv(file_path)
        row_count, column_count = df.shape
        return {
            "status": "success",
            "row_count": row_count,
            "column_count": column_count,
            "message": "Data processed successfully",
        }
    except (pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        raise PipelineError(f"Failed to parse CSV data: {str(e)}")
    except Exception as e:
        raise PipelineError(f"Unexpected pipeline error: {str(e)}")
