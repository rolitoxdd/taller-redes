FROM ubuntu:20.04

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt update -y \
&& apt upgrade -y \
&& apt install build-essential -y \
&& apt install -y wget \
clang \
cmake \
pkg-config \
libncursesw5-dev \
libcurl4-gnutls-dev \
zlib1g-dev \
libgcrypt20-dev \
libgnutls28-dev \
gettext \
ca-certificates \
libaspell-dev \
python3-dev \
libperl-dev \
ruby \
ruby-dev \
liblua5.3-dev \
tcl-dev \
guile-2.0-dev \
libv8-dev \
php-dev \
libphp-embed \
libxml2-dev \
libargon2-0-dev \
libsodium-dev \
asciidoctor \
libcpputest-dev \
&& wget https://github.com/weechat/weechat/archive/v3.1.tar.gz \
&& tar -xzf v3.1.tar.gz \
&& cd weechat-3.1 \
&& mkdir build \
&& cd build \
&& cmake .. \
&& make \
&& make install \
&& apt remove -y llvm-10-dev \
libllvm10 \
gcc-9 \
&& apt autoremove -y \
&& rm -rf /weechat-3.1 /v3.1.tar.gz

ENTRYPOINT ["weechat", "-r /set irc.look.temporary_servers on"]
