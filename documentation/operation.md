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
## Start the `dockerd` daemon
Starting the daemon directly does not seem to work (at least in an Ubuntu instance in WLS). I have found that what it works is this sequence. 
1. Stop the `dockerd` daemon
```bash
sudo start-stop-daemon -K -v --name dockerd
```

2. Start the `dockerd` daemon
```bash
sudo dockerd > /dev/null 2>&1 & disown
```

3. Verify the `dockerd` daemon has started
```bash
docker run hello-world
```


## Start the container
```bash
# map the host directory "$(pwd)/host_directory" (in your PC), to the directory "ansible" in the image"
docker run --rm -it -v $(pwd)/host_directory:/ansible_root dl_dockerfile_02 bash
docker run --rm -it -v $(pwd)/host_directory:/ansible_root dl_image_02 bash
```

This is the canonical way, through `dockercompose.yml` files:
```bash
docker-compose up -d
```


## Docker, connect to a running container
```bash
# for a server
docker exec -it <container_name> bash
# for an Arista
docker exec -it <container_name> Cli
docker exec -it ceos1 Cli
```

## Docker, restart containers
```bash
# restart container without loss configuration
docker-compose stop
```

## Docker, wipe out everything
```bash
# wipe out everything
docker-compose down
```

## Execute ansible commands
```bash
docker exec ceos_basic_01_my_ans_1 ansible localhost -m ping -i ansible_root/inventory.txt
```

## Execut ansible playbook
```bash
docker exec ceos_basic_01_my_ans_1 ansible-playbook <playbook_filename>
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

## Ansible, get information/documentation
```bash
docker exec ceos_basic_01_my_ans_1 ansible-doc -l
```

## Ansible, get help 
```bash
docker exec ceos_basic_01_my_ans_1 ansible-playbook --help
```

## Ansible, execute a one-off command
```bash
ansible <hosts> -a <command>
ansible <hosts> -m <module>
ansible target1 -m ping
```

## Ansible, execute a playbook
```bash
ansible-playbook <playbook_name>
ansible-playbook playbook_server.yaml
ansible-playbook <playbook_name> -i <inventory_file>
```

## Arista EOS, change from `bash` to `cli`
If you have arrived to `bash` from the `cli`, then just type `exit`.
If you have arrived to `bash` direclty, then `Cli` (the first letter is capital).

## Arista, enable LLDP in Docker

<https://youtu.be/RgbWDw__xqM?t=277>

## WSL stop server
Open PowerShell as an administrator
```bash
# see distributions and their status
wsl -l -v
# stop
wsl -t Ubuntu
# start
wsl -d Ubuntu
# Verify the distribution has started
wsl -l -v
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

## WSL stop server
Open PowerShell as an administrator
```bash
# see distributions and their status
wsl -l -v
# stop
wsl -t Ubuntu
# start
wsl -d Ubuntu
# Verify the distribution has started
wsl -l -v
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