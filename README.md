# saveclub

## local development instructions
* docker-compose up
* point browser to `http://lvh.me/`

## Deployment
####Client
* `make deploy.web`
*
####Server
* `make deploy.api`

### TODO
* compare ddbc52fe64a583c210e7c880fc0d5daf0ce572ce sha (api dir) with current master and see why gunicorn isn't binding etc.
* finish deployment of api
* merge test-client-api-linkage branch - set URL ENV variable on frontend
*