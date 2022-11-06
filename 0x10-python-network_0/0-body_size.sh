#!/bin/bash
# Extracts the content length of http response
echo "$(curl -I -s $1 | grep ^Content-Length | awk -F ": " '{print $2}')"
