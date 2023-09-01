# Tarea 0: Star Advanced 🚀🌌


## Consideraciones generales :octocat:

```main.py``` se ocupa coo ejecutor del codigo, este importara los modulos donde obtendra las funciones
nescesarias para la ejecución del juego, se ocupo una logica similar al motor Unity, donde el juego funciona
segun "escenas", estas se ocupan como variables y elementos visuales en la ejecución de la tarea.
Las escenas son archivos de texto y su uso como variable es el nombre que poseen cada una, usan nombres
descriptivos en ingles.
 Cada jugador tiene 2 tableros, uno que es el que se muestra en pantalla y otro que esta oculto y posee
todos los valores del tablero.
 En ranking se muestran los "usuarios" None, representan espacios vacios que se han de llenar con las partidas.
 El nombre de jugador, al momento de cargar partida, no importa como lo escribas, puedes ignorar mayusculas y minisculas


Para programar se ocupo python 3.10 y el IDE Pycharm.

Los comentarios hechos con el signo " # " son solo para el alumno, sirven de pequeñas notas o ideas
que podrian llegar a ser utiles al momento de revisar pero no nescesariamente, todas las funciones
tienen una definicion que busca explicar su funcionamiento general, estas estan hechas con el proposito
de facilitar la correcion del trabajo

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Menú de Inicio
##### ✅ Funcionalidades		
##### ✅ Puntajes
#### Flujo del Juego (30pts) (36%) 
##### ✅ Menú de Juego
##### ✅ Tablero		
##### ✅ Bestias	
##### ✅ Guardado de partida		
#### Término del Juego 14pts (17%)
##### ✅Fin del juego	
##### ✅ Puntajes	
#### Genera: 15 pts (15%)
##### ✅ Menús
##### ✅ Parámetros
##### 🟠 PEP-8
#### Bonus: 3 décimas
##### ❌ 
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. 
Se deben descargar todos los modulos (functions, main, menu_handler, parametros y tablero) y las carpetas 
tiles (junto con los archivos en su interior), la carpeta rankings y la carpeta saved (esta solo posee el archivo .gitkeep)
Todo esto ha de estar dentro de una carpeta principal, en este caso T0.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: para acceder a los elementos al interior de carpetas
2. ```random```: ```randint``` se obtiene para definir la posicion de las bestias Nexus



### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```functions```: Contiene a las funciones principales del codigo, tambien guarda a la clase Jugador
2. ```menu_handler```: "sub_modulo" de ```functions``` se encarga de administrar la mayoria de los viaje entre menus.
3. ```ranking```: contiene todas las funciones nescesarias para mostrar, actualizar y armar el ranking
4.  ```tablero_handler```: contiene las funciones principales para trabajar en los tablero, construye tableros, los carga y se encarga de validar los input de posiciones

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. se puede usar volver solo en la parte de menus, no en el proceso de juego.
2. Los jugadores solo introduciran valores que aparecen en los menus.
3. Ganar no elimina la partida del jugador.
4. El nombre del jugador no introducira elementos que intervieran con el codigo, sin embargo se han tomados medidas, en menu_handler
5. el jugador ha ganado, cuando las casillas que le faltan por revelar son las mismas que 
        el numero de bestias Nexus

-------



## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. "https://es.stackoverflow.com/questions/144517/python-abrir-archivo-txt-en-carpeta-distinta" acceso a archivos dentro de otras carpetas
2. "https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/gitkeep-push-empty-folders-git-commit" como usar .gitkeep



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
