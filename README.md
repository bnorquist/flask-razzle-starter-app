# Microservice Starter Template [![Build Status](https://dev.azure.com/norquistben/norquistben/_apis/build/status/bnorquist.flask-razzle-starter-app?branchName=master)](https://dev.azure.com/norquistben/norquistben/_build/latest?definitionId=3&branchName=master) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a starter template for a simple microservice based application with a web client and API sourced by a SQL database.

The web client is created as a Razzle (SSR React) application and the API is a Flask application hydrated by a Postgres instance.

Development is performed locally with Docker while deployment happens via separate applications on Zeit Now.

## Quickstart

```bash
# 1. Clone this repo
git clone git@github.com:bnorquist/flask-razzle-starter-app.git

# 2. Enter directory
cd flask-razzle-starter-app

# 3. Start up services using Docker and Docker Compose
docker-compose up -d
```

Explore services: client at [lvh.me](http://lvh.me), API at [api.lvh.me](http://api.lvh.me)

## Stack

Web Client

* Typescript
* Razzle (React SSR)
* Express
* Node

API

* Python
* Flask
* Gunicorn

Data

* SQLAlchemy
* Postgres

Infra

* Docker
* Nginx
* Azure Pipelines
* Zeit Now

## Code style

* TSLint
* Prettier
* Black
* Flake8
* MyPy
* Pre-Commit

## Testing

* Pytest
* Jest
* Cypress for integration testing in future

## Deployment

Services instead are deployed as separate applications via [Zeit Now](https://zeit.co)

Before deploying, create a Zeit [account](https://zeit.co/signup) for free.

```bash
# 0. Install the Now CLI
npm install --global now

# 1. Deploy the API service
cd api && now # Copy the resulting url provided by Now

# 2. Update the client API_URL environment variable
touch client/.env

# Edit the .env with the url from the previous step
API_URL = api_deployment_url

# 3. Build and deploy the client service
cd client && npm run build && now
```

### TODO

* Add user models/login
* Create login interface
