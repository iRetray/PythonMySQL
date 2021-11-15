class huespedes:
    #Constructor
    def __init__(self, idhuesped,nombre,direccion,telefono,origen):
        self.idhuesped = idhuesped
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.origen = origen


    #Modificadores
    def setidhuesped (self,idhuesped_new):
        self.idhuesped = idhuesped_new
    def setnombre(self,nombre_new):
        self.nombre = nombre_new
    def setdireccion (self, direccion_new):
        self.direccion = direccion_new
    def settelefono (self, telefono_new):
        self.telefono = telefono_new
    def setorigen (self, origen_new):
        self.origen = origen_new

    #Analizadores
    def getidhuesped(self):
        return (self.idhuesped)
    def getnombre (self):
        return (self.nombre)
    def getdireccion(self):
        return (self.direccion)
    def gettelefono (self):
        return (self.telefono)
    def getorigen (self):
        return (self.origen)

    #Ver objeto
    def verAlumno(self):
        print(self.idhuesped, " - ",self.nombre, " - ", self.direccion, " - ", self.telefono,"-", self.origen)