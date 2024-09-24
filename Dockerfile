FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8089

ENV LOCUST_FILE locustfile.py

CMD ["locust", "-f", "locustfile.py"]