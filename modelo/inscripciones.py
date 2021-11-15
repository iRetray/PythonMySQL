class cronogramas:
    #Constructor
    def __init__(self, actividad,alojamiento,huesped):
        self.actividad = actividad
        self.alojamiento = alojamiento
        self.huesped = huesped


    #Modificadores
    def setactividad (self,actividad_new):
        self.actividad = actividad_new
    def setalojamiento(self,alojamiento_new):
        self.alojamiento = alojamiento_new
    def sethuesped (self, huesped_new):
        self.dia = huesped_new



    #Analizadores
    def getactividad(self):
        return (self.actividad)
    def getalojamiento (self):
        return (self.alojamiento)
    def gethuesped(self):
        return (self.huesped)


    #Ver objeto
    def verAlumno(self):
        print(self.actividad, " - ",self.alojamiento, " - ", self.dia, " - ", self.huesped,)