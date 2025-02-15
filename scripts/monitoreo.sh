#!/bin/bash
# Monitorización de uso de CPU y memoria

while true; do
    echo "Uso de CPU: $(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}')"
    echo "Uso de Memoria: $(free -m | awk 'NR==2{printf "Memoria usada: %sMB (%.2f%%)\n", $3, $3*100/$2 }')"
    sleep 5
done