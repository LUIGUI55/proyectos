#!/bin/bash
# Encontrar y eliminar archivos más antiguos que 30 días

DIRECTORY="/ruta/al/directorio"
find "$DIRECTORY" -type f -mtime +30 -exec rm -f {} \;
echo "Archivos más antiguos que 30 días eliminados en $DIRECTOR"
