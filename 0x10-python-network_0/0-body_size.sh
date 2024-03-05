#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from command line argument
url=$1

# Send a request to the URL and get the size of the response body
response_size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}')

# Display the size of the response body in bytes
echo "$response_size"

