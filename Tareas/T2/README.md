# Tarea 2: DCComando espacial :school_satchel:


## Consideraciones generales :octocat:

¡Hola! Debido a la gran cantidad de líneas de código en esta tarea, voy a ir explicando parte por parte el código para que sea más ameno corregir, recomiendo fuertemente revisar todo con esto al lado, para que se entienda de mejor manera.

Como contexto, se respetó la diferenciación entre back-end y front-end, dentro del back-end se encuentran archivos como "clase_arma.py", "clase_jugador.py" y "clase_alien.py", estos archivos contienen las clases de las entidades que se utilizaran; además, se encuentran archivos con la siguiente secuencia: "logica_XX.py", estos archivos son los encargados de la lógica de la respectiva ventana a la que están asociados.

Algo que también me gustaría comentar es que para esta tarea me base mucho en el código de la AS3 que tuvimos, y en ese código en el back-end implementaban un QLabel y le asignaban un QPixmap, por lo que pensé que estaba bien, sin embargo varios ayudantes me han dicho que me podían descontar puntaje por eso, pero en el momento que me dijeron ya llevaba muy avanzado el código y "arreglarlo" me significaba estar muchas más horas en la tarea, espero que se comprenda la situación

Para partir, dividimos todo en back-end y front-end, dentro del front-end definí la ventana de inicio del juego (dentro del archivo ventana_juego.py), esta ventana la hice "a mano" (sin qt designer), además, la clase posee los métodos "jugar" y "ver ranking", que están asociados a los botones que se encuentran disponibles en la ventana, aquí se implementaron dos señales, la señal "abrir_ventana_principal" que se conecta con el método "mostrar_ventana" de la ventana principal (que veremos más adelante) y la señal "abrir_ventana_ranking" que se conecta con el método "mostrar_ventana" de la ventana ranking.

Ahora pasamos a la ventana principal, la cual se encuentra dentro de "ventana_principal.py", esta ventana la implementé en qtdesigner (**Todos los .ui se encuentran dentro de la carpeta "designer" en "frontend"**), existen diversos métodos que los iremos explicando uno por uno, primero se encuentra el método "mostrar_ventana" que lo único que hace es mostrar la ventana (valga la redundancia) y limpiar el label donde el usuario escribe su nombre. En segundo lugar se encuentra el método "iniciar_usuario" que se encarga de recopilar el nombre de usuario que se ingresó y el botón que fue apretado, este método envía la señal "senal_enviar_login" que se conecta con la lógica de la ventana principal (dentro de la carpeta backend en "logica_principal.py"), dando como atributo una tupla que contiene una lista con los booleanos de si el botón fue o no presionado, y un string que contiene el nombre de usuario ingresado. En tercer lugar se encuentra el método "recibir_validación" que está conectado a una señal en el archivo "logica_principal.py" (que explicaremos más adelante), este método recibe un booleano ("valid") que indica si el registro del usuario fue exitoso y una lista de errores ("errores") que contiene los tipos de errores que pudieron haber ocurrido cuando el usuario quizo jugar.

Siguiendo con la ventana principal tenemos la lógica de esta, que se encuentra en "logica_principal.py", está contiene el método comprobar que recibe la tupla que anteriormente habíamos mandado a través de la señal "senal_enviar_login", este método se encarga de comprobar que el usuario cumpla con los requisitos para continuar. Aquí se encuentran 3 señales, la "senal_respuesta_validación" que es enviada SIEMPRE ya que contiene el booleano del registro y la lista de errores (que se asocia con el método "recibir_validación" de la ventana principal), la señal "senal_abrir_juego" y la señal "senal_cargar_usuario" que son enviadas ÚNICAMENTE cuando el registro fue exitoso, la primera envía el tipo de ambiente escogido por el jugador y la segunda el nombre de usuario y ambiente escogido por el jugador (más adelante comentaré los métodos con los que se conectan pero siento que ahora puede ser más engorroso ya que no lo he explicado)

