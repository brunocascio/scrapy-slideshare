#!/bin/bash

printf "Installing deps: "

(
	apt-get install -y python-dev python-pip \
	&& pip install scrapy

) > /dev/null && echo "OK" || echo "FAIL"
