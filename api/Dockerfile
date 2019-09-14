FROM python:3.7.2

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential \
    && pip install -U pip setuptools wheel

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn app:app -b 0.0.0.0:${PORT}
