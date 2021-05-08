FROM ubuntu:20.04

ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y python-dev
RUN apt-get install -y libnetfilter-queue-dev
RUN apt-get install -y tshark
RUN apt-get install -y tcpdump
RUN apt-get install -y python3-pip
RUN apt-get install -y wireshark
RUN apt-get install -y git
RUN pip3 install git+https://github.com/kti/python-netfilterqueue
RUN git clone https://github.com/shramos/polymorph/
WORKDIR /polymorph
RUN python3 setup.py install
RUN apt-get install -y vim
RUN apt-get install -y iptables
COPY functions/ /usr/local/lib/python3.8/dist-packages/polymorph-2.0.6-py3.8.egg/polymorph/functions/

ENTRYPOINT [ "polymorph" ]
