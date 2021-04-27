FROM ubuntu:20.04 AS builder
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update && apt-get upgrade -y 
RUN  apt-get install -y tar \
    golang \
    build-essential \
    wget 
RUN wget https://github.com/oragono/oragono/archive/v2.5.1.tar.gz 
RUN tar -xzf v2.5.1.tar.gz 
WORKDIR /oragono-2.5.1 
RUN mv default.yaml ircd.yaml 
RUN sed -i 's/^\(\s*\)\"127.0.0.1:6667\":.*$/\1":6667":/' ircd.yaml
RUN sed -i 's/^\s*\"\[::1\]:6667\":.*$//' ircd.yaml
RUN make build
RUN mkdir -p /ircd-bin
RUN cp oragono /ircd-bin
RUN cp -rf languages/ /ircd-bin/languages
RUN cp ircd.yaml /ircd-bin/ircd.yaml 
RUN cp oragono.motd /ircd-bin 

FROM ubuntu:20.04
COPY --from=builder /ircd-bin/ /ircd-bin/
WORKDIR /ircd-bin/
RUN ./oragono mkcerts 
RUN ./oragono initdb
EXPOSE 6667
ENTRYPOINT ["./oragono","run"]

