FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir flask
COPY app.py .
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]
