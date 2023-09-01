columnas_letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#usar .rfind() para saber posicion de letra

numeros = "0123456789101112131415"

def nexus_cercanos(tablero):
    '''

    :param tablero:
    :return:

    donde actualiza todos los valores de las casillas de user_tablero
    '''
    tablero_act = tablero[:]

    for largo in range(0, len(tablero)):
        #revisa las filas del tablero

        for ancho in range(0, len(tablero[0])):
            nexus_cerca = 0
                #revisa las columnas de las filas

            if tablero[largo][ancho] != "N":

                if largo == 0:
                    if tablero[largo+1][ancho] == "N":
                        nexus_cerca+=1
                    if ancho != (len(tablero[0])-1):
                        if tablero[largo + 1][ancho+1] == "N":
                            nexus_cerca += 1
                        if tablero[largo][ancho+1] == "N":
                            nexus_cerca += 1
                    if ancho != 0:
                        if tablero[largo][ancho-1] == "N":
                            nexus_cerca += 1
                        if tablero[largo + 1][ancho-1] == "N":
                            nexus_cerca += 1

                elif ancho == 0:
                    if tablero[largo][ancho+1] == "N":
                        nexus_cerca+=1
                    if largo != (len(tablero)-1):
                        if tablero[largo + 1][ancho] == "N":
                            nexus_cerca += 1
                        if tablero[largo + 1][ancho+1] == "N":
                            nexus_cerca += 1
                    if largo != 0:
                        if tablero[largo - 1][ancho] == "N":
                            nexus_cerca += 1
                        if tablero[largo - 1][ancho+1] == "N":
                            nexus_cerca += 1

                elif largo == (len(tablero)-1):
                    if tablero[largo-1][ancho] == "N":
                        nexus_cerca+=1

                    if ancho != (len(tablero[0])-1):
                        if tablero[largo ][ancho+1] == "N":
                            nexus_cerca += 1
                        if tablero[largo - 1][ancho+1] == "N":
                            nexus_cerca += 1
                    if ancho != 0:
                        if tablero[largo - 1][ancho-1] == "N":
                            nexus_cerca += 1
                        if tablero[largo][ancho-1] == "N":
                            nexus_cerca += 1

                elif ancho == (len(tablero[0])-1):
                    if tablero[largo][ancho-1] == "N":
                        nexus_cerca+=1
                    if largo != (len(tablero) - 1):
                        if tablero[largo+1][ancho - 1] == "N":
                            nexus_cerca += 1
                        if tablero[largo+1][ancho] == "N":
                            nexus_cerca += 1

                    if largo != 0:
                        if tablero[largo-1][ancho - 1] == "N":
                            nexus_cerca += 1
                        if tablero[largo-1][ancho] == "N":
                            nexus_cerca += 1

                else:
                    if tablero[largo+1][ancho+1] == "N":
                        nexus_cerca+=1
                    if tablero[largo+1][ancho] == "N":
                        nexus_cerca+=1
                    if tablero[largo+1][ancho-1] == "N":
                        nexus_cerca+=1

                    if tablero[largo][ancho+1] == "N":
                        nexus_cerca+=1
                    if tablero[largo][ancho - 1] == "N":
                        nexus_cerca += 1

                    if tablero[largo-1][ancho-1] == "N":
                        nexus_cerca+=1
                    if tablero[largo-1][ancho] == "N":
                        nexus_cerca+=1
                    if tablero[largo-1][ancho+1] == "N":
                        nexus_cerca+=1
                tablero_act[largo][ancho] = str(nexus_cerca)



    return tablero_act

def valid_posicion(posicion, show_tablero):
    '''
    :param posicion:
    :param show_tablero:
    :return: valid

    valid entregara la posicion entregada por el usuario si el input es valido
    entregara False si no por lo que volvera a pregunar las coordenadas
    '''
    valid = False

    if "," in posicion:

        medidas = posicion.split(",")
        if len(medidas) == 2:


            if (medidas[0] in numeros) and (medidas[1] in columnas_letras):
                if (0 <= int(medidas[0]) < len(show_tablero)) and (0 <= columnas_letras.rfind(medidas[1]) < len(show_tablero[0])):
                    ancho = columnas_letras.rfind(medidas[1])
                    largo = int(medidas[0])
                    if show_tablero[largo][ancho] == " ":
                        valid = [largo, ancho]

    return valid

def load_tablero(nombre):
    '''

    :param nombre:
    :return: tableros

    con el nombre del jugador cargado, busca los archivos y carga sus tableros
    '''
    nombre = nombre.upper()
    tableros = ["", ""]
    nombre_archivo = "saved/" + nombre + "tablero_save.txt"
    open_txt = open(nombre_archivo, "r")
    user_tablero = ((open_txt.readline()).strip("\n")).split(";")
    show_tablero = ((open_txt.readline()).strip("\n")).split(";")

    for i in range(0, len(user_tablero)):
        user_tablero[i] = user_tablero[i].split(",")
        show_tablero[i] = show_tablero[i].split(",")
    tableros = [user_tablero, show_tablero]
    return tableros