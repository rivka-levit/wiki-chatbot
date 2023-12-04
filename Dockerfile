FROM python:3.12.0

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./nltk_data /usr/local/nltk_data
COPY ./app /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser --disabled-password --no-create-home chat-user

USER chat-user
