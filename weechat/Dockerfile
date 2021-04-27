FROM ubuntu:20.04 AS builder
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update -y && apt-get upgrade -y 
RUN apt-get install -y build-essential  
RUN apt-get install -y wget 
RUN apt-get install -y clang 
RUN apt-get install -y cmake 
RUN apt-get install -y pkg-config 
RUN apt-get install -y libncursesw5-dev 
RUN apt-get install -y libcurl4-gnutls-dev 
RUN apt-get install -y zlib1g-dev 
RUN apt-get install -y libgcrypt20-dev 
RUN apt-get install -y libgnutls28-dev 
RUN apt-get install -y gettext 
RUN apt-get install -y ca-certificates
RUN apt-get install -y libv8-dev 
RUN apt-get install -y libxml2-dev 
RUN apt-get install -y libargon2-0-dev 
RUN apt-get install -y libsodium-dev 
RUN apt-get install -y libcpputest-dev 
RUN wget https://github.com/weechat/weechat/archive/v3.1.tar.gz
RUN tar -xzf v3.1.tar.gz 
RUN mkdir /weechat-3.1/build 
WORKDIR /weechat-3.1/build 
RUN cmake .. \
    -DENABLE_PYTHON=OFF \
    -DENABLE_SPELL=OFF \
    -DENABLE_TCL=OFF \
    -DENABLE_PHP=OFF \
    -DENABLE_PERL=OFF \
    -DENABLE_RUBY=OFF \
    -DENABLE_GUILE=OFF \
    -DENABLE_LUA=OFF
RUN make 
RUN make install 

FROM ubuntu:20.04
COPY --from=builder /usr/local/lib/weechat /usr/local/lib/weechat
COPY --from=builder /usr/local/bin/weechat /usr/local/bin/weechat
RUN apt update -y && apt upgrade -y
RUN apt install -y libcurl4-gnutls-dev 
ENTRYPOINT ["weechat", "-r /set irc.look.temporary_servers on"]

