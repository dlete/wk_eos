# About this file
Installation instructions for the repository.

# Requisites
* none

# Installation

## Create a base directory
In your local computer, create a directory. This will be the root of the project.
```bash
mkdir ./<directory_name>
```
from now on we will refer to `<directory_name>` as `<base>`

Change the prompt to the newly created directory
```bash
mkdir cd ./<base>
```

## Docker
Install docker.
```bash
sudo apt install docker.io -y
```

Add yourself to the docker group.
```bash
sudo usermod -aG docker $USER
```

Start docker, in a WSL Ubuntu image it is necessary to use the command `dockerd`. In WSL the command `sudo service docker start` does not work. Neither does `sysctl docker start`. 
```bash
./auxiliary_scripts/start_docker_daemon
```

or
```bash
sudo dockerd > /dev/null 2>&1 &
```

### Build the container
# https://learn.microsoft.com/en-us/azure/developer/ansible/configure-in-docker-container?tabs=azure-cli
# Build an image from a Dockerfile
# https://docs.docker.com/engine/reference/commandline/build/
```bash
docker build . -t <tag_you_want>
```

### Run the container
# https://learn.microsoft.com/en-us/azure/developer/ansible/configure-in-docker-container?tabs=azure-cli
# Create and run a new container from an image
# https://docs.docker.com/engine/reference/commandline/run/
```bash
docker run -it <tag_you_want>
```

## Arista image
Download cEOS from Arista.
Download too the README file
Transfer to the Linux instance.

# References
## Arista
<https://avd.sh/en/stable/docs/installation/collection-installation.html>

# Uninstall
## Delete the base directory
Arista AVD collection installation
```bash
sudo rm -r ./<directory_name>
```




# Archive
## Create a conda environment
Create the environment
```bash
conda create <conda_environment_name>
```

and activate it
```bash
conda activate <conda_environment_name>
```

Later on, to deactivate
```bash
conda deactivate
```

To see a list of all your environments, type:
```bash
conda info --envs
```

## Install pip
Install 
```bash
conda install pip 
```

Verify  
```bash
conda list
```

## Delete the conda environment
Create the environment
```bash
sudo rm -r ~/miniconda3/envs/<conda_environment_name>
```

## Virtualenv

### Create a virtual environment for this project

* Install `apt-get install python3-venv`, this is necessary to create virtual environments with Python3.

```bash
sudo apt-get install python3-venv
```

* Create a virtual environment. Then activate the virtual environment.

```bash
python3 -m venv </path/to/new/virtual/environment>
source </path/to/new/virtual/environment>/bin/activate
```

I find it convenient to have the virtual environment files in the the root of the project. Also, ensure that those files are not tracked by git (add `*.venv` to `.gitignore`).

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Clone the code

```bash
git clone <url>
```

### Install Python packages

Upgrade `pip` in the virtual environment

```bash
pip install --upgrade pip
```

Install the Python packages

```bash
pip install -r requirements/base.txt
```