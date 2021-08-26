# Cloud Native Workshop
## Table of contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Basic commands](#basic-commands)
4. [How to build your first container](#how-to-build-your-first-container)
5. [Multi-container Docker applications](#multi-container-docker-applications)

## Introduction

Welcome to the first Cloud Native Workshop labs!  
You will learn the basic docker commands, how to prepare, build and run your first container and how to use docker-compose to run a group of containers.

## Installation  

Depending on what system you use, the docker installation may be different, the easiest way is to always follow the instructions provided in the Docker documentation:
- [Windows](https://docs.docker.com/desktop/windows/install/)
- [Mac](https://docs.docker.com/desktop/mac/install/)
- GNU/Linux:
    - [Debian](https://docs.docker.com/engine/install/ubuntu/)
    - [Ubuntu](https://docs.docker.com/engine/install/debian/)
    - [Centos](https://docs.docker.com/engine/install/centos/)
    - [Fedora](https://docs.docker.com/engine/install/fedora/)

If you have a GNU/Linux system, you can also consider performing additional optional configuration thanks to which, among other things, you will be able to execute commands without the need to elevate privileges ▶ [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)

After installing and launching the Docker application, let's run our first command to check the Docker version:
```
$ docker --version
```

## Basic commands
You are probably wondering what are the basic commands you will use every day, here is a short cheat-sheet where you will find the most frequently used commands and their descriptions:

```
$ docker ps
```

```
$ docker images
```

```
$ docker pull <container>
```

```
$ docker run <container>
```


```
$ docker exec
```

```
$ docker stop / $ docker kill
```


## How to build your first container?

## Multi-container Docker applications