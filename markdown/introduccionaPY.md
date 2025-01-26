## Curso Python

    1.- Bienvenida
    2.- Entorno de aprendizaje
    3.- Itroduccion informal
        a) Numeros
        b) Cadenas

# Numeros en python
```python
    # modulo
    3 % 2
    #Potencia
    3**3
    # Podemos distinguir 3 tipos denumeros 
    #enteros, que no tienen parte decimal y van desde menos hasta infinito
    #flotantes: Son numeros que tienen parte decimal 
    #numero Entero:
    (3-2+4*10)

    n=3 
    n
    print(n)
    #va a imprimir 3
    n+3
    #nos va a imprimir 3

    # Sumar dos varibles
    m=10
    n+m
    #nos va  a imprimir la suma de n + m 
    type(m) #--> se ve el nombre dela variable

    n*m+10
    n=10
    m=15
    n+m
    #ES igual a 25
    n=m
    #asignacion
    n # Imprime el valor de la variable "m"
    n = n+25 #Acumulador y el resultado sera igual a 40:

    nota_1 = 2 
    nota_2 = 5
    nota_media = (nota_1 + nota_2)
    #imprimimos
    nota_media #da el resultado 3.5
```


# Cadenas en Python
```python
print("hello World")
print('Este es un texto que incluye " " ')
print("Esta 'palabra se encuentra escrita entre comillas simples'")
print("Esta\"palabra\" se encunetra escrita para collcar comillas del mismo tipo")
print("Esta\'palabra\' se encunetra escrita para collcar comillas simples")
print("una cadena")
print('otra cadena mas')
print('otra cadena mas')

print("un texto\t una tabulacion") #Son caracteres especiales... <Tabulador>

print("un txto\nuna nueva linea")

# ejemplo extrano

print("C:\nnombre\directoriox")
print(r"C:\nombre\directoriox")
print("""Una linea
otra linea 
otra linea
otro gato...\t
una tabulacio""")

c = "Esto es una cadena\n con dos lineas" 
type(c)
```
## Operaciones

```python
c = "esto es una cadena\n de dos lineas"
c+c
# imprime esto es una caadenas de dos lineas
s = "una cadena " "compuesta de dos cadenas"
c1 = ("una cadena")
c2 = "otra cadena"
print("una cadena" + c2 )

diez_espacios = "" *10
print(diez_espacios + "un texto a 10 espacios")

M = "HOLA "

print(M*10)
# te imprime hola hola hola hola hola hola...
```
### Indices en las cadenas 

```python
    palabra = "Python" 
    palabra[0] # p
    palabra[3] # h
    palabra[-1] # n
    print(palabra[-0]) # p
    print(palabra[-2]) # o 
    print(palabra[-6]) # p 
    

```

