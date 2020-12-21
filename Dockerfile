FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /helloworld
COPY requirements.txt /helloworld/
RUN pip install -r requirements.txt
COPY . /helloworld/
EXPOSE 8000
CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "helloworld.wsgi"]