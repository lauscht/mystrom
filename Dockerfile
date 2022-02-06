from python:3.9-slim-bullseye

WORKDIR /app
COPY ./requirements /app/

RUN pip install -r requirements.txt

COPY mystrom /app/mystrom

CMD ["python", "-m", "mystrom.prometheus"]