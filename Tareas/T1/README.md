# Tarea 1: DCCasino :school_satchel:

## Consideraciones generales :octocat:

Primero que todo, creo que cabe destacar que el enunciado de la Tarea estaba bastante confunso, comenté con muchos 
compañeros ciertas cosas del enunciado y creo que algún error de enunciado podríamos tener (todo esto a pesar de 
haber leído las issues), por lo que explicaré mi código desde lo más profundo hasta lo más superficial

Lo más profundo corresponde a la entidad Bebestibles, la cual elaboré como una única clase (sin herencia de los 
distintos tipos de bebestibles) NO abstracta con su respectivo __init__ que posee el nombre, tipo y precio del bebestible, 
además, posee un método denominado consumir_bebestible() el cual retorna un valor aleatorio entre 2 dígitos dados (MIN_ENERGIA_BEBESTIBLE 
y MAX_ENERGÍA_BEBESTIBLE), aquí no definí lo que provoca en el jugador los distintos tipos de bebestibles.

Siguiendo con la entidad Jugador, la elaboré como una clase ABSTRACTA (que posee herencia, las cuáles corresponden a las distintas 
personalidades del jugador), esta función en su __init__ recibe TODAS las carácteristicas del jugador que vienen dentro 
del archivo  ```juegos.csv``` junto con: juegos_jugados (que corresponderá a una lista) y deuda (que corresponde a la resta entre el parametro 
DEUDA_TOTAL y el dinero que posee el jugador, self.dinero) y que además dentro del __init__ llamo a la función actualizar_deuda para que así 
mi característica self.deuda vaya cambiando a través del tiempo. Ahora definiremos las property que definí para energía, suerte, frustracion, 
ego, carisma y confianza (para que se respetaran los rangos dados por los parámetros). A continuación definí los métodos abstractos de esta 
clase abstracta, los cuáles son: comprar_bebestible, probabilidad_jugador, apostar, agregar_juego_jugado y actualizar_deuda; en primer lugar, 
comprar_bebestible lo que hace es definir si el jugador que juega (independiente de su personalidad) tiene el dinero para comprar el bebestible que 
desea, retornado un valor de True si es que puede y de False si es que no puede; en segundo lugar, probabilidad_jugador, que es el método que retorna la probabilidad de que el jugador gane el juego en base a sus características; en tercer lugar, apostar, que es el método que permite que el jugador juegue, pudiendo ganar o perder su dinero, retornando además un booleando que será True cuando el jugador gane y False cuando el jugador pierda; en cuarto lugar, agregar_juego_jugado, la cual añadirá a self.juegos_jugados el nombre del juego al cual el jugador está jugando; y en quinto lugar, actualizar_deuda, que como bien dije anteriormente, actualizara el valor de self.deuda.

Habiendo explicado superficialmente la clase Jugador, podemos definir las clases hijas de esta, las cuales corresponden a: Ludopata, Tacano, Bebedor y Casual. Todas estás clases ocupan las clases abstractas definidas anteriormente, pero en el caso de consumir_bebestible le agregan ciertas cosas, dado que el bebestible actúa de diferente manera dependiendo de la personalidad del jugador. Además, a cada sub-clase se le agrego su método característico (como tacaño_extremo, ludopatía, entre otros). Cabe destacar que en Casual para el método suerte_principiante únicamente se pidió que fuera su primera vez jugando a cualquier juego (y su suerte se mantiene con el agregado por toda su estadía).

Ahora que ya definimos nuestra clase Jugador podemos definir nuestra clase Juego, la cual posee su respecto __init__ que recibe: nombre, esperanza, apuesta mínima y apuesta máxima del juego. También se definieron los siguientes métodos: entregar_resultados y probabilidad_de_ganar. Creo que es mejor partir por probabilidad_de_ganar, ya que lo que hace esta función es recibir un objeeto que pertenece a la clase Jugador + una cantiad apostada, lo que hace este método es llamar a la función probabilidad_jugador del objeto que pertenece a la clase Jugador (ya que lo necesitamos para calcular la probabilidad de ganar el juego), y al calcular esa probabilidad la retorna (y es ocupada en el metodo apostar del Jugador, donde se compara con un numero random ocupando la funcion Random()); también esta la función entregar_resultados, donde se recibe un objeto que pertenece a la clase Jugador y un booleano indicando si la apuesta fue ganada o pertida (sacado de la funcion Apostar del jugador), en cualquier caso se actualizan los atributos del jugador y se imprimen en pantalla los cambios.

