FROM ubuntu:20.04

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt-get update \
&& apt-get upgrade -y \
&& apt-get install -y tar \
golang \
build-essential \
wget \
&& wget https://github.com/oragono/oragono/archive/v2.5.1.tar.gz \
&& tar -xzf v2.5.1.tar.gz \
&& cd /oragono-2.5.1 \
&& mv default.yaml ircd.yaml \ 
&& sed -i 's/^\(\s*\)\"127.0.0.1:6667\":.*$/\1":6667":/' ircd.yaml\
&& sed -i 's/^\s*\"\[::1\]:6667\":.*$//' ircd.yaml\
&& make build\
&& mkdir -p /ircd-bin\
&& cp oragono /ircd-bin\
&& cp -rf languages/ /ircd-bin/languages\
&& cp ircd.yaml /ircd-bin/ircd.yaml \
&& cp oragono.motd /ircd-bin \
&& apt-get remove -y build-essential \
golang \
wget \
&& apt-get autoremove -y \
&& rm -rf /oragono-2.5.1 \
&& rm /v2.5.1.tar.gz

WORKDIR /ircd-bin/

RUN ./oragono mkcerts \
&& ./oragono initdb

EXPOSE 6667

ENTRYPOINT ["./oragono","run"]
