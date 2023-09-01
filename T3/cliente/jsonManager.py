"""
Modulo contiene funciones auxiliares
"""
import json
import os



def data_json(llave):
    """
    Lee parametros.json y retorna el valor del dato con la key correspondiente
    """

    directory = os.getcwd()
    if directory.endswith('cliente'):
        ruta = os.path.join('parametros.json')
    else:
        ruta = os.path.join('../parametros.json')
    with open(ruta, "r", encoding="UTF-8") as archivo:
        diccionario_data = json.load(archivo)
    valor = diccionario_data[llave]
    return valor


def leer_archivo(ruta):
    """
    Lee y devuelve los bytes del archivo en la ruta
    """
    with open(ruta, "rb") as archivo:
        bytes_ = archivo.read()
    return bytes_