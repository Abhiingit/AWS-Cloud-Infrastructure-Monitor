FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY monitor ./monitor

ENV PYTHONUNBUFFERED=1
ENV AWS_REGION=ap-south-1

CMD ["python", "-m", "monitor.main"]
