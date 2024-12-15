import re

def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, correo):
        print(f"{correo} es válido.")
    else:
        print(f"{correo} no es válido.")

# Prueba de correos electrónicos
correos = ["usuario@dominio.com", "malformado@com", "@falso.com", "valido@correo.org"]
for correo in correos:
    validar_correo(correo)

