# About
Lab with one node

# Operate
Start containerlabs container
```bash
docker run --rm -it --privileged \
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

```bash
sudo containerlab deploy -t <topology_file>
```

open as many terminals as you want, and connect to the container
```bash
# containerlabs/ansible
docker exec -it 42c3dc91483f zsh
# arista ceos
docker exec -it <name or id> Cli
```

save running to startup, https://containerlab.dev/cmd/save/
```bash
sudo containerlab save -t <topology file>
```

then comment out the line 
#startup-config: init-configs/ceos-cfg.j2
in the topology file

arista in containerlabs
https://containerlab.dev/manual/kinds/ceos/#user-defined-config


firts time a switch boots
configure startup file in the topology file
boot device
configure
save to startup
destroy lab/shutdown
coment out the startup config
boot -> boots with the ocnfiguration in startup