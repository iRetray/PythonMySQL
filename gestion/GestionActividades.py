import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem

from control.conexion import Conexion
from modelo.actividades import actividades
from Ventanas.actividades import Ui_MainWindow

class GestionEstudiantes (QMainWindow):
    def __init__ (self):

        super(GestionEstudiantes, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.objConexion = Conexion ()
        self.miConexion = self.objConexion.conectar()
        print("Objeto tipo GestionEstudiantes creado")
        self.ui.BbuscarActividades.clicked.connect(self.BuscarActividad)
        self.ui.BeliminarActividades.clicked.connect(self.EliminarActividad)
        self.ui.BmodificarActividades.clicked.connect(self.modificarActividad)
        self.ui.BSalirActividades.clicked.connect(self.SalirActividades)
        self.ui.BAgregarActividades.clicked.connect(self.AgregarActividades)


    def SalirActividades(self):
        self.objConexion.desconectar()
        self.close()

    def BuscarActividad(self):
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc("allActividades")

            fila = 0
            x = self.ui.BbuscarActividades.rowCount()
            for rep in range(x):
                self.ui.BbuscarActividades.removeRow(0)

            for result in mycursor.stored_results():
                for (idactividad, nombre, descripcion , dificultad , coordinador) in result:
                    self.ui.BbuscarActividades.insertRow(fila)
                    celdaidactividad = QTableWidgetItem(idactividad)
                    celdaNombre = QTableWidgetItem(nombre)
                    celdadescripcion = QTableWidgetItem(descripcion)
                    celdadificultad = QTableWidgetItem(dificultad)
                    celdacoordinador = QTableWidgetItem(coordinador)


                    self.ui.BbuscarActividades.setItem(fila, 0, celdaidactividad)
                    self.ui.BbuscarActividades.setItem(fila, 1, celdaNombre)
                    self.ui.BbuscarActividades.setItem(fila, 2, celdadescripcion)
                    self.ui.BbuscarActividades.setItem(fila, 3, celdadificultad)
                    self.ui.BbuscarActividades.setItem(fila, 4, celdacoordinador)

                    fila = fila + 1
            mycursor.close()

        except Exception as ex:
            ex_st = str(ex)
            QMessageBox.information(self, "Fallo ejecutando el procedimiento", ex_st, QMessageBox.Ok)

    def verEstudiante(self):
        try:
            mycursor = self.miConexion.cursor()
            id = self.ui.SCodigoV.value()
            band=0
            mycursor.callproc("getEstudiantexid", [id])

            fila = 0
            x = self.ui.TBBuscar.rowCount()
            for rep in range(x):
                self.ui.TBBuscar.removeRow(0)

            for result in mycursor.stored_results():
                for (id, nombre, apellido, investigación) in result:
                    self.ui.TBBuscar.insertRow(fila)
                    celdaCodigo = QTableWidgetItem(str(id))
                    celdaNombre = QTableWidgetItem(nombre)
                    celdaApellido = QTableWidgetItem(apellido)
                    celdaInvestigacion = QTableWidgetItem(str(investigación))

                    self.ui.TBBuscar.setItem(fila, 0, celdaCodigo)
                    self.ui.TBBuscar.setItem(fila, 1, celdaNombre)
                    self.ui.TBBuscar.setItem(fila, 2, celdaApellido)
                    self.ui.TBBuscar.setItem(fila, 3, celdaInvestigacion)
                    band=1
            if band == 0:
                mensaje = "NO EXISTE ESTUDIANTE CON ID " + str(id)
                QMessageBox.information(self, "Error", mensaje, QMessageBox.Ok)
            mycursor.close()

        except Exception as ex:
            ex_st = str(ex)
            QMessageBox.information(self, "Fallo ejecutando el procedimiento", ex_st, QMessageBox.Ok)

    def agregarEstudiante (self):
        try:
            if self.ui.TNombre.text() != "" and self.ui.TApellido.text() != "":
                mycursor =self.miConexion.cursor()
                code = self.ui.SCodigoN.value()
                nombre = self.ui.TNombre.text()
                apellido = self.ui.TApellido.text()
                investigación = self.ui.SInvestigacion.value()

                mycursor.callproc("newEstudiante",[code,nombre,apellido,investigación])
                self.miConexion.commit()
                QMessageBox.information(self, "Información", "EL ESTUDIANTE HA SIDO CREADO", QMessageBox.Ok)

                mycursor.close
            else:
                QMessageBox.information(self, "Error", "¡¡¡FALTAN DATOS!!!", QMessageBox.Ok)

        except Exception as ex:
            ex_st = str(ex)
            QMessageBox.information(self, "Fallo ejecutando el procedimiento", ex_st, QMessageBox.Ok)

    def modificarEstudiante(self):
        try:
            if self.ui.TNombre.text() != "" and self.ui.TApellido.text() != "":
                mycursor = self.miConexion.cursor()
                idviejo = self.ui.SCodigoV.value()
                band = 0
                mycursor.callproc("getEstudiantexid", [idviejo])

                for result in mycursor.stored_results():
                    for (idviejo, nombre, apellido, investigación) in result:
                        band = 1
                if band ==1:
                    code = self.ui.SCodigoN.value()
                    nombre = self.ui.TNombre.text()
                    apellido = self.ui.TApellido.text()
                    investigación = self.ui.SInvestigacion.value()

                    mycursor.callproc("modEstudiante",[code,nombre,apellido,investigación, idviejo])
                    self.miConexion.commit()
                    QMessageBox.information(self, "Información", "EL ESTUDIANTE HA SIDO MODIFICADO", QMessageBox.Ok)

                else:
                    mensaje = "NO EXISTE ESTUDIANTE CON ID " + str(idviejo) + " POR LO QUE NO SE PUEDE MODIFICAR"
                    QMessageBox.information(self, "Error", mensaje, QMessageBox.Ok)
                mycursor.close
            else:
                QMessageBox.information(self, "Error", "¡¡¡FALTAN DATOS!!!", QMessageBox.Ok)

        except Exception as ex:
            ex_st = str(ex)
            QMessageBox.information(self, "Fallo ejecutando el procedimiento", ex_st, QMessageBox.Ok)

    def eliminarEstudiante(self):
        try:
            mycursor = self.miConexion.cursor()
            id = self.ui.SCodigoV.value()
            band = 0
            mycursor.callproc("getEstudiantexid", [id])

            for result in mycursor.stored_results():
                for (id, nombre, apellido, investigación) in result:
                    band = 1
            if band == 1:
                mycursor.callproc("delEstudiante", [id])
                self.miConexion.commit()
                QMessageBox.information(self, "Información", "EL ESTUDIANTE HA SIDO ELIMINADO", QMessageBox.Ok)
            else:
                mensaje = "NO EXISTE ESTUDIANTE CON ID " + str(id) + " POR LO QUE NO SE PUEDE ELIMINAR"
                QMessageBox.information(self, "Error", mensaje, QMessageBox.Ok)
            mycursor.close

        except Exception as ex:
            ex_st = str(ex)
            QMessageBox.information(self, "Fallo ejecutando el procedimiento", ex_st, QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vF = GestionEstudiantes()
    vF.show()
    sys.exit(app.exec_())