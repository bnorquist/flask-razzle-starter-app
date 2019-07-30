FROM python:3.7.2

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        build-essential \
        gettext \
        libffi-dev \
        libgdal-dev \
        libssl-dev \
        && pip install --upgrade pip setuptools wheel

COPY . .

RUN pip install -r requirements.txt

# RUN ls -al

ENTRYPOINT ["gunicorn", "app:app"]
