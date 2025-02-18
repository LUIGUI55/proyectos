#!/bin/bash
# Realizar un escaneo de puertos

HOST="127.0.0.1"
PORTS=(22 80 443)

for PORT in "${PORTS[@]}"; do
    (echo > /dev/tcp/$HOST/$PORT) &> /dev/null && echo "Puerto $PORT está abierto en $HOST" || echo "Puerto $PORT está cerrado en $HOST"
done

