#!/bin/bash
if [ -f "$1" ]; then
    echo "El archivo $1 existe."
else
    echo "El archivo $1 no existe."
fi

