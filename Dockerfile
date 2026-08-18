FROM python:3.12-slim
WORKDIR /challenge
COPY _shared /challenge/_shared
COPY entrypoint.py /challenge/entrypoint.py
ENTRYPOINT ["python", "/challenge/entrypoint.py"]
