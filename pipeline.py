import io
import numpy as np
import pandas as pd

def analyze_csv(file_content: bytes) -> dict:
    """
    دالة لتحليل ملفات الـ CSV، معالجة البيانات، وتنظيف القيم غير القياسية
    لتتوافق تماماً مع متطلبات الـ JSON ومعايير FastAPI.
    """
    try:
        # قراءة ملف الـ CSV من المحتوى الثنائي (Bytes)
        df = pd.read_csv(io.BytesIO(file_content))
        
        # التأكد من التعامل مع الملفات الفارغة أو التالفة
        if df.empty:
            return {
                "status": "success",
                "rows": 0,
                "columns": 0,
                "data": []
            }

        # حساب بعض الإحصائيات الأساسية (اختياري حسب متطلبات مشروعك)
        rows_count = len(df)
        cols_count = len(df.columns)
        
        # 🌟 خطوة أساسية: تنظيف الـ DataFrame من قيم NaN و inf و -inf وإبدالها بـ None
        df = df.replace({np.nan: None, np.inf: None, -np.inf: None})
        
        # تحويل الجدول إلى قائمة من القواميس (JSON-friendly)
        data_records = df.to_dict(orient="records")
        
        return {
            "status": "success",
            "rows": rows_count,
            "columns": cols_count,
            "data": data_records
        }
        
    except Exception as e:
        # التعامل مع أخطاء الملفات التالفة أو غير الصالحة وإرجاع رسالة خطأ واضحة
        raise ValueError(f"Error processing CSV file: {str(e)}")