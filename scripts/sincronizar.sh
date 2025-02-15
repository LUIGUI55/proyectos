#!/bin/bash
# Sincronizar dos directorios

SOURCE_DIR="/ruta/al/directorio_origen"
DEST_DIR="/ruta/al/directorio_destino"

rsync -av --delete "$SOURCE_DIR/" "$DEST_DIR/"
echo "Sincronización completada de $SOURCE_DIR a $DEST_DIR"