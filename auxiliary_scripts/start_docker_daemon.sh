#!/usr/bin/bash

# taken from
# https://askubuntu.com/questions/1375195/run-dockerd-as-a-background-on-wsl-ubuntu
# the script below could be added to ~/.bashrc if you wanted the docker daemon to start
# automatically every time you log into the server.

# Start Docker (if not already running)
RUNNING=`ps aux | grep dockerd | grep -v grep`
if [ -z "$RUNNING" ]; then
    sudo dockerd > /dev/null 2>&1 &
    disown
fi
