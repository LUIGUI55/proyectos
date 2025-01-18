# introduccion a python
Es un lenguaje interpretado de tipado dinamico. Los programas (.py) pueden escribirse en un editor ligero como Geany, que es capaz de ejecutar codigo y compilarlo (.pyc).Ademas, tiene autocompletado, soporte multidocumento, gestion deproyectos, aplica colores de sintaxis y cuenta con emulador de terminal integrado.


## Escritura de programas.
La longitud maxima de linea recomendada es de 79 caracteres.
ountoy coma **;** se puede usar para separar varias sentencias en una misma linea, pero no se aconseja su uso;

```python
edad = 15; print(edad)
```
El codigo pyhon se escribe en cada linea desde la primera posicion excepto cuando es necesario dejar el codigo sangrado. El sangrado en Python es obligatorio, se hace con **Espacios en blanco** o **saltos de tabulacion** y sirve para agrupar bloques de lineas de codigo que tienen relacion a distintos niveles. Se utiliza con estructuras de control **(if-else,while,for)**, ademas con funsiones y clases.Ademas, permite que la lectura del codigo sea comoda y agradable.

El sangrado se puede hacer con espaciados y tabulaciones pero ambos tipos no se pueden mezclar

Es posible sangrar con un unico espacio en blanco pero **lo normal es utilizar un numero de espacios multiplo de cuatro** en cada nivel de sangrado (cuatro, ocho, doce, etc), o bien distinto numero de saltos de tabulacion.

Por defecto Geany inserta tabulaciones aunque se puede cambiar este modo de sangrar en las preferencias del menu 

Las expresiones entre parentesis **"()"**, llaves **"{}"** y corchetes **"[]"** separadas por comas **","** se pueden escribir ocupando varias lineas

### *Ejemplo* 
```python

# sangrado con 4 espacios 

edad = 23 

if edad >=18:
    print('Es mayor de edad:')
    else:
    print('Es menor de edad:')

# cuandoo el bloque a sangrar solo ocupa una linea de esta puede 
#escribirse desdepues de dos puntos:

if azul('Cielo')

# La antidiagonal "\" permite escribir una linea de
#codigo demasiado extensa en varias lineas:

if condicion1 and condicion2 and condicion3 and \ 
    condicion4 and condicion5

# Las expresiones entre parentesis, llaves o corchetes pueden 
#pueden ocupar varias lineas 

dias  = ['Lunes', 'Martes', 'Miercoles', 'Jueves',
'Viernes', 'Sabado', 'Domingo '] 
```

# PALABRAS RESERVADAS (VARIABLES,CADENAS)

las 35 palabras reservadas o (**Keywords**) de Python son:

```python
and,as,assert,async,await,break,class,continue,def,del,
elif,else,except,False,finally,for,from,global,if,import,
in,is,lambda,None,nonlocal,not,or,pass,,raise,return,True,
try,while,yield.
```

No se pueden declar variables,objetos,funsiones y clases con estos terminos.El siguiente codigo muestra la lista de palabras reservadas.

```python
import keyword
print(keyword.kwlist)
```

## Declarar varibales.

El signno igual "=" se utiliza para asignar numeros,booleanos,caadenas y expresiones a las variables de un programa.El tipo de Variable sera ek tipo de datos asignado: al declar una variable no es necesario especificar el tipo de dato porque mientras se asigna ek area de memoria necesaria el interprete python elige automaticamente el tipo mas apropiado.

El nombre de una variable tiene que empexar por una letra del alafabeto o un guion bajo.En las siguientes posiciones podran aparecer tambien numeros.Python ditingue entre mayusculas y minusculas:

```python

numero_entero = 5  # declara variable numérica
Numero_Entero = 5  # declara otra variable numérica distinta
x = y = z = 5  # asignación múltiple: x=5, y=5 y z=5
m, n = 5, 4 * 8  # asignación múltiple: m = 5 y n = 32
p1, p2 = (1, 2)  # asignación múltiple de tupla: p1 = 1 y p2 = 2 
cadena = 'Python3'  # declara cadena alfanumérica
cadena = 'Pytonisos\tdel\tmundo\n'  # incluye tab y salto de línea
cadena = '''cadenas
            que ocupan
            varias líneas'''  # declara cadena de varias líneas'
numero_float1 = 23.45  # números con decimales 
numero_float2 = 0.1e-3  # números con notación científica
numero_hexadecimal = 0x23  # número hexadecimal
booleano_verdad = True  # booleano: Verdadero
booleano_falso = False  # booleano: Falso
booleano_negar = not booleano_falso  # True, Verdadero
numero_complejo = 2 + 4j * 2  # (2+8j)

cadena1 = "4.5" # declara cadena1
cadena2 = "67" # declara cadena2
numero1 = float(cadena1) # Convierte cadena a flotante -> 4.5
numero2 = int(cadena2) # Convierte de cadena a entero -> 67

var_nula = None  # Declara variable con valor vacío o nulo

```
Asignar multiples valores de una lista

