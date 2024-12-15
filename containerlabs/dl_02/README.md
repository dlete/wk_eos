# About
Lab with one node

# Operate

## Day to day
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

from within the .venv of the host
ansible-playbook playbook/ping.yml

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


# Troubleshoot

## BGP Setsockopt 
https://arista.my.site.com/AristaCommunity/s/article/Troubleshooting-cEOS-lab-on-WSL2

# Ansible
## from containerlabs container
## from the hosts
cd /workspace/wk_eos
source .venv/bin/activate # here you have ansible
cd containerlabs/<lab>      # because you have the ansible.cfg here
ansible-playbook playbooks/<playbook> -i inventory/<hosts>

## Connection
https://github.com/tonybourkesdnpros/Ansible_Quickstart_Arista/tree/main/Ansible-EOS
https://arista.my.site.com/AristaCommunity/s/article/Python-3-10-and-SSLV3-ALERT-HANDSHAKE-FAILURE-error

in inventory/hosts.yml
FABRIC:
  vars:
    # ansible_connection: set ansible_connection variable if required
    ansible_user: robot
    ansible_password: aladdin
    # we have defined the no checking of host keys in ansible.cfg
    #ansible_ssh_common_args: '-o StrictHostKeyChecking=no'
    ansible_connection: httpapi
    ansible_network_os: eos
    ansible_become: yes
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_ciphers: AES256-SHA:DHE-RSA-AES256-SHA:AES128-SHA:DHE-RSA-AES128-SHA

in group_vars
ansible_connection: ansible.netcommon.httpapi
ansible_network_os: arista.eos.eos

in playbook
