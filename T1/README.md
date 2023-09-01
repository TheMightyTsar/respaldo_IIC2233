# Tarea 1: DCCampeonato 🏃‍♂️🏆

Utilizando OOP se creo el juego, el torneo, los entrenadores y los programones.
 Cuando se inicializa la instancia de MainGame se inicia todas las instancias del
resto de objetos, gracias a esto se ejecuta el "reinicio" del programa si asi lo 
decide el usuario.

Gran parte del juego esta determinada según en que escena/menu nos encontremos, defina la validez de los input,
cual sera el menu a mostrar etc.

La logica y el funcionamiento del juego depende de MainGame.scene, esta variable
determina el funcionamiento del juego, nos indica en que menu estamos y todo
eso determina como responde el resto del codigo.


## Consideraciones generales :octocat:
Hay variables, destinadas a crear objetos, que estan "hardcodeadas" en accion_escena() en clases.py
por alguna razon el usar random en parametros.py en variables fijas evita que cambie su valor,
como al estar en un metodo si cambia se ingresaron alli.



### Cosas implementadas y no implementadas :white_check_mark: :x:


#### Programación Orientada a Objetos (18pts) (22%%)
##### 🟠 Diagrama
##### ✅ Definición de clases, atributos, métodos y properties		
##### ✅ Relaciones entre clases
#### Preparación programa: 11 pts (7%)			
##### ✅ Creación de partidas
#### Entidades: 28 pts (19%)
##### ✅ Programón
se encuentra en programones_clases.py
##### ✅ Entrenador		
hay N entrenadores, el jugador es el mismo objeto y se encuentra en MainGame
##### ✅ Liga	
en MainGame es DCCampeonato, clase Torneo, en clases.py
##### ✅ Objetos		
en clases.py
#### Interacción Usuario-Programa 57 pts (38%)
los menu estan manejados principalmente por scene_handler.py
y por metodos de la clase MainGame
su texto, esta en archivos de textp en la carpeta escenas
##### ✅ General	
##### ✅ Menú de Inicio
##### ✅ Menú Entrenador
##### ✅ Menu Entrenamiento

##### ✅ Simulación ronda campeonato
##### ✅ Ver estado del campeonato
##### ✅ Menú crear objeto: 
Existe el menu, no se implemento la mecanica
##### ✅ Menú utilizar objeto
##### ✅ Ver estado del entrenador
el texto no se encunetra alineado
##### ✅ Robustez
#### Manejo de archivos: 12 pts (8%)
##### ✅ Archivos CSV
se trabaja en CSV_extractor.py
##### ✅ Parámetros
#### Bonus: 5 décimas
##### ❌ Mega Evolución
##### ❌ CSV dinámico

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` 
una vez iniciado el codigo corre por su cuenta



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint()```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```clases```: Contiene a las clases del juego, más informacion en los comentarios del archivo
2. ```CSV_extractor```: Hecha para extraer info de los archivos CSV y dejarlos como listas
3. ```programones_clases```: maneja las clases de programones
4. ```parametros```: contiene las variables (constantes) principales del codigo
5. ```scene_handler```: maneja lo relacionado con las escenas e inputs (dependen de las escenas)

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Mejora-post ronda (sobrevivir ronda), todos los programones de los entrenadores que pasen a la siguiente ronda se
veran mejorados según su tipo. de esta manera no es obligatorio jugar un OTP (One Trick Pony)
2. Tras cada ronda la energia se restaura
3. Volver al menu principal reinicia la simulacion
4. Hay informacion que aparece en pantalla y no nescesariamente en Menus


PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
