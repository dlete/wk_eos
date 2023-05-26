#!/usr/bin/bash

# taken from
# https://askubuntu.com/questions/1375195/run-dockerd-as-a-background-on-wsl-ubuntu
# the script below could be added to ~/.bashrc if you wanted the docker daemon to start
# automatically every time you log into the server.

# Start Docker (if not already running)
RUNNING=`ps aux | grep dockerd | grep -v grep`
if [ -z "$RUNNING" ]; then
    pid_of_dockerd=$(pidof dockerd)
    echo $pid_of_dockerd > "./mypid.pid"
    #kill -9 $pid_of_dockerd
    kill -9 "pidof dockerd"
    disown
fi
