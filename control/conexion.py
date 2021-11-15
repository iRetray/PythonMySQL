import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        conect = None
        print("Objeto tipo Conexion creado...")

    def conectar (self):
        try:
            self.conect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="basealojamiento(pf)")
            if self.conect.is_connected():
                print("Estamos conectados")
                return self.conect
        except Error as error:
            print("Error durante la conexión !!!!")
            print(error)
    def desconectar (self):
        if self.conect.is_connected ():
            self.conect.close()
            print("Conexión cerrada...")