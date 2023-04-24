FROM python:3.9

RUN apt-get update && apt-get install -y dnsutils

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT ["python", "scanner.py"]
