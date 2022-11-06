#!/bin/bash
# Extracts the content length of http response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
