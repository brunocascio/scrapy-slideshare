#!/bin/bash

printf "Installing deps: "

(
	sudo apt-get install -y python-dev python-pip \
	&& sudo pip install scrapy

) > /dev/null && echo "OK" || echo "FAIL"
