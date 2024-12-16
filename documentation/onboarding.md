# About this file
Onboarding instructions.

## Install
## Operate
## Labs
One folder per lab.

## References
Related, useful information.

## Conventions
### Ansible files
All in `*.yml`. Do not use any other extension.

### File extensions
Three letters.

YAML, `*.yml`

## Known issues
### Arista connection with Ansible
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