#!/bin/bash


for node in web-server{00..09}; do
    ssh $node 'echo -e "$HOSTNAME\t$(date "+%F") $(uptime)"'
done