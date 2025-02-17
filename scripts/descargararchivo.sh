#!/bin/bash
# Descargar un archivo desde una URL

URL="http://example.com/archivo.zip"
DEST_DIR="/ruta/al/directorio_destino"

wget -P "$DEST_DIR" "$URL"
echo "Archivo descargado desde $URL a $DEST_DIR"
