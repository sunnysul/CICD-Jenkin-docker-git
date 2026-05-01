#!/bin/bash
echo "Build started"

docker build -t flaskapp .
docker run -d -p 5000:5000 flaskapp