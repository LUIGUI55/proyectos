#!/bin/bash
# Realizar un ping a una lista de servidores

SERVERS=("servidor1.com" "servidor2.com" "servidor3.com")

for SERVER in "${SERVERS[@]}"; do
    if ping -c 1 "$SERVER" &> /dev/null; then
        echo "$SERVER está accesible."
    else
        echo "$SERVER no está accesible."
    fi
done
