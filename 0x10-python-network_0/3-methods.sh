#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -s -X OPTIONS -I $1 -L | grep -i Allow | cut -d " " -f2-
