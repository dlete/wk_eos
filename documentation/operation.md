# About this file
Operation instructions for the repository.

# Docker daemon
## Start
Start the docker daemon
```bash
# https://askubuntu.com/questions/1375195/run-dockerd-as-a-background-on-wsl-ubuntu
sudo dockerd > /dev/null 2>&1 & disown
```

## Verify
Verify 
```bash 
ps aux | grep dockerd
```

```bash 
docker run hello-world
```

## Stop
Stop the docker daemon
```bash
sudo start-stop-daemon -K -v --name dockerd
```

# Daily routine
1. Start the `dockerd` daemon
2. Stop the `dockerd` daemon
####// build the image
#docker build -t first-dockerfile -f Dockerfile1 .

Start the container
# map the host directory "$(pwd)/host_directory" (in your PC), to the directory "ansible" in the image"
```bash
docker run --rm -it -v $(pwd)/host_directory:/ansible dl_dockerfile_01 bash
```



# How to
## Docker, see images
```bash
docker images
```

## Docker, remove images
<https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes>

Docker provides a single command that will clean up any resources — images, containers, volumes, and networks — that are dangling (not tagged or associated with a container):
```bash
docker system prune
```

To additionally remove any stopped containers and all unused images (not just dangling images), add the -a flag to the command:
```bash
docker system prune -a
```

```bash
docker rmi <image> <image>
```


## Docker, see containers
```bash
docker ps
docker container ls
docker container ls -a
```

## Docker, see cpu/memory consumption
```bash
docker stats
```

## Docker, start container
```bash
docker pw
```

## Docker, stop container
```bash
docker stop <container__id/name?>
```

## Docker, connect to an Arista running image
```bash
docker exec -it ceos1 Cli
```


# Archive
## Conda environments

### Activate the conda base environment automatically

```bash
# activate every time a terminal is opened
conda config --set auto_activate_base true
# do not activate every time a terminal is opened
conda config --set auto_activate_base false
```

### See all the conda environments
```bash
conda info envs
```

## Conda packages
### Add
```bash
conda install <package_name>
```
### List
```bash
conda list
```

### Remove
```bash
conda remove <package_name>
```