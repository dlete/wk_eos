# LIst of things to do
Start containerlabs AND ansible with one single dockercompose?
Modify ansible image not to create any directories in the image and to map pwd to pwd of the host
how to give a container a hostname
https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-to-containers
https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#adding-ansible-command-shell-completion

investigate Execution Environments
https://docs.ansible.com/ansible/latest/getting_started_ee/index.html#getting-started-ee-index

Copy ssh keys to nodes
https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_put_module.html#ansible-collections-ansible-netcommon-net-put-module
https://docs.ansible.com/ansible/latest/collections/ansible/posix/index.html#plugins-in-ansible-posix

install arista.avd
arista-galaxy collection arista.avd install

How to stop a container
docker stop <container>
docker kill <container>
ps -aux | grep <containier id>

How to remove a container


bring up container with ansible
WORKS
```bash
docker run --network clab --rm -it dlete/ansible:8.0.0 bash
```

WORKS
docker run --network clab --ip 172.20.20.10 --rm -it dlete/ansible:8.0.0 bash

WORKS
```bash
docker run --rm -it \
    --privileged \                      # puts you in root
    --name my_test_ansible_host \
    --network clab --ip 172.20.20.10 \
    -v $(pwd):$(pwd) \
    dlete/ansible:8.0.0 bash

docker run --rm -it \
    --name my_test_ansible_host \
    --network clab --ip 172.20.20.10 \
    -v $(pwd):$(pwd) \
    dlete/ansible:8.0.0 bash
```

does not work
```bash
docker run --rm -it --privileged \
    --name my_test_ansible_host \
    --network host \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /var/run/netns:/var/run/netns \
    -v /etc/hosts:/etc/hosts \
    -v /var/lib/docker/containers:/var/lib/docker/containers \
    --pid="host" \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    dlete/ansible:8.0.0 bash
```




ORDER
start containerlabs
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

start ansible
```bash
docker run --network clab --ip 172.20.20.10 --rm -it dlete/ansible:8.0.0 bash
```