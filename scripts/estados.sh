#!/bin/bash
# Comprobar el estado de un servicio

SERVICE_NAME="nombre_del_servicio"

if systemctl is-active --quiet "$SERVICE_NAME"; then
    echo "El servicio $SERVICE_NAME está activo."
else
    echo "El servicio $SERVICE_NAME no está activo."
fi