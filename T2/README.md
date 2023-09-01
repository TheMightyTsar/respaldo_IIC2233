# Tarea 2: DCCruz vs Zombies :zombie::seedling::sunflower:


Se intento comentar lo mas posible cosas poco claras, todos los comentarios son utiles
los cuales se encuntran tras un # son principalmente dirigidos al alumno.

```main.py``` es el archivo a ejecutar para iniciar el juego.

Se ocupo Python 3.10 y el IDE Pycharm.

Se trabaja con la logica de Frontend y Backend.

Se sigue una estructura similar a la presentada en la actividad Sumativa 3.

La mayoria de las señales son snake_case y las funciones a las que se conectan estan en camelCase, usualmente ocupan el mismo nombre.

El Frontend y el backen de los elementos del juego, esta otorgado por una version "logica" que hereda de QObject y una
version visual QLabel, se encuentran en logic y ventana respectivamente, la realacion entre objetos esta otorgada por
un ID string con el que puedo encontrar los objetos dentro de diccionarios.

El juego tiene un "reloj" interno (Ticker, ya que emite ticks badum pstt), esta logica es administrada por ```Backend/zaWarudo.py```.

Como se 'reinicia' la ventana de juego por cada ronda, la logica guarda los datos nescesarios, 
numero de ronda y el escenario/ambiente/clima escogido.

Los zombies se crean al inicio, una cantdiad que se encuentra definida en ```parametros```. 

Las plantas, sus balas, soles y la pala se encuentran definidos en ```Backend/plantas```.

Las casillas sirven de "Frontend" para las plantas.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Ventanas: 39 pts (40%)
##### ✅ Ventana de Inicio
##### ✅ Ventana de Ranking	
##### ✅ Ventana principal
##### ✅ Ventana de juego	
##### ✅ Ventana post-ronda
#### Mecánicas de juego: 46 pts (47%)			
##### ✅ Plantas
##### ✅ Zombies
##### ✅ Escenarios		
##### ✅ Fin de ronda	
##### ✅Fin de juego	
#### Interacción con el usuario: 22 pts (23%)
##### ✅ Clicks	
##### ✅ Animaciones
#### Cheatcodes: 8 pts (8%)
Se aprietan las teclas al mismo tiempo (Deben estar en mayusculas)
#####  ✅Pausa
##### ✅ S + U + N
##### ✅ K + I + L
#### Archivos: 4 pts (4%)
##### ✅ Sprites
##### ✅ Parametros.py
#### Bonus: 9 décimas máximo
##### ❌ Crazy Cruz Dinámico
##### ✅ Pala
##### ✅ Drag and Drop Tienda
##### ❌ Música juego

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe copiar en su totalidad los archivos 
presentes en el repositorio. las carpetas y elementos escenciales son:
1. ```ui_files``` en ```Frontend```
2. la carpetas ```sprites``` y ```sonidos``` se deben ingresar a la carpeta ```Frontend```
3. ```aparicion_zombies.py``` y ```puntajes.txt``` se encuentran dentro de ```T2``` en ninguna subcarpeta

Puedes checkear con la distribucion que poseo (https://drive.google.com/file/d/1-GgRoBNj5apX8w47YswKVKja0p4czqOs/view?usp=sharing)
## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```argv``` y ```exit()```
2. ```PyQt5```: ```uic```,  ```QtCore```, ```QtGui```, ```QtWidget```
3. ```os```: ```path.join()```
4. ```random```: se ocupa ```randint``` y ```choice```

### Librerías propias
Por otro lado, los módulos principales que fueron creados fueron los siguientes:

1. ```parametros.py```: Contiene todos los valores constantes/variables que se usan en el juego.
2. ```dccruz.py```: Contiene la clase DCCruz, que hereda de QApplication. establece las conexiones entre señales.
3. ```zaWarudo.py```: Administra la señal tick, lo que permite que el juego corra.
4. ```mouse.py```: junto con la ventana de Juego trabajan el drag and drop
5. ```soles.py```: contiene a las clases de los soles
6. ```zombies.py```: contiene a los zombies
7. El resto es mas descriptivo, logic es backend y ventana frontend

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Una vez se bugearon los zombies y no comian, no volvio a pasar y no se que desencadeno ese error.
2. Los cambios de los valores relacionado a los parametros, se justifican a partir de https://github.com/IIC2233/Syllabus/issues/250#issuecomment-1272365931
3. Debido al uso de 'TimeHandler' en zaWarudo.py como reloj interno, el juego corre en mi una medida de tiempo propia,  reavisar TIME_BETWEEN_TICKS en parametros.py
4. En el computador del alumno los botones solo registran el click izquierdo, por lo que mayores ediciones en el codigo con respecto a esto se evitaron
5. El archivo de Texto 'puntajes.txt' tiene al menos 5 usuarios ingresados 
6. Si se juega nuevamente con un nombre de usuario, se reemplazan los datos anteriores
7. Los sprites de zombie Hernan caminado tienen distintos tamaños, por eso su modificaciones de tamaño cuando camina.
8. Se tomaron flexibilidad en cuanto el movimiento de los zombies, para hacerlo mas fluidos y dinamicos.
**( la razon de velocidad de 1.5/1 se mantiene )**  al igual que la cantidad fija de zombies por linea, se le dio aleatoridad para que sea mas dinamico


 


-------





## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://doc.qt.io/qtforpython-5 no extraccion de xodigo directo pero se observo codigo no visto en los contenidos
2. https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/ porque se hizo el arreglo "extraño" 
al implementar los UIC, (saber la logica detras y no solo copiar de AS3)
3. https://www.geeksforgeeks.org/deletelater-method-in-pyqt5/ porque el .deleteLater()?


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
