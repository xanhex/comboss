FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -U pip &&\
    pip install -r requirements.txt --no-cache-dir &&\
    python3 create_db.py

CMD ["gunicorn", "app:create_app()", "--bind", "0:8000", "--reload"]
# CMD ["flask", "run", "--debug", "--host", "0.0.0.0", "--port", "8000"]
