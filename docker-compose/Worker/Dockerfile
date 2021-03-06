FROM ubuntu:latest
LABEL maintainer="github.com/thomMar"
ENV DEBIAN_FRONTEND noninteractive


# Various dependencies
RUN apt-get update -yqq && apt-get install -yqq \
	build-essential software-properties-common \
	git \
	python3 python3-setuptools python3-dev python3-tk python3-pip npm --no-install-recommends apt-utils

# Clone pixelwalker repo
COPY . /pixelwalker
WORKDIR /pixelwalker

# Python dependencies
RUN pip3 install -r requirements.txt

# Install FFmpeg dependencies
RUN apt-get install -yq ffmpeg

# Get settings
WORKDIR /pixelwalker/pixelwalker/pixelwalker
COPY ./docker-compose/Worker/settings.py ./
COPY ./docker-compose/Worker/urls.py ./

# Launch service
WORKDIR /pixelwalker/pixelwalker
CMD celery worker -A pixelwalker -l info -Q worker -n worker@%h
