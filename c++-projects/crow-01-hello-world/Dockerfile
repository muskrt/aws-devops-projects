FROM debian:stable-slim
RUN apt update 
RUN echo 'deb http://ftp.de.debian.org/debian sid main' >> /etc/apt/sources.list 
# RUN echo 'deb http://ftp.de.debian.org/debian buster main ' >> /etc/apt/sources.list 
# RUN apt-get --download-only install libboost-dev -y
Run apt install libmysqlcppconn-dev -y
# RUN  apt get-install libmysqlcppconn-dev
RUN  apt install g++ -y
RUN  apt install cmake -y 
WORKDIR /APP 
COPY . . 
RUN chmod +x install_crow.sh
RUN ./install_crow.sh
RUN ls /usr/lib/x86_64-linux-gnu/ | grep libmysql
RUN g++ --std=c++11  -Wall -I/usr/include/cppconn  -o testapp main.cpp -lpthread  -lssl -lcrypto  -static -L/usr/lib -lmysqlcppconn-static -L/usr/lib -lmysqlclient 
RUN chmod +x testapp 
Run apt-get clean
Run rm -rf /var/lib/apt/lists/*
cmd   ./testapp 
