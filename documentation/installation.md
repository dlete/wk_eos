# About this file
Installation instructions to run Arista cEOS labs:
* In a WSL instance
* Ubuntu as the OS
* Docker installed from the Docker apt repository (not from the Ubuntu repository) 
* Ansible installed as Docker image over in an `alpine` image.
* containerlab installed as a Docker image.
* Arista EOS with the cEOS images.
* Arista containers running in containerlab.

# Requisites
* A Windows or Linux operating system to serve as the host server for Docker.

# Install
## Install WSL, ubuntu

## Base directory
Create a base directory or clone the Git repository.

### Clone this repository
When you clone a Git repository it will be placed in a directory named as the repository itself in the directory you are it. Hence, place yourself where you want this new repository to be cloned to and
```bash
git clone <url_of_repository>
```

### Create base directory
In your local computer, create a directory. This will be the root of the project.
```bash
mkdir ./<directory_name>
```
from now on we will refer to `<directory_name>` as `<base>`

Change directory to the newly created directory
```bash
mkdir cd ./<base>
```

## Install Docker Engine
<https://docs.docker.com/engine/install/ubuntu/>
Install from Docker apt
`docker-ce` is needed because it is a requirement of containerlab

verify
```bash
sudo service docker start
sudo docker run hello-world
```

## Ansible image
Build with `Dockerfile`. You will find it in the `dockerfiles` directory.

```bash
docker build --tag <image_name:tag> --file <path_to_dockerfile_file> <PATH>
docker build --tag first-dockerfile --file Dockerfile1 .
docker build --tag dlete_ansible:3.16 --file Dockerfile1 .
```
Reference: [docker build](https://docs.docker.com/engine/reference/commandline/build/)

## Arista images, get them
Download cEOS from Arista.
Download also too the README file
Transfer to the Linux instance.

## Import the Arista image
Convention for naming the Arista cEOS images: `arista/ceos:<version_number>`.
```bash
# import the downloaded cEOS-lab.tar.xz image
docker import cEOS-lab.tar.xz arista/ceos:4.29.3M
```

## install containerlab
<https://containerlab.dev/install/>
BUT do so as a container
<https://containerlab.dev/install/#container>

Launch containerlab
```bash
docker run --rm -it --privileged \
    --name container_containerlab \
    --network host \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /var/run/netns:/var/run/netns \
    -v /etc/hosts:/etc/hosts \
    -v /var/lib/docker/containers:/var/lib/docker/containers \
    --pid="host" \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    ghcr.io/srl-labs/clab bash
```

```bash
docker run --rm -it --privileged \
    --network host \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /var/run/netns:/var/run/netns \
    -v /etc/hosts:/etc/hosts \
    -v /var/lib/docker/containers:/var/lib/docker/containers \
    --pid="host" \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    ghcr.io/srl-labs/clab bash
```


# Uninstall
## Backup containerlab topology files
## Delete all the containers
## Delete the containerlab image
## Delete the Ansible image
## Delete the Arista images
## Uninstall Docker Engine
<https://docs.docker.com/engine/install/ubuntu/>

## Remove Docker

## Delete the base directory
Arista AVD collection installation
```bash
sudo rm -r ./<directory_name>
```
