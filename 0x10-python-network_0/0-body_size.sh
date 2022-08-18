#!/bin/bash
# Sends a request to that URL
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