Posterior a esto (y en caso de que el registro haya sido exitoso) procedemos a la ventana del juego, que se encuentra dentro del archivo "ventana_juego.py", esta ventana la diseñé en qt designer y posee una gran cantidad de señales y métodos (intentaré hacerlo lo más claro posible). En primer lugar poseemos el método "mostrar_ventana" que es el método asociado a la señal "señal_abrir_juego" de la lógica principal, este metodo crea los "players" de los sonidos que se ocuparan (la risa y el disparo), además insertamos el fondo dependiendo del ambiente que haya escogido el jugador. Posterior a eso tenemos "keyPressEvent" que se encarga de revisar las teclas que presiona el jugador (pero que depende de si el juego está en pausa o no), en caso de que presione teclas permitidas en el juego, (**el disparo se ocupará con la letra "k"**), se enviará la señal "senal_tecla" hacia la lógica del juego, también se aprovechó de definir inmediamente los cheatcodes que en el caso de que sean apretados por el usuario, se envía una señal hacia la lógica del juego que se encargará de hacerlos funcionar. En segundo lugar, tenemos el metodo cargar_jugador que está asociado a la señal "senal_cargar_usuario" de la lógica principal, que se encarga de cargar al jugador en la clase Jugador. En tercer lugar, tenemos el método mostrar_alien, que se encarga de hacer visibles a los aliens en la ventana. En cuarto lugar, tenemos el método mostrar_mira que hace que la mira aparezca al momento de iniciar el juego. En quinto lugar, tenemos el método "definir_aliens" que se encarga de hacer como atributo de la clase a los aliens, puestos en una lista. En sexto lugar, tenemos el método "mover_mira" que se encarga de que la mira haga los movimientos que define el jugador. En sexto lugar, tenemos el método mover_aliens que se encarga de lo mismo que el método "mover_mira", solo que los movimientos están ya definidos. Después de esto vienen una serie de métodos que se encargan de hacer la animación de la muerte de los aliens, asignando los pixeles que deben ir en cada momento de la explosión. En séptimo lugar, tenemos el método "cambiar_mira_disparo", que se encarga de cambiar el color de la mira a rojo. En octavo lugar, tenemos el método "volver_mira" que se encarga de volver al color negro de la mira después de haber pasado un segundo (todo esto se controla por timers en la lógica del juego). En noveno lugar, tenemos el método actualizar_balas que se encarga de que el label asociado al número de balas se vaya actualizando dependiendo de la cantidad de balas que tenga el jugador. En noveno lugar, tenemos el método "actualizar_nivel" que se encarga de actualizar el label asociado al nivel actual que se encuentra el jugador. En decimo lugar tenemos el método "pausar_juego" que se encarga de ponerle pausa y reanudar al juego (valga la redundancia nuevamente). En onceavo (?) lugar tenemos el método "juego_terminado" que se encarga de terminar el juego poniendo en un label el resultado del juego y haciendo la animación del perro en caso de ganar (junto con la risa). En doceavo (?) lugar tenemos el método "pasar_post_juego", que se encarga de cerrar la ventana y mandar la señal "senal_mostrar_ventana_postjuego" para que se abra la otra ventana. En treceavo (?) lugar tenemos el método "reiniciar_ventana" que se encarga de esconder a todos los labels de los aliens, tambien de eliminar el texto que indicaba el resultado de la partida y de volver al perro en su versión normal. En penúltimo lugar tenemos el método "salir_juego" que está asociado al botón "salir", lo que hace es guardar el puntaje acumulado que llevaba el jugador y cierra la ventana, abriendo la ventana de inicio. En último lugar tener el método "actualizar_barra", que se encarga de actualizar continuamente la barra de tiempo. Quiero aclarar que di un repaso muy por encima ya que hay muchas señales que creo que quedaría algo extremadamente largo. 

Ahora tenemos la lógica del juego, la cual se encuentra dentro del archivo "logica_juego.py", esta lógica se encarga del funcionamiento del juego, posee una gran cantidad de timers de los cuáles quiero destacar "timer_actualizar_juego" (asociado al método "actualizar_juego") que se encargad en que TODO el tiempo se esté actualizando la posición de los aliens, la cantidad de aliens muertos y los requerimientos para pasar de nivel o aparecer otros aliens. Un aspecto importante a destacar es que esta clase posee como atributo la mira. Además, considero que explicar todos los métodos no vale la pena ya que son bastante autoexplicativos, además, el juego funciona correctamente. 

