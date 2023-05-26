# sourced from
# https://github.com/willhallonline/docker-ansible
# this file is for Ansible 2.13, with alpine 3.17 (2.13-alpine-3.17). Lives in:
# includes ansible-core + ansible
# https://raw.githubusercontent.com/willhallonline/docker-ansible/master/ansible-core/alpine316/Dockerfile

# pull base image
FROM alpine:3.17

# https://pypi.org/project/ansible-core/
ARG ANSIBLE_CORE_VERSION=2.15.0
# https://pypi.org/project/ansible/
ARG ANSIBLE_VERSION=7.6.0
# https://pypi.org/project/ansible-lint/
ARG ANSIBLE_LINT=6.16.2
ENV ANSIBLE_CORE_VERSION ${ANSIBLE_CORE_VERSION}
ENV ANSIBLE_VERSION ${ANSIBLE_VERSION}
ENV ANSIBLE_LINT ${ANSIBLE_LINT}

# LABEL about the custom image
LABEL maintainer="daniel.lete@heanet.ie"
LABEL version="2020-12-14"
LABEL description="This is a custom Docker Image \
with Alpine 3.17 and Ansible 2.13"

RUN apk --no-cache add \
        sudo \
        python3\
        py3-pip \
        #openssl \
        #ca-certificates \
        #sshpass \
        openssh-client \
        #rsync \
        git && \
    apk --no-cache add --virtual build-dependencies \
        python3-dev \
        libffi-dev \
        musl-dev \
        gcc \
        cargo \
        #openssl-dev \
        #libressl-dev \
        build-base && \
    pip3 install --upgrade pip wheel && \
    #pip3 install --upgrade cryptography cffi && \
    pip3 install ansible-core==${ANSIBLE_CORE_VERSION} && \
    pip3 install ansible==${ANSIBLE_VERSION} && \
    pip3 install --ignore-installed  ansible-lint==${ANSIBLE_LINT} && \
    #pip3 install mitogen jmespath && \
    #pip3 install --upgrade pywinrm && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* && \
    rm -rf /root/.cache/pip && \
    rm -rf /root/.cargo

RUN mkdir /ansible && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

WORKDIR /ansible

CMD [ "ansible-playbook", "--version" ]