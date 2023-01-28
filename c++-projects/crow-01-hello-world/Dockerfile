FROM debian:stable-slim
RUN apt update 
RUN echo 'deb http://ftp.de.debian.org/debian sid main' >> /etc/apt/sources.list
RUN apt install libboost-dev -y
Run apt install libmysqlcppconn7v5 -y
# RUN  apt get-install libmysqlcppconn-dev
RUN  apt install g++ -y
WORKDIR /APP 
COPY . . 
cmd sudo g++ --std=c++11 -Wall -I/usr/include/cppconn -o testapp main.cpp -lpthread -L/usr/lib -lmysqlcppconn
