# Execute 
from 
https://docs.ansible.com/ansible/latest/getting_started_ee/run_execution_environment.html#running-custom-execution-environment


must have hosts.yml inside the inventory directory

ansible-navigator run test_remote.yml -i inventory --execution-environment-image ghcr.io/ansible-community/community-ee-base:latest --mode stdout --pull-policy missing --enable-prompts -u robot -k -K


https://www.liquidweb.com/blog/add-user-grant-root-privileges-ubuntu-18-04/

https://ansible-arista-howto.readthedocs.io/en/latest/INSTALL.html

# Installation and update

## Installation

* Create virtual environment
In the root of the repository

```bash
python3 -m venv .venv
```

* Activate the environemnt

```bash
source .venv/bin/activate
```

* Install packages

```bash
pip install -r requirements/base.txt
```

## Update

* Update pip. Execute whithin the environment

```bash
python -m pip install --upgrade pip
```

* Update all the packages

```bash
pip install -r requirements/base.txt --upgrade
# only Ansible
python3 -m pip install --upgrade ansible
```