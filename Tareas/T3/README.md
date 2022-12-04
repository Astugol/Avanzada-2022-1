# Tarea 3: DCCasillas :school_satchel:

## Consideraciones generales :octocat:

¡Hola! No me explicaré tanto en los emojis de abajo sino que aquí explicare más en profundidad mi código, ya que considero que puede ser más fácil para ustedes (igualmente dejaré comentarios abajo).

Primero quiero decir que para este código me base mucho con respecto a: AF3 de este semestre, T3 del 2021-2, T3 del 2021-1. Por lo que notarás que la organización del código es bastante similar a estas.

Para correr este programa recomiendo utilizar la consola, lo que tienes que hacer es dentro de la carpeta "Servidor" hacer correr el archivo ```main.py``` y posteriormente en la carpeta "Jugador" hacer correr el archivo ```main.py```. Además, la carpeta Sprites que nos dieron en el enunciado debe ser colocada dentro de la carpeta Cliente, junto con las demás carpetas como "frontend" y "backend"

La conexión entre el servidor y el cliente funciona a la perfección, se logró encriptar, desencriptar, codificar y decodificar los mensajes de manera correcta, para esto, cada carpeta (Cliente y Servidor) posee un archivo ```codificacion.py``` en el que se encuentran todas estas funciones EXCEPTUANDO a la función decodificar, ya que considere más oportunido decodificar el mensaje en la función "recibir" tanto del servidor como del cliente. Además, en una de las sesiones de ayuda de la T3 le pregunté a un ayudante si para la decodificación podía ocupar únicamente los bytes utilizados por el bloque (ya que consideraba que los demás eran "inutiles") a lo que me indicó que si podía, por eso notarás que tanto "numero_bloque" como "utilizo_20" no los utilizo.

En la carpeta servidor se encuentra el archivo ```main.py``` el cual es el que debe ser ejecutado e instancia a la clase Servidor de ```servidor.py```, la cual se encarga de iniciar el servidor (valga la redundancia)

Dentro del servidor implementé un archivo llamado ```logica.py``` el cual se encarga de verificar que todo este en orden, además de hacer funcionar el juego (es instanciada en el archivo ```servidor.py```). Quiero destacar que el número aleatorio que recibe el jugador se implementa en este archivo y no en la carpeta Jugador ya que lo considere más oportuno en caso de que algún jugador pueda "hackear" el código y de algún modo asignarse el número que necesite para ganar.

Tanto el la carpeta Servidor como la carpeta Cliente poseen un archivo ```parametros.json```, el cual contiene los principales parametros que se utilizarán en el código, para poder leer estos parametros de mnaera correcta cree el archivo ```utils.py``` el cual dentro posee la función "data_json(llave)", la cual retorna el parametro que estamos buscando (esto tanto para el Servidor como para el Cliente)

La carpeta Cliente contiene el archivo ```main.py``` el cual es el que debe ser ejecutado y llama a la clase Cliente de ```cliente.py```.

Agregando, la carpeta Cliente fue separada en 2: "frontend" y "backend", en el frontend se encuentran todas las ventanas que el juego necesita, junto con otra carpeta denominada "ui_files", la cual contiene todos los .ui de todas las ventanas.

En el backend se encuentra el archivo ```cliente.py``` el cual se encarga de establecer la conexión con el servidor, para no hacer tanto lio de código (y basándome también en la AF3 jaja) cree otro archivo llamado ```interfaz.py``` el cual se encarga de instanciar a todas las ventanas del juego y de manejar los mensajes que envía el Servidor.

