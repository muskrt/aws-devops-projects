#!/bin/bash
docker image build -t muskrt/LOGINAPP:1.0 
docker container run --rm --name myapp -dit --network host muskrt/LOGINAPP:1.0
