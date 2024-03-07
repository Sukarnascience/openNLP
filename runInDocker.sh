#!/bin/bash

# Build the Docker image
docker build -t open_nlp .

# Run the Docker container
docker run -it open_nlp
