class habitaciones:
    #Constructor
    def init(self, idhabitacion,tipo,reg_tempe,precio,keeper, alojamiento):
        self.idhabitacion = idhabitacion
        self.tipo = tipo
        self.reg_tempe = reg_tempe
        self.precio = precio
        self.keeper = keeper
        self.alojamiento = alojamiento

    #Modificadores
    def setalojamiento (self,idalojamiento_new):
        self.idalojamiento = idalojamiento_new
    def sethabitacion(self,idhabitacion_new):
        self.idhabitacion = idhabitacion_new
    def settipo (self, tipo_new):
        self.tipo = tipo_new
    def setreg_tempe (self, reg_tempe_new):
        self.reg_tempe = reg_tempe_new
    def setprecio (self,precio_new):
        self.precio = precio_new
    def setkeeper (self,keeper_new):
        self.keeper = keeper_new

    #Analizadores
    def getidalojaiento(self):
        return (self.idalojamiento)
    def getidhabitacion (self):
        return (self.idhabitacion)
    def gettipo(self):
        return (self.tipo)
    def getreg_tempe (self):
        return (self.reg_tempe)
    def getprecio(self):
        return (self.precio)
    def getkeeper(self):
        return (self.keeper)
    #Ver objeto
    def verhabitaciones(self):
        print(self.idalojamiento, " - ",self.idhabitacion, " - ", self.tipo, " - ", self.reg_tempe,"-",self.precio,"-",self.keeper)