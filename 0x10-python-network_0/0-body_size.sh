#!/bin/bash
# Extracts the content length of http response
curl -I -s $1 | grep -i ^Content-Length | awk '{print $2}'