```python
a, *b = [1, 2, 3, 4]  # a toma primer valor y b lista con los demás
print('a', a)  # 1
print('b', b)  # [2, 3, 4]
```
*Resultado*
a:1
b:[2,3,4]

Variable especial:

En python un guion bajo unico '_' es una variable especial que almacena el valor en la ejecucion de codigo, que puede utlizarse con posterioridad para consultar su valor, en asignaciones, en calculos o simplemente cuando deseen ignorar los valores obtenidos evitando con ello el tener que declarar variables especificas.

El siguiente ejemplo la variable _ almacena en cada ciclo los valores del 0 al 9 que con posterioridad se van sumando ala variable **Total**:

```python
total = 0 
for _ in range(10):
    total += _
    print(total,end='') # 0 1 2 3 4 5 6 7 8 9 etc
```

En la siguiente asigacion multiple la variable _ se utiliza para asignar todos los valores excepto el primero y el ultimo que son los aue interesan para un calculoposterior.

```python
var1, *_, var2 = (10, 20, 30, 40, 50, 60, 70)
print(var1+var2)  # 80
```

En una lista de comprension la variable _ se puede utilizar para calculos:

```python
lista = [12, 15, 21, 17, 28]
cuadrados = [_**2 for _ in lista]
print(cuadrados)  # [144, 225, 441, 289, 784]
```
En el entorno interactivo de python se pueden usar tambien para acceder al valor obtenido como resultado de evaluar la ultima expresion:

```python
>>> 5 + 6
11
>>> _ 
11
```
## Nuestro primer programa en python:
#### Hola mundo en python.
En cualquier lenguaje de programacion al iniciar, no puede faltar el *famoso* Hola mundo...
Se trata del primer programa que se hace, que consiste en orgrmamar una aplicacion que muestra por medio de pantalla ese texto.

**EJEMPLO**:
```pyhton
 print("hola mundo desde pyhton:")
```
**or lo tanto ya sabes que la varibale *print* es para imprimir valores**.

#### Definiendo variables en python:

vamos a complicar mas cosas. Creemos una variable qwu almacene un numero. A diferencia de otros lenguajes de programacion no es necesario decirle a python el tipo de dato que queremos almacenar en *"x"*, en otro lenguaje es necesario especificar que *"x"* almacenara un valor entero. pero no es el caso de python.

**python es un lenguaje inteligente ya que al ver el numero 5, sabra de que tipo tendra que ser la "x"**
```python
x = 5
```

Ahora juntamos la varible *print* que ya sabemos para que sirve y la varible *x* 

```python
print(x)
# La salida sera el numero 5
```
En anterior fragmento habras visto el uso de *#*
se trata de la forma que tiene pyhton de crear los denominados comentarios.Un comentario es un tecto que acompana al codigo, pero que no es codigo propiamente dicho.Se usa para realizar anotaciones sobre el codigo que puedan resultar utiles a otras persoinas.En nuestro caso, simplmente lo hemos usado para decirte que la salida de ese comando cera *5*, ya que *x* valia 5.
### Sumando variables en pyhton.
Vamos a sumar dos variables e imprimir su valor. Lo primero vamos a declararlas con nombres *a* y *b*.
Declarar una variable significa crearla.
```python
#Declaramos las variables A,B
#y asignamos 2 valores.
a = 3
b = 7
```
Ahora pyhon ya conoce *a* y *b* y sus respectivos valores.Podemos hacer uso de *+* para sumarlos, y una vez mas de *print()* para mostrar los valores en pantalla.
```pyhton
print(a+b)
```
Es importante que solo usemos variables que solo allan sido definidas, porque de lo contrario tendremos un error.

El siguiente codigo hace uso de *if* para comprobar si la a es == a 10;
Si lo es se imprimira es "10" y si no lo es "no es 10";
```python
a = 10
if a == 10:
    print("Es 10")
else:
    print("No es 10")

```

### Decimales y cadenas 
De la misma forma que hemos visto que una varible puede alamcenar un valor entero como *10*, es posible tambien almacenar otros tipos como decimales o incluso cadenas de texto

Si queremos almacenar un valor decimal,basta con indicarlo usando la separacion con . 

```python
valor_decimal = 10.5625
```

Y si queremoa almacenar una cadena, es necesario indicar su contenido entre comillas simples o dobles *''* *""*

```python
mi_cadena = "Hola mundo"
```
...continue...
