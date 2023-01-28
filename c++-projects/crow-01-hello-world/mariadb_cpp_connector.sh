FROM debian:stable-slim
RUN wget https://dlm.mariadb.com/2531493/Connectors/cpp/connector-cpp-1.0.2/mariadb-connector-cpp-1.0.2-debian-buster-amd64.tar.gz
RUN tar -xvzf mariadb-connector-cpp-*.tar.gz
RUN cd mariadb-connector-cpp-*/
RUN sudo install -d /usr/include/mariadb/conncpp
RUN sudo install -d /usr/include/mariadb/conncpp/compat
RUN sudo install include/mariadb/* /usr/include/mariadb/ && sudo install include/mariadb/conncpp/* /usr/include/mariadb/conncpp && sudo install include/mariadb/conncpp/compat/* /usr/include/mariadb/conncpp/compat
RUN sudo install -d /usr/lib/mariadb && sudo install -d /usr/lib/mariadb/plugin
RUN sudo install lib/mariadb/libmariadbcpp.so /usr/lib && sudo install lib/mariadb/plugin/* /usr/lib/mariadb/plugin
