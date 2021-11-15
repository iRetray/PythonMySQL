class empleados:
    #Constructor
    def init(self, idempleado,nombre,direccion,telefono,cargo, alojamiento):
        self.idempleado = idempleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.cargo = cargo
        self.alojamiento = alojamiento

    #Modificadores
    def setalojamiento (self,idalojamiento_new):
        self.idalojamiento = idalojamiento_new
    def setNombre(self,nombre_new):
        self.nombre = nombre_new
    def setdireccion (self, direccion_new):
        self.direccion = direccion_new
    def settelefono (self, telefono_new):
        self.telefono = telefono_new
    def setempleado (self,idempleado_new):
        self.idempleado = idempleado_new
    def setcargo (self,cargo_new):
        self.cargo = cargo_new

    #Analizadores
    def getidalojaiento(self):
        return (self.idalojamiento)
    def getNombre (self):
        return (self.nombre)
    def getdireccion(self):
        return (self.direccion)
    def gettelefono (self):
        return (self.telefono)
    def getnum_idempleado(self):
        return (self.idempleado)
    def getcargo(self):
        return (self.cargo)
    #Ver objeto
    def verempleados(self):
        print(self.idalojamiento, " - ",self.nombre, " - ", self.direccion, " - ", self.telefono,"-",self.idempleado,"",self.cargo)