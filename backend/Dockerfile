# Description: Dockerfile for the backend service
# Author: Angel
# *** Multi-stage build ***

FROM python:3.12

RUN apt-get update && apt-get install -y cron \
    && apt-get clean nano \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN echo "* * * * * echo 'Hello from the cron' >> /var/log/cron.log 2>&1" > /etc/cron.d/hello-cron

EXPOSE 8000

CMD ["python", "app.py"]