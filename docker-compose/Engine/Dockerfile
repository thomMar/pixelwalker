FROM ubuntu:latest
LABEL maintainer="github.com/thommar"
ENV DEBIAN_FRONTEND noninteractive


# Various dependencies
RUN apt-get update -yqq && apt-get install -yqq \
	build-essential \
	git \
	python3 python3-setuptools python3-dev python3-tk python3-pip npm

# Clone pixelwalker repo
COPY . /pixelwalker
WORKDIR /pixelwalker

# Python dependencies
RUN pip3 install -r requirements.txt

# Bower JS+CSS dependencies
RUN npm install --no-optional --only=production -g bower
RUN bower install --config.interactive=false --allow-root

# Get settings
WORKDIR /pixelwalker/pixelwalker/pixelwalker
COPY ./docker-compose/Engine/settings.py ./
COPY ./docker-compose/Engine/urls.py ./

WORKDIR /pixelwalker/pixelwalker

# Launch service
CMD celery worker -A pixelwalker -l info -Q engine -n engine@%h --detach && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py loaddata AppSettings && \
  	python3 manage.py loaddata TaskTypes && \
    python3 manage.py runserver 0.0.0.0:8000
