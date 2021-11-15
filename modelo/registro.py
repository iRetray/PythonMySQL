class registro:
    #Constructor
    def init(self, habitacion,huesped,fechain,fechaout,cuenta):
        self.habitacion = habitacion
        self.huesped = huesped
        self.fechain = fechain
        self.fechaout = fechaout
        self.cuenta = cuenta

    #Modificadores
    def sethuesped (self,huesped_new):
        self.huesped = huesped_new
    def sethabitacion(self,habitacion_new):
        self.habitacion = habitacion_new
    def setfechain (self, fechain_new):
        self.fechain = fechain_new
    def setfechaout (self, fechaout_new):
        self.fechaout = fechaout_new
    def setcuenta (self,cuenta_new):
        self.cuenta = cuenta_new

    #Analizadores
    def gethuesped(self):
        return (self.huesped)
    def gethabitacion (self):
        return (self.habitacion)
    def getfechain(self):
        return (self.fechain)
    def getfechaout (self):
        return (self.fechaout)
    def getcuenta(self):
        return (self.cuenta)
    #Ver objeto
    def verregistro(self):
        print(self.huesped, " - ",self.habitacion, " - ", self.fechain, " - ", self.fechaout,"-",self.cuenta)