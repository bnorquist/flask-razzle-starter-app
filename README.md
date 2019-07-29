# saveclub

### local development instructions
* (in project directory) `docker build . -t saveclub`
* `docker run -d --name 'container_name' 'build_name'`
* `docker exec -it 'container_name' /bin/bash`
* you should now be inside a container with the web process running
* run tests with `pytest tests/`
