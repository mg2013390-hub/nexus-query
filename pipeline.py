import pandas as pd


class PipelineError(Exception):
    pass


def process_pipeline(file_path: str) -> dict:
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            raise PipelineError("Dataset is empty.")
        return {
            "status": "success",
            "row_count": len(df),
            "column_count": len(df.columns),
            "message": "Processed successfully",
        }
    except Exception as e:
        if isinstance(e, PipelineError):
            raise e
        raise PipelineError(str(e))
