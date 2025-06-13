FROM python:3.9-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 7001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7001"]
