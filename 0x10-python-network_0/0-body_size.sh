#!/bin/bash


var="$(curl -I -s $1 | grep ^Content-Length: | cut -d: -f2- | sed 's/^ *\(.*\).*/\1/')"
echo "$var"
