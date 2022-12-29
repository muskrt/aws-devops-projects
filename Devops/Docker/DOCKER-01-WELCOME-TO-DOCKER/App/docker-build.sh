#!/bin/bash
docker image build -t muskrt/welcomeapp:1.0 .
docker container run --rm -dit --network host --name myapp muskrt/welcomeapp:1.0