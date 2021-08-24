FROM python:3.8.0-slim-buster

WORKDIR /webapp

RUN pip install --upgrade pip
COPY ./requirements.txt /webapp/requirements.txt

RUN pip install -r requirements.txt

COPY . /webapp

ENTRYPOINT ["uvicorn", "app_python.api.server:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000"]