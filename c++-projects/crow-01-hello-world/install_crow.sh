#!/bin/bash
apt install -y libasio-dev
# git clone https://github.com/CrowCpp/Crow.git
cd Crow
mkdir build
cd build
cmake .. -DCROW_BUILD_EXAMPLES=OFF -DCROW_BUILD_TESTS=OFF
make install