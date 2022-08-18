#!/bin/bash
# Sends a request to that URL
curl -w '%{size_download}\n' --silent --output /dev/null "$1"
