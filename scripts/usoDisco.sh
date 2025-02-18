#!/bin/bash
# Generar un informe de uso de disco

OUTPUT_FILE="/ruta/al/informe_uso_disco.txt"

df -h > "$OUTPUT_FILE"
echo "Informe de uso de disco generado en $OUTPUT_FILE"
