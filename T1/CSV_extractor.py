'''
Este modulo trabaja con los archivos CSV y los exportaran como listas de listas
'''


### imports

### codigo

# Entrenadores
def extraer_entrenadores():
    # se abre el archivo
    txt_open = open("entrenadores.csv", "r", encoding="utf-8")
    lista_txt = txt_open.readlines()
    txt_open.close()

    # se trabaja la lista
    sublista = None
    lista_listas = []
    for elem in lista_txt:
        if elem[0:6] != "nombre":

            sublista = (elem.strip("\n")).split(",")
            lista_listas.append(sublista[:])
    return lista_listas


# Programones
def extraer_programones():
    # se abre el archivo
    txt_open = open("programones.csv", "r", encoding="utf-8")
    lista_txt = txt_open.readlines()
    txt_open.close()

    # se trabaja la lista
    sublista = None
    lista_listas = []
    for elem in lista_txt:
        if elem[0:6] != "nombre":

            sublista = (elem.strip("\n")).split(",")
            lista_listas.append(sublista[:])
    return lista_listas


# Evoluciones
def extraer_evoluciones():
    # se abre el archivo
    txt_open = open("evoluciones.csv", "r", encoding="utf-8")
    lista_txt = txt_open.readlines()
    txt_open.close()

    # se trabaja la lista
    sublista = None
    lista_listas = []
    for elem in lista_txt:
        if elem[0:6] != "nombre":

            sublista = (elem.strip("\n")).split(",")
            lista_listas.append(sublista[:])
    return lista_listas


# Objetos
def extraer_objetos():
    # se abre el archivo
    txt_open = open("objetos.csv", "r", encoding="utf-8")
    lista_txt = txt_open.readlines()
    txt_open.close()

    # se trabaja la lista
    sublista = None
    lista_listas = []
    for elem in lista_txt:
        if elem[0:6] != "nombre":

            sublista = (elem.strip("\n")).split(",")
            lista_listas.append(sublista[:])
    return lista_listas

def extraer_bayas():
    bayas = []
    objetos = extraer_objetos()
    for elem in objetos:
        if elem[1] == "baya":
            bayas.append(elem)
    return bayas

def extraer_pocion():
    pocion = []
    objetos = extraer_objetos()
    for elem in objetos:
        if elem[1] == "pocion":
            pocion.append(elem)
    return pocion

def extraer_caramelos():
    caramel = []
    objetos = extraer_objetos()
    for elem in objetos:
        if elem[1] == "caramelo":
            caramel.append(elem)
    return caramel