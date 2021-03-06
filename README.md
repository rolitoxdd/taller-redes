En el presente repositorio se presenta el trabajo de captura y análisis de trafico IRC entre el servidor Oragono y el cliente Weechat, para lo cual se utilizó el programa Wireshark.

Del tráfico capturado se realizó un estudio y análisis de cada mensaje captado entre la interacción servidor-cliente.

Se presentan dos carpetas, las cuales contienen los dockerfiles de los softwares estudiados. Ademas, se adjunta un documento de docker compose que automatiza la ejecucion de los servicios junto a la creación de una red privada.

- Disclaimer n°1: Es importante mencionar que en este trabajo se utilizó docker-compose con la finalidad de facilitar el montaje servidor-cliente.

Pasos a seguir:

1. Primero clonamos el repositorio:

```sh
$ git clone https://gitlab.com/eit-udp/taller-redes/2021-1/grupo_777
```

2. Lenvantar red, servidor y cliente:

```sh
$ docker-compose run client
```

Una vez realizados los pasos anteriores se inicia automaticamente el cliente de Weechat y para iniciar correctamente la conexion con oragono se debe continuar con el siguiente comando:

```sh
/connect server
```

Para cambiar o seleccionar un nick distinto de root utilizamos:

```sh
/nick <nick-a-usar>
```

A partir de este punto podemos utilizar nuestro cliente de Weechat conectado al servidor de Oragono y empezar el analisis y captura de trafico en Wireshark seleccionando la red asociada al red privada generada.

Video de la captura de tráfico:

[![Protocolo IRC](http://img.youtube.com/vi/8dNjg6tq-zI/0.jpg)](http://www.youtube.com/watch?v=8dNjg6tq-zI "Protocolo IRC")

- Disclaimer n°2: Las imagenes buildeadas con los dockerfiles tambien pueden ser descargadas usando los comandos:

```sh
$ docker pull rolitoxdd/weechat
$ docker pull rolitoxdd/oragono
```

---

En esta nueva entrega se trabaja con el programa Polymorph, el cual se encarga de captar y modificar paquetes a tiempo real. Para su implementacion y uso se realizó una imagen de docker (Dockerfile contenido en los archivos).

Pasos a seguir para inicializar Polymorph:

1. Posterior a los pasos anteriormente descritos debera buildear o descargar la imagen de Polymorph creada:

Buildear:

```sh
grupo_777/polymorph $ docker build -t rolitoxdd/polymorph .
```

Descargar:

```sh
$ docker pull rolitoxdd/polymorph
```

2. Para correr Polymorph se debe ejecutar el siguiente comando:

```sh
$ docker run -it --privileged --net grupo_777_default rolitoxdd/polymorph
```

Nota importante: Para poder elegir correctamente las IPs de target y gateway al momento de realizar el spoof dentro de polymorph es importante inspeccionar la red y de esta extraer las IPs con el comando:

```sh
$ docker network inspect grupo_777_default
```

Video demostración Polymorph:

[![IRC - Intercepción y Modificación de paquetes /w Polymorph - 777](http://img.youtube.com/vi/5sbMDurwiEA/0.jpg)](http://www.youtube.com/watch?v=5sbMDurwiEA "IRC - Intercepción y Modificación de paquetes /w Polymorph - 777")

---

Video de modificación de métricas de red:

[![Métricas de Red](https://img.youtube.com/vi/CpIbepU4xv4/0.jpg)](https://www.youtube.com/watch?v=CpIbepU4xv4 "Métricas de Red")
