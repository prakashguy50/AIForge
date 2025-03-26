FROM python:3.9-slim
WORKDIR /app
COPY pipelines/ /app/pipelines
RUN pip install -r /app/pipelines/requirements.txt
CMD ["python", "/app/pipelines/data_ingestion.py"]
