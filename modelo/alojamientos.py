class alojamientos:
    #Constructor
    def __init__(self, idalojamiento,nombre,direccion,telefono,num_habitaciones,contacto):
        self.idalojamiento = idalojamiento
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.num_habitaciones = num_habitaciones
        self.contacto = contacto

    #Modificadores
    def setalojamiento (self,idalojamiento_new):
        self.idalojamiento = idalojamiento_new
    def setNombre(self,nombre_new):
        self.nombre = nombre_new
    def setdireccion (self, direccion_new):
        self.direccion = direccion_new
    def settelefono (self, telefono_new):
        self.telefono = telefono_new
    def setnum_habitaciones (self,num_habitaciones_new):
        self.num_habitaciones = num_habitaciones_new
    def setcontacto (self,contacto_new):
        self.contacto = contacto_new

    #Analizadores
    def getidalojaiento(self):
        return (self.idalojamiento)
    def getNombre (self):
        return (self.nombre)
    def getdireccion(self):
        return (self.direccion)
    def gettelefono (self):
        return (self.telefono)
    def getnum_habitaciones(self):
        return (self.num_habitaciones)
    def getcontacto(self):
        return (self.contacto)
    #Ver objeto
    def veralojamiento(self):
        print(self.idalojamiento, " - ",self.nombre, " - ", self.direccion, " - ", self.telefono,"-",self.num_habitaciones,"",self.contacto)