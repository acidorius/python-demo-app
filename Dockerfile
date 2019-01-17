FROM python:3 as builder
WORKDIR /python/app
COPY src/ .
RUN pip install flask
RUN pip install gunicorn
CMD ["gunicorn", "-w -b 0.0.0.0:5000 main:app" ]
