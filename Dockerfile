# استخدام صورة بايثون الرسمية الخفيفة
FROM python:3.10-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# تثبيت الاعتماديات النظامية الضرورية
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# نسخ ملفات الاعتماديات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع إلى الحاوية
COPY . .

# فتح المنفذ الذي يعمل عليه الخادم
EXPOSE 8000

# أمر تشغيل التطبيق عبر Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]