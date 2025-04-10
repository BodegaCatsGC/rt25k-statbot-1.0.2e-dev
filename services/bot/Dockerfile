FROM python:3.10-slim

WORKDIR /app

ENV PYTHONPATH="${PYTHONPATH}:/app"

COPY services/bot/ /app/bot/
COPY requirements.txt .

RUN apt-get update && apt-get install -y tesseract-ocr
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot/main.py"]
