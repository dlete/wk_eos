# Questions

## Why can't set specific version of ansible in Dockerfile?
A. Because you were using the parameter `ENV` incorrectly. You were using `ENV VERSION 15.1` and should have been writing `ENV VERSION=15.1`. You were missing the `=` symbol.

Q. Why have images with no names? and why can't be deleted saying they have child images?

## What is servicenow?


# Reference sites, articles, etc.
## Courses
### UDEMY, Docker for the Absolute Beginner - Hands On - DevOps
<https://heanet.udemy.com/course/learn-docker/>

## Articles
### Dzone
<https://dzone.com/articles/ci-dockerizing-an-ansible-playbook-and-deploying-t>

### Microsoft
<https://learn.microsoft.com/en-us/azure/developer/ansible/configure-in-docker-container?tabs=azure-cli>

### Arista, cEOS-lab in GNS3
<https://arista.my.site.com/AristaCommunity/s/article/ceos-lab-in-gns3>

### Arista, Network CI/CD Part 1 - Building network topologies with Docker and cEOS-lab
<https://arista.my.site.com/AristaCommunity/s/article/ceos-lab-topo>

### Arista, AVD
<https://avd.sh/en/stable/docs/installation/collection-installation.html>

### Arista, implementation of Setup Ansible AVD With VS Code Container
<https://avd.sh/en/stable/docs/how-to/vscode-container.html>

### Containerlab, quick start
<https://containerlab.dev/quickstart/>

### How to use Arista cEOS to build a topology to test features
<https://kevin-wang-xin.medium.com/how-to-use-arista-ceos-to-build-a-topology-to-test-features-49d316110b98>

### Containerlab with cEOS
<https://containerlab.dev/manual/kinds/ceos/>

### How to setup Arista cEOS Docker Image
<https://www.youtube.com/watch?v=ngS80TzrSAw>


# How to
## Docker daemon, start
sudo service docker start

## Docker daemon, verify 
sudo service docker status
or
docker run hello-world

## Docker daemon, stop
sudo service docker stop


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

## Git, change repository
Add files using the command line or push an existing Git repository with the following command:
```bash
cd existing_repo
git remote add origin https://git.heanet.ie/dlete/wk_sand.git
git branch -M main
git push -uf origin main
```

## Git, setup repository
Git global setup
```bash
git config --global user.name "Daniel Lete"
git config --global user.email "daniel.lete@heanet.ie"
```

Create a new repository
```bash
git clone git@git.heanet.ie:dlete/wk_eos.git
cd wk_eos
git switch -c main
touch README.md
git add README.md
git commit -m "add README"
git push -u origin main
```

Push an existing folder
```bash
cd existing_folder
git init --initial-branch=main
git remote add origin git@git.heanet.ie:dlete/wk_eos.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

Push an existing Git repository
```bash
cd existing_repo
git remote rename origin old-origin
git remote add origin git@git.heanet.ie:dlete/wk_eos.git
git push -u origin --all
git push -u origin --tags
```

## WSL stop server
Open PowerShell as an administrator
```bash
# see distributions and their status
wsl -l -v
# stop all distributions
wsl --shutdown
# terminate a specific distribution
wsl -t Ubuntu
# start
wsl -d Ubuntu
# Verify the distribution has started
wsl -l -v
```
<https://superuser.com/questions/1126721/rebooting-ubuntu-on-windows-without-rebooting-windows>
