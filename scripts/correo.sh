#!/bin/bash
# Enviar un correo electrónico

TO="destinatario@example.com"
SUBJECT="Asunto del correo"
BODY="Cuerpo del correo"

echo "$BODY" | mail -s "$SUBJECT" "$TO"
echo "Correo enviado a $TO"


