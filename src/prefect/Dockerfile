FROM python:alpine3.19

WORKDIR /app

COPY ./requirements.txt .

COPY ./src ./src

RUN pip install -r requirements.txt

ENTRYPOINT ["python","-m","src.prefect"]

