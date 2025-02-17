#!/bin/bash
# Backup de un directorio

SOURCE_DIR="/ruta/al/directorio"
BACKUP_DIR="/ruta/al/backup"

DATE=$(date +%Y%m%d%H%M%S)
BACKUP_NAME="backup_$DATE.tar.gz"

tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$SOURCE_DIR"
echo "Backup completado: $BACKUP_DIR/$BACKUP_NAME"

