
import sys
from servidor import server
from servidor.jsonManager import data_json

if __name__ == "__main__":
    HOST = data_json("HOST")
    PORT = data_json("PORT")
    servidor = server.servidor(HOST, PORT)

