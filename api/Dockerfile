FROM python:3.7.2

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential \
    && pip install -U pip setuptools wheel

COPY . .

RUN pip install -r requirements.txt

RUN pre-commit run --all-files --show-diff-on-failure

RUN pytest api/tests --doctest-modules --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8000", "app:app"]