# Tarea 0: Nombre de la tarea :school_satchel:

## Consideraciones generales :octocat:

El código corre de manera correcta lo pedido, se asumieron ciertos parámetros para que el código funcionara mejor, los cuáles serán explicados más adelante.

Para desarrollar la mayoría de las restricciones ocupe funciones las cuales se encuentran dentro de ```funciones.py``` y las interfaces Menú de Usuario, Menú de administrador y Menú de Inicio también se encuentra dentro de ```funciones.py```.

En el enunciado nos solicitaron que cuando una persona se equivoque en algún paso de algún procedimiento (por ejmplo realizando una encomienda) se pudiera continuar en el mismo error y no comenzar de cero, para desarrollar esto hice uso del comando ```while```.

Además, agregue comentarios sobre cada paso que realizaba el usuario/administrador, cosa de que fuera más "realista" el programa (por ejemplo: "¡Bienvenido de vuelta, administrador!")

Agregando a las consideraciones generales, cabe destacar que el nombre que le asigne a las variables ocupadas hacen alusión a la función que emplean, por ejemplo: "es_administrador = True or False", de tal manera que el código no sea tan díficil de leer

Para finalizar las consideraciones, con el objetivo de no superar las 100 líneas de codigo en una misma línea (valga la redundancia) ocupe el método "\" y seguir escribiendo abajo, pero tuve que pegar el texto a la izquierda del todo de la siguiente línea para que funcionara bien, me suena un poco extraño pero así me funcionó en VS Code.

### Cosas implementadas y no implementadas :white_check_mark: :x:


#### Menú de Inicio (18pts) (18%)
##### ✅ Requisitos <Se cumplieron todos\>
##### ✅ Iniciar sesión <Se logra de manera exitosa, dando error si el nombre de usuario no existe o la clave es incorrecta\>
##### ✅ Ingresar como administrador <Logrado, solo se logra entrar cuando la clave de administrador es correcta\>
##### ✅ Registrar usuario <Logrado, el nombre de usuario debe ser alfabético y la clave puede contener números y letra, una consideración es que para restringir esto lo que hice fue escribir a mano todas las letras y números\>
##### ✅ Salir <Logrado, con mensaje que indica que efectivamente se salió del programa\>
#### Flujo del programa (31pts) (31%) 
##### ✅ Menú de Usuario <Logrado, se muestran todas las opciones posibles a elegir y funcionan de manera correcta, cumplen además con todas las restricciones\>
##### ✅ Menú de Administrador <Logrado, se muestran todas las opciones posibles a elegir y de manera ordenada, se logran a cabalidad las funciones solicitadas\>
#### Entidades 15pts (15%)
##### ✅ Usuarios <Cumplido, se cumple con el formato solicitado para ingresar y utilizar a la entidad\>
##### ✅ Encomiendas <Cumplido, se logra manipular a la entidad de manera correcta\>
##### ✅ Reclamos <Cumplido, funciona de manera correcta y las restricciones asociadas a las commas también se respetan\>
#### Archivos: 15 pts (15%)
##### ✅ Manejo de Archivos <Todos los archivos están trabajados de manera correcta, con el formato asignado, para algunas funciones como mostrar la tabla con las encomiendas se asumieron cosas que serán explicadas más adelante\>
#### General: 21 pts (21%)
##### ✅ Menús <Se visualizan de manera correcta y ordenada\>
##### ✅ Parámetros <Se trabajó con todos los parametros solicitados\>
##### ✅ Módulos <Se trabajó con ciertas funciones que ayudaron a que el codigo funcionara, las cuáles serán detalladas mas adelante\>
##### 🟠 PEP8 <Creo que se pudieron haber pasado ciertas cosas, revisé detalladamente pero sinceramente no descartaría que alguna línea no estuviera en este formato>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```codigo.py```. Además se tiene el siguiente archivo ```funciones.py```, el cual contiene (valga la redundancia) todas las funciones asociadas al código; este archivo se modularizó en el programa. Cabe recalcar que todo el programa se trabajó en la carpeta T0


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```datetime```: ```datetime```


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Nombre de usuario como máximo de 26 caracteres: si el nombre de usuario sobrepasa esa cantidad de caracteres la tabla que se imprime en la función "actualizar
encomienda" del Menú de Administrador no funciona de manera correcta, además en la gran cantidad de páginas web se tiene un tope de caracteres por nombre de usuario.
2. Nombre de artículo como máximo de 57 caracteres: si el nombre de artículo sobrepasa esa cantidad de caracteres la tabla que se imprime en la función "actualizar
encomienda" del Menú de Administrador no funciona de manera correcta, además en la gran cantidad de servicios que ofrecen encomiendas tambiéne existe un máximo de
caracteres por nombre de artículo
3. Nombre del destino como máximo de 27 caracteres: si el nombre del destino sobrepasa esa cantidad de caracteres la tabla que se imprime en la función "actualizar encomienda" del Menú de Administrador no funciona de manera correcta.
4. Títulos del reclamo sin coma: en el enunciado de la tarea dice que tenemos que considerar que la descripción del reclamano puede contener comas, pero no indican
nada del título, por lo que asumí que nunca pondrán un ejemplo que lleve coma.


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://stackoverflow.com/questions/47823426/get-the-date-a-year-from-today-in-dd-mm-yyyy-format-in-python>: este hace \<obtener la fecha y hora actual en el formato correspondiente> y está implementado en el archivo <codigo.py> en las líneas <157/158>

