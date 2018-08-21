[![Build Status](https://travis-ci.org/antoinehng/pixelwalker.svg?branch=django_2.0)](https://travis-ci.org/antoinehng/pixelwalker 'Travis CI') [![Coverage Status](https://coveralls.io/repos/github/antoinehng/pixelwalker/badge.svg?branch=django_2.0)](https://coveralls.io/github/antoinehng/pixelwalker?branch=django_2.0 'Coveralls')

__Warning:__ _This project is about to be ready for production purposes._

![Screenshot](screenoshot_pixelwalker.png)

## How to try?

Using [docker-compose](https://docs.docker.com/compose/install/)

```
# GETTING THE SOURCE
# Clone the repo and make it your active directory
git clone https://github.com/antoinehng/pixelwalker ./pixelwalker
cd ./pixelwalker

# CREATE A MEDIA LIBRARY FOLDER ON YOUR HOST
# Default location is {{ repo-root }}/media_library/
# If you need to change this, go to docker-compose/docker-compose.yml 
# and change the volumes parameters for the engine and worker services
mkdir media_library

# USE DOCKER-COMPOSE
# Move to the docker-compose directory
cd docker-compose

# Build all needed docker images
docker-compose build

# Start all services
docker-compose up
```

The plateform should be accessible at http://localhost:8000

