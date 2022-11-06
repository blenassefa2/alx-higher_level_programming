#!/bin/bash
# Extracts the content length of http response
curl -s "$1" | wc -c
