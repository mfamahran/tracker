FROM python:3.10-slim-buster

WORKDIR /app

COPY ../requirements/base.txt base.txt
RUN pip3 install -r base.txt

COPY . .
ENV FLASK_APP=src/main.py
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]