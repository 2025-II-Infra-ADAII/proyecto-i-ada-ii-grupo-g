# Informe de Correción - Algoritmo Voraz

## 0. Resumen

En esta sección del informe vamos a detallar el funcionamiento adecuado del programa, esto mediante el modo debug y los breakpoints, por los cuales se tomaron capturas de pantallas adecuadas para cada paso de la ejecución. Para esto cada sección de este informe esta dividida señalando que imagen representa cierta parte de la ejecución.

## 1. Voraz1

En esta parte del programa lo que se hace despues de abrir el archivo a leer es crear una nueva variable llamada "Finca" la cual empieza a recibir cada uno de los datos en el archivo, esto nos permitirá usarlos más adelante.

## 2. Voraz2 y Voraz3

Aqui como se puede comprobar es la parte en la que se le van añadiendo los datos a "Finca" con cada uno de los datos siendo asignado como P (Prioridad), T_S (Tiempo de supeervivencia) y T_R (Tiempo de Riego).

## Voraz4 y Voraz5

En esta sección del programa lo que se hace es crear la variable "Tablones_con_clave" los cuales nos serviran más adelante nuevamente, pero que tienen una particularidad y es que aquí se crea la clave para la programación voraz. Usando la formula:

\[
\text{Clave}_i = \frac{p_i}{tr_i}
\]

## Voraz6, Voraz7 y Voraz8

Esta parte es la que aplica un metodo de ordenamiento para los datos de la nueva variable "Tablones_ordenados", los cuales usando la "clave" del punto anterior trata de ordenar de manera descendente los datos de acuerdo a la clave.

## Voraz 9 y Voraz10

En esta parte del programa lo que hay es una serie de operaciones matematicas que son necesarias para el funcionamiento del programa, creando tres variables "costo_total", "penalización" y "tiempo_actual". Cada uno es lo siguiente:

- "Tiempo_actual": Representa el tiempo desde que se empezo hasta que se empieza a regar el tablón actual.
- "Penalización": Representa el tiempo adicional que se genera cuando un tablón se riega más allá de su tiempo ideal, en caso de que no pase no se genera ninguna por lo que no puede ser menor a 0 y si se tarda más se sumará
- "Costo Total": Este ultimo representa el costo al final de todos los tablones que se regaron y causaron penalización, por lo que su formula al final será P * Penalización.

## Voraz11

Esta es la penultima parte antes de devolver todo el algoritmo y array para guardar los resultados, pues se encarga de guardar todo lo que esta en "Tablones_Ordenados" asignado su orden original que se asigno al leer el archivo. Esto para saber en que orden se realizaron los riegos de acuerdo a su heurística

## Voraz12

Al final lo que nos retorna es lo que pedimos al programa que es no solo el costo total de realizar todos los riegos, sino tambien el orden en que se realizaron dichos riegos en un archivo que se puede leer.