Posterior al juego tenemos la ventana post-juego, esta ventana se encuentra dentro de "ventana_postjuego.py" y fue diseñada en qt designer, dependiendo del resultado del juego permite seguir jugando o únicamente volver a la ventana de inicio.

También tenemos la lógica del post_juego, que se encarga de guardar el nombre y puntaje que obtuvo el jugador en su partida, dentro del archivo "puntajes.txt".

Luego, tenemos la ventana del ranking, dentro del archivo "ventana_ranking.py", esta ventana posee los mejores puntajes obtenidos en el juego, pero como necesita de una "lógica", cree la "logica_ranking.py", que se encarga de hacer una lista con el nombre de los mejores puntajes y otra lista con el puntaje obtenido, para que así en la ventana del ranking sea unicamente reemplazar en los labels el nombre y puntaje dados por la lista.

Una última consideración es que probablemente para la precisión de la mira existen casos donde por pocos pixeles el alien muere sin que necesariamente la mira este centrado en él, intente hacerlo lo mejor posible pero la precisión no está al 100% sino que al 90%.

La carpeta de Sprites y Sonidos es la misma que la que nos entregaron el en enunciado.


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Ventana de Inicio: 4 pts (4%)
#### Ventana de Ranking: 5 pts (5%)
#### Ventana principal: 7 pts (7%)
#### Ventana de juego: 14 pts (13%)
#### Ventana de post-nivel: 5 pts (5%)
#### Mecánicas de juego: 47 pts (45%)
##### ✅ Arma <Se puede mover correctamente y tiene todo lo que se requiere, la instancie como una clase>
##### ✅ Aliens y Escenario de Juego <Los aliens están definidos por una clase, y el escenario de juego responde de manera correcta ante la decisión del jugador>
##### ✅ Fin de Nivel <Se cumple con lo requerido, la dificultad, tiempo y número de aliens funcionan correctamente gracias a la lógica del juego.>
##### ✅ Fin del juego <Se logra guardar el nombre y puntaje obtenido, revise prácticamente todos los casos borde>
#### Cheatcodes: 8 pts (8%)
##### ✅ Pausa <Funciona con la letra P y con el boton de pausa, todo se logra a través de señales entre la ventana del juego y la lógica del juego>
##### ✅ O + V+ N + I <Se logra cumplir con el cheatcode, simplemente no pude poner balas infinitas sino que le puse un número extremadamente grande>
##### ✅  C + I + A <Se logra cumplir con el cheatcode, lo único es que le da el nivel por ganado, no salta directamente al otro nivel sino que hace la animación del nivel ganado, pero se cumple con el objetivo>
#### General: 14 pts (13%)
##### ✅ Modularización <Está bien modularizado>
##### 🟠 Modelación <No descartaría errores de back-end, front-end, intenté hacerlo lo mejor posible>
##### ✅ Archivos  <Se trabaja de manera efectiva con los archivos>
##### 🟠 Parametros.py <Ocupé todo lo dicho en el enunciado, pero nuevamente, no descarataría que se me haya pasado algo>
#### Bonus: 10 décimas máximo
##### ✅ Risa Dog <Se implementó correctamente en la ventana del juego>
##### ❌ Estrella <No lo hice>
##### ❌ Disparos extra <No lo hice>
##### ❌ Bomba <No lo hice>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```.   

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```choice, randint```
2. ```PyQt5.QtCore```: ```QObject, pyqtSignal, QTimer, QRect, QUrl```
3. ```PyQt5.QtMultimedia```: ```QMediaPlayer, QMediaContent```
4. ```PyQt5.QtGui```: ```QPixmap```
5. ```PyQt5.QtWidgets```: ```QLabel, QApplication```
6. ```PyQt5```: ```uic```
7. ```sys```


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://www.youtube.com/watch?v=Ciz3slS1xt0&ab_channel=JieJenn>: este hace \<el audio del disparo y la risa del perro, está implementado en las líneas 58 a 66 de la ventana_juego.py>