Después de todas estas clases viene la clase Casino, donde se simulará una partida de casino, en primer lugar, esta clase no recibe argumentos en su __init__, pero si posee atributos, los cuales son: self.jugador (jugador elegido para jugar), self.bebestibles (lista que contiene a los bebestibles que el jugador ha consumido) y self.juegos (lista que contiene a los jeugos que el jugador ha jugado). Además, posee las funciones evento_especial y jugar; en primer lugar, evento_especial, calcula la probabilidad de que ocurra el evento especial cuando el jugador apuesta, imprimiendo en pantalla si es que el caso tuvo el evento especial o no (en caso de que ocurra se le da un bebestible aleatorio al jugador); en segundo lugar esta la función apostar, que es lo principal de la tarea, dentro se encuentra todo el funcionamiento del codigo con todas las decisiones que puede tomar el participante, cabe destacar que ocupe mucho los while para que así si el jugador se equivocaba en alguna decisión no me fuera tan dificil devolverlo al mismo lugar que estaba antes.

Otra consideración importante es que dentro del archivo ```funciones.py``` se encuentran todos los menús del programa, así como también el hecho de cargar al jugador/bebestible/juego dentro de la clase que le corresponde.

El archivo principal main.py lo escribí así para que se viera más atractivo y no simplemente llamar al método.


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️
#### Programación Orientada a Objetos: 38 pts (28%)
##### ✅  Diagrama <Corregí lo que me indicaron en el avance de la tarea y creo que esta correcto de acuerdo a mi código>
##### ✅ Definición de clases, atributos, métodos y properties <La definición de las clases está bien, la única que me da duda es la de Casino, pero hable con muchos ayudantes y la mayoría me dijo que mientras explicara lo que hice no tendría ningún problmea>
##### ✅ Relaciones entre clases <Desarrolle relación entre todas las clases posibles, si bien no todas se relacionaron entre todas, como mínimo una clase se relacionó con otra>
#### Simulaciones: 10 pts (7%)
##### ✅ Crear partida <Se puede jugar una partida sin ningún tipo de problema, cualquier error que se cometa saldrá escrito en pantalla>
#### Acciones: 35 pts (26%)
##### ✅ Jugador <Todas las acciones que puede realizar el jugador (dependiendo de su personalidad) se lograron y se pueden llevar a cabo>
##### ✅ Juego <Todas las acciones que realiza el juego se lograron y se pueden llevar a cabo>
##### ✅ Bebestible <La accion de consumir bebestible está bien definida y responde a las distintas personalidades del jugador>
##### ✅ Casino <Todas las acciones del casino están definidas y funcionan correctamente>
#### Consola: 41 pts (30%)
##### ✅ Menú de Inicio <Contiene lo requerido y funciona de manera correcta, se encuentra en funciones.py>
##### ✅ Opciones de jugador <Contiene lo requerido y también funciona de manera correcta, se encuentra en funciones.py>
##### ✅ Menú principal <Contiene lo requerido, ante cualquier error notifica, se encuentra en funciones.py>
##### ✅ Opciones de juegos <Contiene lo requerido y cumple con las expectativas>
##### ✅ Carta de bebestibles <Cumple con lo requerido, lo único es que se asumirá que los bebestibles tienen cierto largo pero eso se verá después>
##### ✅ Ver estado del Jugador <Se muestran todas las características del jugador de manera ordenada>
##### 🟠 Robustez <Creo que se puede hacer de manera más corta la consola, sin embargo, funciona correctamente>
#### Manejo de archivos: 13 pts (9%)
##### ✅ Archivos CSV  <Se manipulan todos correctamente>
##### ✅ parametros.py <Todos los parámetros están bien definidos, se pueden cambiar si gusta>
#### Bonus: 3 décimas máximo
##### ✅ Ver Show <Se cumple con lo pedido, lo único es que consideré que tal vez no era tan necesario crear una clase con la entidad Show>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint(), random()```
2. ```abc```: ```ABC, abstractmethod``` 



## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Multiplicador bonificacion cliente recurrente debe ser un número entero: es válido ya que así se cumple con que todos los atributos del jugador sean int
2. El número máximo de carácteres del nombre del bebestible debe ser de 18 y del tipo debe ser de 20: es válido ya que en los archivos ninguno se pasa de ese número pero por si acaso lo incluí aquí



