import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from gestion.GestionActividades import GestionActividades
from gestion.GestionAlojamientos import GestionEvaluaciones
from gestion.GestionCronogramas import GestionInvestigaciones
from gestion.GestionEmpleados import GestionProfesores
from gestion.GestionHabitaciones import GestionPublicaciones
from gestion.GestionHuespedes import GestionResultados
from gestion.GestionRegistro import GestionTemas
from Ventanas.Menu import Ui_MainWindow

class Entrada(QMainWindow):
    def __init__(self):

        super(Entrada, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Bactividades.clicked.connect(self.actividades)
        self.ui.Balojamientos.clicked.connect(self.alojamientos)
        self.ui.Bcronogramas.clicked.connect(self.cronogramas)
        self.ui.Bempleados.clicked.connect(self.empleados)
        self.ui.Bhabitaciones.clicked.connect(self.habitaciones)
        self.ui.Bhuespedes.clicked.connect(self.huespedes)
        self.ui.Binscripciones.clicked.connect(self.inscripciones)
        self.ui.Bregistro.clicked.connect(self.registro)
        self.ui.Bsalir.clicked.connect(self.salir)

    def actividades(self):
        self.ventanaE = GestionActividades()
        self.ventanaE.show()

    def alojamientos(self):
        self.ventanaP = Gestionalojamientos
        self.ventanaP.show()

    def Evaluaciones(self):
        self.ventanaEva = GestionCronogramas()
        self.ventanaEva.show()

    def Investigaciones(self):
        self.ventanaI = GestionEmpleados()
        self.ventanaI.show()

    def Publicaciones(self):
        self.ventana2 = GestionHabitaciones()
        self.ventana2.show()

    def Temas(self):
        self.ventana2 = GestionHuespedes()
        self.ventana2.show()

    def Resultados(self):
        self.ventana2 = GestionInscripciones()
        self.ventana2.show()

    def Consultas(self):
        self.ventana2 = GestionRegistro()
        self.ventana2.show()

    def Salir(self):
        QMessageBox.information(self, "Despedida", "Hasta luego!")
        self.objConexion.desconectar()
        self.close()

if __name__ == "__main__":
    app =QApplication(sys.argv)
    vP =Entrada()
    vP.show()
    sys.exit(app.exec_())

Entrada()