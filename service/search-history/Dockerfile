FROM python:3.6-alpine
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


EXPOSE 5000

COPY . .

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]