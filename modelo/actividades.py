class actividades:
    #Constructor
    def __init__(self, idactividad,nombre,descripcion,dificultad,coordinador):
        self.idactividad = idactividad
        self.nombre = nombre
        self.descripcion = descripcion
        self.dificultad = dificultad
        self.coordinador = coordinador

    #Modificadores
    def setidactividad (self,idactividad_new):
        self.idactividad = idactividad_new
    def setNombre(self,nombre_new):
        self.nombre = nombre_new
    def setdescripcion (self, descripcion_new):
        self.descripcion = descripcion_new
    def setdificultad (self, dificultad_new):
        self.dificultad = dificultad_new
    def setcoordinador (self,coordinador_new):
        self.coordinador = coordinador_new

    #Analizadores
    def getidactividad(self):
        return (self.idactividad)
    def getNombre (self):
        return (self.nombre)
    def getdescripcion(self):
        return (self.descripcion)
    def getdificultad (self):
        return (self.dificultad)
    def getcoordinador(self):
        return (self.coordinador)

    #Ver objeto
    def verAlumno(self):
        print(self.idactividad, " - ",self.nombre, " - ", self.descripcion, " - ", self.dificultad,"-",self.coordinador)


    def BAgregarActividades(self):
        print("El boton se ha clikeado")