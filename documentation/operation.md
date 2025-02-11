# About
Instructions for a day to day operation. For Day 1 and subsequent.

# Normal day
## Docker, up
### Verify Docker is running
```shell
sudo service docker status
# or
docker run hello-world
```

### Start Docker
```shell
sudo service docker start
# and verify again
sudo service docker status
```

### Verify the Docker images are available
```shell
docker images
```
Should display the Arista images (`arista/ceos:4.29.3M`), the containerlabs (`ghcr.io/srl-labs/clab`), and AVD (`avd-quickstart:latest`) images.

## Containerlab, up
### Go to the containerlabs directory

```shell
cd <containerlabs_directory>
```

### Start containerlab
This is done by creating a Docker container from the containerlab image (`ghcr.io/srl-labs/clab`), or `avd-quickstart`

With the containerlab image
```shell
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
(it will end up with the shell `ash` because the container is an Alpine image and Alpine does not have the shell `bash`).

With the AVD quickstart image
```shell
docker run --rm -it --privileged \
    --name container_avd \
    --network host \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /etc/hosts:/etc/hosts \
    --pid="host" \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    -e AVD_GIT_USER="Daniel Lete" \
    -e AVD_GIT_EMAIL="daniel.lete@gmail.com" \
    avd-quickstart:latest || true ; \
```
You will see that the prompt has changed. 

### Verify containerlab is running
Either by:
* Observing that the prompt has changed. 
* `docker ps` does render a running container with the name tag you gave it at the moment of creating it. 

### Deploy/launch a lab
From within the containerlab docker:

```shell
sudo containerlab deploy --topo <path_to_topology_file>
sudo containerlab deploy --topo <./<lab>/clab/topology.yml>
```
Topology files have the extension `*.yml` and should be within the directory `clab`. Usually have the filename `topology.yml`.
Remember, you have to execute as `sudo`
It will not bring the lab immediately. It may take about 1 minute (or more, depending on the number of containers).


## Operate nodes
### Connect to the nodes

#### By attaching to the docker image
From any terminal (does not have to the docker container). For example: you could have one terminal for each node.
```shell
# The following command will put you in the EOS CLI. 
# Note that the keyword is "Cli", not "cli"
docker exec -it <container_name> Cli
# or
docker exec -it <container_name> bash
# The above will put you in shell shell. To enter EOS CLI, execute:
# /usr/bin/FastCli
```

## Operate nodes, with ansible

## Operate nodes, with AVD


## Containerlab, down
### Destroy a lab
Go to, execute in, the Docker container that has the containerlab image. For the same lab that you had created

```shell
# Verify the node containers are running
docker ps
# Destroy the lab
sudo containerlab destroy --topo <path_to_topology_file>
# Verify the node containers have stopped
docker ps
```
You should still see the containerlab container running.

### Remove the containerlab container
By exiting. The container and its associated anonymous volumes  will be automatically removed because the container was created with the option `docker run --rm`.

```shell
# Verify the containerlab container has stopped and been removed
docker ps
docker ps -a
```


## Docker, down
### Verify Docker is running
```shell
sudo service docker status
# or
docker run hello-world
```

### Stop Docker
```shell
sudo service docker start
```
and verify again




# Create a lab
* Create folder for lab under `containerlabs`. This is the <lab_root>
* Create folder `clab`
* Create topology file
* Create `init-configs` folder
* Create initial configuration 

* Change to the lab directory
* Start a docker container with containerlabs installed on it
```shell
docker run --rm -it --privileged \
    --name container_avd \
    --network host \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /etc/hosts:/etc/hosts \
    --pid="host" \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    -e AVD_GIT_USER="Daniel Lete" \
    -e AVD_GIT_EMAIL="daniel.lete@heanet.ie" \
    avd-quickstart:latest || true ; \
```
* Deploy the lab with containerlabs
  * Verify the containers have come up
  * Verify the containers have the correct name
  * Ping the containers (the container `avd-quickstart:latest` does not have `ping`)
  * Verify the containers have the correct initial configuration. Verify `management api` is running/open (if ping works, there is no need really for this step, you can assume the initial configuration has been applied correctly)

  * Destroy the lab with containerlabs
  * Comment the line `startup-config: init-configs/ceos-cfg.j2` in `hosts.yml`
  * Deploy the lab with containerlab. Now you have the initial config saved to startup, and hence connectivity


* create `ansible.cfg in` <lab_root>
* create inventory directory
* create host files
* (create group vars)
* create playbooks directory
* Verify that ansible can communicate with the nodes (authentication, ports open, etc. and network/IP communication). This playbook `ansible-playbook -i inventory playbooks/ping.yml` will determine both.


# Known issues
### Arista connection with Ansible
Need to have this in the Arista device configuration
```
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
!
```

Need to have this in the `hosts.yml` file.

```yml
FABRIC:
  vars:
    ansible_user: robot
    ansible_password: aladdin
    # The no checking of host keys is already set in ansible.cfg
    #ansible_ssh_common_args: '-o StrictHostKeyChecking=no'
    ansible_connection: httpapi
    ansible_network_os: eos
    ansible_become: yes
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_ciphers: AES256-SHA:DHE-RSA-AES256-SHA:AES128-SHA:DHE-RSA-AES128-SHA
```

### Containerlabs, shell is `ash` instead of `bash`
Usually, an Alpine Linux image doesn't contain `bash`, Instead you can use `/bin/ash`, `/bin/sh`, `ash` or only `sh`.

Found in [stackoverflow]{https://stackoverflow.com/questions/35689628/starting-a-shell-in-the-docker-alpine-container}

### Start the `dockerd` daemon
Starting the daemon directly does not seem to work (at least in an Ubuntu instance in WLS). I have found that what it works is this sequence. 
1. Stop the `dockerd` daemon
```shell
sudo start-stop-daemon -K -v --name dockerd
```

2. Start the `dockerd` daemon
```shell
sudo dockerd > /dev/null 2>&1 & disown
```

3. Verify the `dockerd` daemon has started
```shell
docker run hello-world
```


# Troubleshooting
fatal: [clab-dl_02-leaf1]: FAILED! => {"changed": false, "msg": "Method not found"}
fatal: [clab-dl_02-spine1]: FAILED! => {"changed": false, "msg": "Method not found"}
Means that it can't find the collection