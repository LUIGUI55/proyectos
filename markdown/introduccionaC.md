### 1.- introduccion 
El lenguaje de programación C está caracterizado por ser de uso general, con una sintaxis sumamente compacta y de
alta portabilidad.
Es común leer que se lo caracteriza como un lenguaje de "bajo nivel". No debe confundirse el término "bajo" con
"poco", ya que el significado del mismo es en realidad "profundo", en el sentido que C maneja los elementos básicos
presentes en todas las computadoras: caracteres, números y direcciones .
Esta particularidad, junto con el hecho de no poseer operaciones de entrada-salida, manejo de arreglo de caracteres,
de asignación de memoria, etc , puede al principio parecer un grave defecto; sin embargo el hecho de que estas
operaciones se realicen por medio de llamadas a Funciones contenidas en Librerías externas al lenguaje en sí, es el
que confiere al mismo su alto grado de portabilidad, independizandolo del "Hardware" sobre el cual corren los
programas, como se irá viendo a lo largo de los siguientes capítulos.
La descripción del lenguaje se realiza siguiendo las normas del ANSI C, por lo tanto, todo lo expresado será
utilizable con cualquier compilador que se adopte; sin embargo en algunos casos particulares se utilizaron funciones
Compilador ó Sistema Operativo-dependientes, explicitándose en estos casos la singularidad de las mismas.

### 2.- ANATOMIA DE UN PROGRAMA C

Siguiendo la tradición, la mejor forma de aprender a programar en cualquier lenguaje es editar, compilar, corregir y
ejecutar pequeños programas descriptivos. Analicemos por lo tanto el primer ejemplo :
EJEMPLO 1
#include <stdio.h>
main()
{
printf("Bienvenido a la Programacion
en lenguaje C \n");
return 0;
}
#### FUNCION main()
Dejemos de lado por el momento el análisis de la primer linea del programa, y pasemos a la segunda.
La función main() indica donde empieza el programa, cuyo cuerpo principal es un conjunto de sentencias
delimitadas por dos llaves, una inmediatamente después de la declaración main() " { ", y otra que finaliza el listado
"} ". Todos los programas C arrancan del mismo punto: la primer sentencia dentro de dicha función, en este caso
printf ("......")

En el EJEMPLO 1 el programa principal está compuesto por sólo dos sentencias: la primera es un llamado a una
función denominada printf(), y la segunda, return, que finaliza el programa retornando al Sistema Operativo.
Recuérdese que el lenguaje C no tiene operadores de entrada-salida por lo que para escribir en video es necesario
llamar a una función externa. En este caso se invoca a la función printf(argumento) existente en la Librería y a la
cual se le envía como argumento aquellos caracteres que se desean escribir en la pantalla. Los mismos deben estar
delimitados por comillas. La secuencia \n que aparece al final del mensaje es la notación que emplea C para el
caracter "nueva linea" que hace avanzar al cursor a la posición extrema izquierda de la línea siguiente. Más adelante
analizaremos otras secuencias de escape habituales.
La segunda sentencia (return 0) termina el programa y devuelve un valor al Sistema operativo, por lo general cero si
la ejecución fué correcta y valores distintos de cero para indicar diversos errores que pudieron ocurrir. Si bien no es
obligatorio terminar el programa con un return, es conveniente indicarle a quien lo haya invocado, sea el Sistema
Operativo o algún otro programa, si la finalización ha sido exitosa, o no. De cualquier manera en este caso, si
sacamos esa sentencia el programa correrá exactamente igual, pero al ser compilado, el compilador nos advertirá de
la falta de retorno.
Cada sentencia de programa queda finalizada por el terminador "; ", el que indica al compilador el fin de la misma.
Esto es necesario ya que, sentencias complejas pueden llegar a tener más de un renglón, y habrá que avisarle al
compilador donde terminan.
Es perfectamente lícito escribir cualquier sentencia abarcando los renglones que la misma necesite, por ejemplo
podría ser:
printf("Bienvenido a la Programacion en lenguaje C \n")

### 3.- ENCABEZAMIENTO.

Las líneas anteriores a la función main() se denominan ENCABEZAMIENTO (HEADER) y son informaciones que
se le suministran al Compilador.
La primera línea del programa está compuesta por una directiva: " #include " que implica la orden de leer un archivo
de texto especificado en el nombre que sigue a la misma ( <stdio.h> ) y reemplazar esta línea por el contenido de
dicho archivo.
En este archivo están incluidas declaraciones de las funciones luego llamadas por el programa (por ejemplo printf() )
necesarias para que el compilador las procese. Por ahora no nos preocupemos por el contenido del archivo ya que
más adelante, en el capítulo de funciones, analizaremos exhaustivamente dichas declaraciones.
Hay dos formas distintas de invocar al archivo, a saber, si el archivo invocado está delimitado por comillas (por
ejemplo "stdio.h") el compilador lo buscará en el directorio activo en el momento de compilar y si en cambio se lo
delimita con los signos <.......> lo buscará en algun otro directorio, cuyo nombre habitualmente se le suministra en el
momento de la instalación del compilador en el disco ( por ejemplo C:\TC\INCLUDE). Por lo general estos archivos
son guardados en un directorio llamado INCLUDE y el nombre de los mismos está terminado con la extensión .h

La razón de la existencia de estos archivos es la de evitar la repetición de la escritura de largas definiciones en cada
programa.
Nótese que la directiva "#include" no es una sentencia de programa sino una orden de que se copie literalmente un
archivo de texto en el lugar en que ella está ubicada ,por lo que no es necesario terminarla con "; ".

### 4.- COMENTARIOS

La inclusión de comentarios en un programa es una saludable práctica, como lo reconocerá cualquiera que haya
tratado de leer un listado hecho por otro programador ó por sí mismo, varios meses atrás. Para el compilador, los
comentarios son inexistentes, por lo que no generan lineas de código, permitiendo abundar en ellos tanto como se
desee.
En el lenguaje C se toma como comentario todo caracter interno a los simbolos: /* */ . Los comentarios pueden
ocupar uno o más renglones. También podemos tener comentarios sobre una misma líneas mediante la inclusión de
doble barras //
```C
suma = suma + k // comentario sobre la línea
/* este es un comentario corto */
/* ..........
............ */

```
