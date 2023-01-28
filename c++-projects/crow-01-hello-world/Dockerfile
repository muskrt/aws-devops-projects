FROM debian:stable-slim
RUN apt update 
RUN echo 'deb http://ftp.de.debian.org/debian sid main' >> /etc/apt/sources.list
RUN apt install libboost-dev -y
Run apt install libmysqlcppconn-dev -y
RUN apt install git -y 
# RUN  apt get-install libmysqlcppconn-dev
RUN  apt install g++ -y
RUN  apt install cmake -y 
WORKDIR /APP 
COPY . . 
RUN chmod +x install_crow.sh
RUN ./install_crow.sh
cmd  g++ --std=c++11 -Wall -I/usr/include/cppconn -o testapp main.cpp -lpthread -L/usr/lib -lmysqlcppconn
