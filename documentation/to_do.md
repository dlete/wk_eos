# Questions

## Why can't set specific version of ansible in Dockerfile?
A. Because you were using the parameter `ENV` incorrectly. You were using `ENV VERSION 15.1` and should have been writing `ENV VERSION=15.1`. You were missing the `=` symbol.

Q. Why have images with no names? and why can't be deleted saying they have child images?

## What is servicenow?

# References

## Courses
### UDEMY, Docker for the Absolute Beginner - Hands On - DevOps
<https://heanet.udemy.com/course/learn-docker/>

## Articles
<https://dzone.com/articles/ci-dockerizing-an-ansible-playbook-and-deploying-t>

<https://learn.microsoft.com/en-us/azure/developer/ansible/configure-in-docker-container?tabs=azure-cli>

### How to use Arista cEOS to build a topology to test features
<https://kevin-wang-xin.medium.com/how-to-use-arista-ceos-to-build-a-topology-to-test-features-49d316110b98>

# Commands

## Execute a process/command in a container
```bash
docker run <image> <command>
# execute a command WHEN STARTING a container
docker run <image> ansible-playbook -u playbook.yml
```

```bash
docker exec <container> <command>
# execute a command in RUNNING a container
docker exec <container> cat /etc/hosts
```

## Attach and detach
```bash
# run attached
docker run <container>

# run detached (d stands for detached). Container
docker run -d <container>

# if you want to attach to a running container
docker attach <container_name>
```

## run command in a running container
```bash
docker exec <container> <command>
docker exec d88cba4d610c cat /etc/*release*
```

## inspect container
```bash
docker inspect blissful_hopper
```

## container logs
```bash
docker logs blissful_hopper
```

## Image history
```bash
docker history <image_name>
```
