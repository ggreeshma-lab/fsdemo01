From python:3.10.10-slim
WORKDIR /app
COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt
COPY app.py .
CMD ["python","app.py"]