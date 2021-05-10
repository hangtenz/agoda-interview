FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY internal ./internal

CMD ["python","internal/endpoint.py"]

EXPOSE 5000

