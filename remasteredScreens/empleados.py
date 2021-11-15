from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


def connect():
    connection = pymysql.connect(
        host="localhost", port=3306, user="root", password="", db="basealojamientos(pf)"
    )
    print("Database is Connected!")
    return connection


class Ui_MainWindow(object):

    def addEmploye(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL newempleado("+self.inputID.text() + \
            ",'"+self.inputName.text()+"','"+self.inputDirection.text() + \
            "','"+self.inputPhone.text()+"', NULL, '"+self.inputCharge.text()+"')"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure newempleado")

    def searchByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL getempleadosxid("+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        objects = myCursor.fetchall()
        print(objects)
        myConnection.commit()
        self.tableEmployes.setRowCount(0)
        for row_number, row_data in enumerate(objects):
            self.tableEmployes.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableEmployes.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        print("Finished SQL Procedure getempleadosxid")

    def deleteByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL delempleados("+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure delempleados")

    def modifyByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL modempleado("+self.inputID.text() + \
            ",'"+self.inputName.text()+"','"+self.inputDirection.text() + \
            "','"+self.inputPhone.text()+"', NULL, '"+self.inputCharge.text() + \
            "', "+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure modempleado")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 681, 531))
        self.frame_3.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 661, 481))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.widget_23 = QtWidgets.QWidget(self.frame_6)
        self.widget_23.setGeometry(QtCore.QRect(-1, 0, 161, 16))
        self.widget_23.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_23.setObjectName("widget_23")
        self.widget_24 = QtWidgets.QWidget(self.frame_6)
        self.widget_24.setGeometry(QtCore.QRect(0, 10, 16, 471))
        self.widget_24.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_24.setObjectName("widget_24")
        self.widget_25 = QtWidgets.QWidget(self.frame_6)
        self.widget_25.setGeometry(QtCore.QRect(520, 0, 141, 16))
        self.widget_25.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_25.setObjectName("widget_25")
        self.widget_26 = QtWidgets.QWidget(self.frame_6)
        self.widget_26.setGeometry(QtCore.QRect(645, 10, 16, 471))
        self.widget_26.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_26.setObjectName("widget_26")
        self.widget_27 = QtWidgets.QWidget(self.frame_6)
        self.widget_27.setGeometry(QtCore.QRect(10, 470, 641, 16))
        self.widget_27.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_27.setObjectName("widget_27")
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        self.label_16.setGeometry(QtCore.QRect(240, 70, 201, 20))
        self.label_16.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                    "background-color: rgb(85, 255, 127);\n"
                                    "background-color: rgb(85, 170, 127);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        self.label_17.setGeometry(QtCore.QRect(170, 250, 361, 20))
        self.label_17.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                    "background-color: rgb(85, 170, 127);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_6)
        self.label_18.setGeometry(QtCore.QRect(30, 280, 20, 20))
        self.label_18.setObjectName("label_18")
        self.inputSearchID = QtWidgets.QLineEdit(self.frame_6)
        self.inputSearchID.setGeometry(QtCore.QRect(60, 280, 113, 20))
        self.inputSearchID.setObjectName("inputSearchID")
        self.buttonSearch = QtWidgets.QPushButton(self.frame_6)
        self.buttonSearch.setGeometry(QtCore.QRect(210, 280, 81, 21))
        self.buttonSearch.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(85, 170, 127);")
        self.buttonSearch.setObjectName("buttonSearch")
        self.buttonDelete = QtWidgets.QPushButton(self.frame_6)
        self.buttonDelete.setGeometry(QtCore.QRect(360, 280, 75, 23))
        self.buttonDelete.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(85, 170, 127);")
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonModify = QtWidgets.QPushButton(self.frame_6)
        self.buttonModify.setGeometry(QtCore.QRect(490, 280, 75, 23))
        self.buttonModify.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(85, 170, 127);")
        self.buttonModify.setObjectName("buttonModify")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.frame_6)
        self.textBrowser_4.setGeometry(QtCore.QRect(160, 0, 361, 71))
        self.textBrowser_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_43 = QtWidgets.QLabel(self.frame_6)
        self.label_43.setGeometry(QtCore.QRect(70, 120, 21, 16))
        self.label_43.setObjectName("label_43")
        self.inputID = QtWidgets.QLineEdit(self.frame_6)
        self.inputID.setGeometry(QtCore.QRect(70, 140, 131, 31))
        self.inputID.setObjectName("inputID")
        self.label_44 = QtWidgets.QLabel(self.frame_6)
        self.label_44.setGeometry(QtCore.QRect(240, 120, 47, 13))
        self.label_44.setObjectName("label_44")
        self.inputName = QtWidgets.QLineEdit(self.frame_6)
        self.inputName.setGeometry(QtCore.QRect(240, 140, 171, 31))
        self.inputName.setObjectName("inputName")
        self.label_45 = QtWidgets.QLabel(self.frame_6)
        self.label_45.setGeometry(QtCore.QRect(460, 120, 71, 16))
        self.label_45.setObjectName("label_45")
        self.inputDirection = QtWidgets.QLineEdit(self.frame_6)
        self.inputDirection.setGeometry(QtCore.QRect(450, 140, 171, 31))
        self.inputDirection.setObjectName("inputDirection")
        self.label_46 = QtWidgets.QLabel(self.frame_6)
        self.label_46.setGeometry(QtCore.QRect(70, 190, 61, 16))
        self.label_46.setObjectName("label_46")
        self.inputPhone = QtWidgets.QLineEdit(self.frame_6)
        self.inputPhone.setGeometry(QtCore.QRect(70, 210, 131, 31))
        self.inputPhone.setObjectName("inputPhone")
        self.label_47 = QtWidgets.QLabel(self.frame_6)
        self.label_47.setGeometry(QtCore.QRect(240, 190, 47, 13))
        self.label_47.setObjectName("label_47")
        self.inputCharge = QtWidgets.QLineEdit(self.frame_6)
        self.inputCharge.setGeometry(QtCore.QRect(240, 210, 171, 31))
        self.inputCharge.setObjectName("inputCharge")
        self.label_48 = QtWidgets.QLabel(self.frame_6)
        self.label_48.setGeometry(QtCore.QRect(450, 190, 81, 16))
        self.label_48.setObjectName("label_48")
        self.inputPLace = QtWidgets.QLineEdit(self.frame_6)
        self.inputPLace.setGeometry(QtCore.QRect(450, 210, 171, 31))
        self.inputPLace.setObjectName("inputPLace")
        self.buttonAdd = QtWidgets.QPushButton(self.frame_6)
        self.buttonAdd.setGeometry(QtCore.QRect(560, 250, 75, 23))
        self.buttonAdd.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.buttonAdd.setObjectName("buttonAdd")
        self.tableEmployes = QtWidgets.QTableWidget(self.frame_6)
        self.tableEmployes.setGeometry(QtCore.QRect(20, 310, 621, 151))
        self.tableEmployes.setObjectName("tableEmployes")
        self.tableEmployes.setColumnCount(6)
        self.tableEmployes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployes.setHorizontalHeaderItem(5, item)
        self.BSalirEmpleados = QtWidgets.QPushButton(self.frame_6)
        self.BSalirEmpleados.setGeometry(QtCore.QRect(50, 40, 75, 23))
        self.BSalirEmpleados.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.BSalirEmpleados.setObjectName("BSalirEmpleados")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_16.setText(_translate(
            "MainWindow", "INGRESE LA SIGUIENTE INFORMACION:"))
        self.label_17.setText(_translate(
            "MainWindow", "INGRESE EL ID PARA BUSCAR,ELIMINAR O MODIFICAR"))
        self.label_18.setText(_translate("MainWindow", "ID:"))
        self.buttonSearch.setText(_translate("MainWindow", "BUSCAR"))
        self.buttonSearch.clicked.connect(self.searchByID)
        self.buttonDelete.setText(_translate("MainWindow", "ELIMINAR"))
        self.buttonDelete.clicked.connect(self.deleteByID)
        self.buttonModify.setText(_translate("MainWindow", "MODIFICAR"))
        self.buttonModify.clicked.connect(self.modifyByID)
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#55aa7f;\">MENU </span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#55aa7f;\">EMPLEADOS </span></p></body></html>"))
        self.label_43.setText(_translate("MainWindow", "ID:"))
        self.label_44.setText(_translate("MainWindow", "NOMBRE:"))
        self.label_45.setText(_translate("MainWindow", "DIRECCION:"))
        self.label_46.setText(_translate("MainWindow", "TELEFONO:"))
        self.label_47.setText(_translate("MainWindow", "CARGO:"))
        self.label_48.setText(_translate("MainWindow", "ALOJAMIENTO:"))
        self.buttonAdd.setText(_translate("MainWindow", "AGREGAR"))
        self.buttonAdd.clicked.connect(self.addEmploye)
        item = self.tableEmployes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableEmployes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableEmployes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Direccion"))
        item = self.tableEmployes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.tableEmployes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cargo"))
        item = self.tableEmployes.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Alojamiento"))
        self.BSalirEmpleados.setText(_translate("MainWindow", "SALIR:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
