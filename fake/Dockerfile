FROM python:alpine3.19

WORKDIR /app

COPY . .

RUN pip install flask

ENTRYPOINT ["flask", "--app", "api", "run", "--host=0.0.0.0"]

