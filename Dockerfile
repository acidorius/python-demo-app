FROM python:3 as builder
WORKDIR /python/app
COPY src/ .
RUN pip install flask
CMD [ "python", "./main.py" ]
