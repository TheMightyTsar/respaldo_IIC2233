# Tarea 3: DCCard-Jitsu 🐧🥋

La estructura y codigo de la tarea se ven influenciados por la AF3.

Cliente:

La apliacion que ejecuta el cliente es dependiente de uic, que permite ejecutar archivos ui de QTDesigner.
Frontend y Backend se encuentran implementadas en sus carpetas respectivas, las conexiones y la isntancia
de la APP se realizan en ```DCCCardJitsu.py```. El codigo se ejcuta desde ```main.py```

Servidor:

 El codigo se ejcuta desde ```main.py```, la estructura del servidor sigue a la presentada en la AF3, 
los usuarios son capaces de conectarse a el
## Consideraciones generales :octocat:



### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Networking: 26 pts (19%)
##### 🟠 Protocolo	
##### 🟠 Correcto uso de sockets		
##### 🟠 Conexión	
##### 🟠 Manejo de Clientes	
##### ❌✅🟠 Desconexión Repentina
#### Arquitectura Cliente - Servidor: 31 pts (23%)			
##### ✅ Roles			
##### 🟠 Consistencia		
##### 🟠 Logs
#### Manejo de Bytes: 27 pts (20%)
##### ❌✅🟠 Codificación			
##### ❌✅🟠 Decodificación			
##### ❌✅🟠 Encriptación		
##### ❌✅🟠 Desencriptación	
##### ❌✅🟠 Integración
#### Interfaz Gráfica: 27 pts (20%)	
##### ✅ Ventana inicio		
##### ✅ Sala de Espera			
##### ✅ Ventana de juego							
##### ✅ Ventana final
#### Reglas de DCCard-Jitsu: 17 pts (13%)
##### ❌✅🟠 Inicio del juego			
##### ❌✅🟠 Ronda				
##### ❌✅🟠 Termino del juego
#### Archivos: 8 pts (6%)
##### ✅ Parámetros (JSON)		
##### ✅ Cartas.py	
##### ❌✅🟠 Cripto.py
#### Bonus: 8 décimas máximo
##### ❌✅🟠 Cheatcodes	
##### ❌✅🟠 Bienestar	
##### ❌✅🟠 Chat

## Ejecución :computer:
Los módulos principales de la tarea a ejecutar son los archivos  ```main.py``` en las carpetas cliente y servidor.
1. ```archivo.ext``` en ```ubicación```
2. ```directorio``` en ```ubicación```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: señales, uic y qobjects principalmente
2. ```os```: reconocer manejo de carpetas por conflictos al buscar  ```parametros.json```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```jsonManager```: Contiene a ```data_json``` permite abrir el archivo ```parametros.json```
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. En la Ventana de Inicio la confirmacion/ingreso a la ventana de espera se hace por un boton y no la puerta (se presentan ambas opciones en el enunciado)
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------

## Referencias de código externo :book:




## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
