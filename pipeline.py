import pandas as pd
import io

class DataPipelineEngine:
    @classmethod
    def process_dataset(cls, file_contents: bytes):
        try:
            df = pd.read_csv(io.BytesIO(file_contents))
            if df.empty:
                return {"status": "error", "message": "Empty dataframe"}
            return {
                "status": "success",
                "row_count": len(df),
                "column_count": len(df.columns)
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}