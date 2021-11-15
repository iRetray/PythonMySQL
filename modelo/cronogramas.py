class cronogramas:
    #Constructor
    def __init__(self, actividad,alojamiento,dia,hora):
        self.actividad = actividad
        self.alojamiento = alojamiento
        self.dia = dia
        self.hora = hora


    #Modificadores
    def setactividad (self,actividad_new):
        self.actividad = actividad_new
    def setalojamiento(self,alojamiento_new):
        self.alojamiento = alojamiento_new
    def setdia (self, dia_new):
        self.dia = dia_new
    def sethora (self, hora_new):
        self.hora = hora_new


    #Analizadores
    def getactividad(self):
        return (self.actividad)
    def getalojamiento (self):
        return (self.alojamiento)
    def getdia(self):
        return (self.dia)
    def gethora (self):
        return (self.hora)

    #Ver objeto
    def verAlumno(self):
        print(self.actividad, " - ",self.alojamiento, " - ", self.dia, " - ", self.hora,)