Además, tenemos el archivo ```logica_juego.py``` el cual se encarga de (valga la redundancia) toda la lógica detrás del juego. Una cosa que puede llamarte la atención es que el archivo ```ventana_juego.py``` (de la carpeta frontend) es mucho más largo que el archivo ```logica_juego.py```, pero tiene una explicación y esto es ya que me trate de asegurar lo más posible de incluir todos los casos borde, y como los labels son tantos me quedó algo bastante "cochino" (notarás que las líneas están muy pegadas unas a otras, pero si las separaba el archivo quedaba de más de 400 líneas :(, perdón de antemano, si se puede te recomendaría que las separaras en las condiciones (if, elif y else; y también con los for) ya que tal vez lo entenderias mejor)

He probado hasta el cansancio el código y podría asegurarte que para 2 personas funciona de manera excelente, para 3/4 personas también lo probé y funciona de manera correcta, pero no lo he probad tantas veces y quizas se me haya escapado un caso borde.

En general creo que implementé todo lo que se pedia en la tarea, asumí ciertas cosas que te las dejaré abajo en la sección de "supuestos", gracias!

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Networking: 23 pts (18%)
##### ✅ Protocolo <Se implementa de manera correcta>
##### ✅ Correcto uso de sockets <Se implementa de manera correcta>
##### ✅ Conexión <Cliente y servidor se conectan y funcionan>
##### ✅ Manejo de clientes <Los clientes son trabajados de manera correcta>
#### Arquitectura Cliente - Servidor: 31 pts (25%)
##### ✅ Roles <Los roles están bien definidos>
##### ✅ Consistencia <Estoy casi seguro que la consistencia es adecuada>
##### ✅ Logs <La función log es implementada para imprimir cosas en consola>
#### Manejo de Bytes: 26 pts (21%)
##### ✅ Codificación <Los mensajes son codificados de manera correcta gracias a la función codificar de ```codificacion.py```>
##### ✅ Decodificación <Los mensajes son decodificados de manera correcta y en la función recibir del servidor o cliente>
##### ✅ Encriptación <Los mensajes son encriptados de manera correcta gracias a la función encriptar de ```codificacion.py```>
##### ✅ Desencriptación <Los mensajes son desencriptados de manera correcta gracias a la función desencriptar de ```codificacion.py```>
##### ✅ Integración <El protocolo para el envío de mensajes se utiliza correctamente>
#### Interfaz: 23 pts (18%)
##### ✅ Ventana inicio <La ventana de inicio cumple con todo lo pedido>
##### ✅ Sala de Espera <La sala de espera cumple con todo lo requerido, además de activar el botón solo para el host de la partida (primera persona en conectarse)>
##### ✅ Sala de juego <La sala de juego meustra todos los elementos mínimos y se actualiza a tiempo real>
##### ✅ Ventana final <La ventana final contiene todo lo requerido, además del botón para volver a la ventana de inicio>
#### Reglas de DCCasillas: 18 pts (14%)
##### ✅ Inicio del juego <Solo se puede dar inicio al juego cuando hayan mínimo 2 jugadores en la partida, y cuando hayan 4, esta comenzará automáticamente>
##### ✅ Ronda <Solo el jugador con el turno asignado puede tirar el dado, los demás tendrán el boton inhabilitado>
##### ✅ Termino del juego <El juego termina cuando algún jugador tenga sus 2 fichas en la zona de victoria>
#### General: 4 pts (3%)
##### ✅ Parámetros (JSON) <Los parametros json son ocupados de manera correcta>
#### Bonus: 5 décimas máximo
##### ❌ Cheatcode <No lo hice>
##### ❌ Turnos con tiempo <No lo hice>
##### ❌ Rebote <No lo hice>

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` (tanto en el servidor como cliente). Además se debe crear los siguientes archivos y directorios adicionales:
1. ```Sprites``` en ```cliente``` (carpeta)


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```math```: ```ceil, trunc```
2. ```random```: ```randint```
3. ```threading```: ```Lock```
4. ```pickle```
5. ```socket```
6. ```os```: ```path.join```
7. ```json```
8. ```PyQt5.QtWidgets```: ```QApplication```
9. ```sys```
10. ```PyQt5.QtCore```: ```QObject, pyqtSignal, QTimer, Qt```
11. ```PyQt5.QtGui```: ```QPixmap```
12. ```PyQt5```: ```uic```


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Solo se puede comenzar un nuevo juego cuando todos los demás jugadores hayan salido de la ventana final --> Es válido ya que sino tendríamos que "expulsarlos" de la sala de espera, sin embargo, nos pidieron que tuvieramos un botón para cuando el jugador quiera salir.
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<AF5 de este semestre>
