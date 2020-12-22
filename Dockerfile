FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /helloworld
COPY requirements.txt /helloworld/
RUN pip install -r requirements.txt
COPY . /helloworld/