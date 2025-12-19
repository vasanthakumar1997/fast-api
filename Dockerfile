FROM python:3.11-slim

WORKDIR /firstapp

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "firstapp.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
