# LIst of things to do

How to attach to a running container

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

deploy 
containerlab deploy -t topology_02.yml 