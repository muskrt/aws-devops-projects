#Name=muskrt/cpp-crow:templates
# FROM debian:stable-slim
# RUN apt update 
# RUN echo 'deb http://ftp.de.debian.org/debian sid main' >> /etc/apt/sources.list 
# # RUN apt-get --download-only install libboost-dev -y
# Run apt install libmysqlcppconn-dev -y
# RUN  apt install g++ -y
# RUN  apt install cmake -y 
# WORKDIR /APP 
# COPY . . 
# RUN chmod +x install_crow.sh
# RUN ./install_crow.sh
# RUN ls /usr/lib/x86_64-linux-gnu/ | grep libmysql
# RUN g++  --std=c++11  -Wall -I/usr/include/cppconn  -o testapp main.cpp -lpthread -L/usr/lib -lmysqlcppconn
# RUN chmod +x testapp 
# Run apt-get clean
# Run rm -rf /var/lib/apt/lists/*
# cmd   ./testapp 




FROM debian:stable-slim as build 
RUN apt update 
RUN echo 'deb http://ftp.de.debian.org/debian sid main' >> /etc/apt/sources.list 
# RUN apt-get --download-only install libboost-dev -y
Run apt install libmysqlcppconn-dev -y
RUN  apt install g++ -y
RUN  apt install cmake -y 
WORKDIR /APP 
COPY . . 
RUN chmod +x install_crow.sh
RUN ./install_crow.sh
RUN ls /usr/lib/x86_64-linux-gnu/ | grep libmysql
RUN g++  --std=c++11  -Wall -I/usr/include/cppconn  -o testapp main.cpp -lpthread -L/usr/lib -lmysqlcppconn
RUN chmod +x testapp 

FROM debian:stable-slim  
WORKDIR /APP 
COPY --from=build /APP . 
COPY --from=build /usr/include/cppconn /usr/include/cppconn
COPY --from=build /usr/include/c++ /usr/include/c++
COPY --from=build /usr/lib/x86_64-linux-gnu/libmysql* /usr/lib/x86_64-linux-gnu/
COPY --from=build /usr/lib/x86_64-linux-gnu/libmariadb* /usr/lib/x86_64-linux-gnu/

CMD ./testapp 



