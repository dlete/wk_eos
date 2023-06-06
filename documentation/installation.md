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
### Install docker
```bash
sudo apt install docker.io -y
```

### post install, one-off
Add yourself to the docker group.
```bash
sudo usermod -aG docker $USER
```

### start docker daemon
Start docker, in a WSL Ubuntu image it is necessary to use the command `dockerd`. In WSL the command `sudo service docker start` does not work. Neither does `sysctl docker start`. 
```bash
./auxiliary_scripts/start_docker_daemon
```

or
```bash
sudo dockerd > /dev/null 2>&1 &
disown
```

### Build the image
<https://learn.microsoft.com/en-us/azure/developer/ansible/configure-in-docker-container?tabs=azure-cli>

Build an image from a Dockerfile
<https://docs.docker.com/engine/reference/commandline/build/>
```bash
docker build . -t <tag_you_want>
docker build -t <tag_for_the_image> -f <path_to_dockerfile> .
```

### Run the container
https://learn.microsoft.com/en-us/azure/developer/ansible/configure-in-docker-container?tabs=azure-cli
Create and run a new container from an image
https://docs.docker.com/engine/reference/commandline/run/
```bash
docker run --rm -it <tag_you_want> bash
# map the host directory "$(pwd)/host_directory" (in your PC), to the directory "ansible" in the image"
docker run --rm -it -v $(pwd)/host_directory:/ansible_root dl_dockerfile_01 bash
```

## Ansible


## Arista image
Download cEOS from Arista.
Download too the README file
Transfer to the Linux instance.

### Import the Arista image
```bash
# import the downloaded cEOS-lab.tar.xz image
docker import cEOS-lab.tar.xz ceosimage:4.21.0F
```

### Create containers of Aristas
With compose



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