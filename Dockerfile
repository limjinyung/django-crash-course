FROM python:3.6
ENV PYTHONBUFFERED=1
WORKDIR /helloworld
COPY requirements.txt /helloworld/
RUN pip install -r requirements.txt
COPY . /helloworld/

VOLUME /helloworld
CMD ["python", "manage.py", "test", "--noinput"]