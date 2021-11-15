from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


def connect():
    connection = pymysql.connect(
        host="localhost", port=3306, user="root", password="", db="basealojamientos(pf)"
    )
    print("Database is Connected!")
    return connection


class Ui_MainWindow(object):

    def addPlace(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL newalojamiento("+self.inputID.text() + \
            ",'"+self.inputName.text()+"','"+self.inputDirection.text() + \
            "','"+self.inputPhone.text()+"','"+self.inputPlace.text() + \
            "', NULL)"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure newalojamiento")

    def searchByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL getalojamientosxid("+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        objects = myCursor.fetchall()
        print(objects)
        myConnection.commit()
        self.tablePlaces.setRowCount(0)
        for row_number, row_data in enumerate(objects):
            self.tablePlaces.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tablePlaces.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        print("Finished SQL Procedure getalojamientosxid")

    def deleteByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL delalojamientos("+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure delalojamientos")

    def modifyByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL modalojamientos("+self.inputID.text() + \
            ",'"+self.inputName.text()+"','"+self.inputDirection.text()+"','"+self.inputPhone.text() + \
            "',"+self.inputPlace.text()+", NULL,"+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure modalojamientos")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 681, 531))
        self.frame_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 661, 481))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.widget_16 = QtWidgets.QWidget(self.frame_5)
        self.widget_16.setGeometry(QtCore.QRect(-1, 0, 16, 481))
        self.widget_16.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_16.setObjectName("widget_16")
        self.widget_17 = QtWidgets.QWidget(self.frame_5)
        self.widget_17.setGeometry(QtCore.QRect(10, 0, 191, 16))
        self.widget_17.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_17.setObjectName("widget_17")
        self.widget_19 = QtWidgets.QWidget(self.frame_5)
        self.widget_19.setGeometry(QtCore.QRect(645, 0, 16, 471))
        self.widget_19.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_19.setObjectName("widget_19")
        self.widget_22 = QtWidgets.QWidget(self.frame_5)
        self.widget_22.setGeometry(QtCore.QRect(450, 0, 201, 16))
        self.widget_22.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_22.setObjectName("widget_22")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(230, 70, 201, 20))
        self.label_19.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                    "background-color: rgb(255, 0, 0);\n"
                                    "background-color: rgb(255, 0, 0);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_5)
        self.label_20.setGeometry(QtCore.QRect(140, 240, 361, 20))
        self.label_20.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                    "background-color: rgb(255, 0, 0);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_5)
        self.label_21.setGeometry(QtCore.QRect(20, 270, 20, 20))
        self.label_21.setObjectName("label_21")
        self.inputSearchID = QtWidgets.QLineEdit(self.frame_5)
        self.inputSearchID.setGeometry(QtCore.QRect(60, 270, 113, 20))
        self.inputSearchID.setObjectName("inputSearchID")
        self.buttonSearch = QtWidgets.QPushButton(self.frame_5)
        self.buttonSearch.setGeometry(QtCore.QRect(200, 270, 81, 21))
        self.buttonSearch.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(255, 0, 0);")
        self.buttonSearch.setObjectName("buttonSearch")
        self.buttonDelete = QtWidgets.QPushButton(self.frame_5)
        self.buttonDelete.setGeometry(QtCore.QRect(310, 270, 75, 23))
        self.buttonDelete.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(255, 0, 0);")
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonModify = QtWidgets.QPushButton(self.frame_5)
        self.buttonModify.setGeometry(QtCore.QRect(420, 270, 75, 23))
        self.buttonModify.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(255, 0, 0);")
        self.buttonModify.setObjectName("buttonModify")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_5)
        self.textBrowser_3.setGeometry(QtCore.QRect(200, 0, 256, 71))
        self.textBrowser_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(50, 110, 47, 13))
        self.label_6.setObjectName("label_6")
        self.inputID = QtWidgets.QLineEdit(self.frame_5)
        self.inputID.setGeometry(QtCore.QRect(50, 130, 131, 31))
        self.inputID.setObjectName("inputID")
        self.label_34 = QtWidgets.QLabel(self.frame_5)
        self.label_34.setGeometry(QtCore.QRect(230, 110, 47, 13))
        self.label_34.setObjectName("label_34")
        self.inputName = QtWidgets.QLineEdit(self.frame_5)
        self.inputName.setGeometry(QtCore.QRect(220, 130, 211, 31))
        self.inputName.setObjectName("inputName")
        self.label_35 = QtWidgets.QLabel(self.frame_5)
        self.label_35.setGeometry(QtCore.QRect(450, 110, 61, 16))
        self.label_35.setObjectName("label_35")
        self.inputDirection = QtWidgets.QLineEdit(self.frame_5)
        self.inputDirection.setGeometry(QtCore.QRect(450, 130, 191, 31))
        self.inputDirection.setObjectName("inputDirection")
        self.label_36 = QtWidgets.QLabel(self.frame_5)
        self.label_36.setGeometry(QtCore.QRect(50, 180, 61, 16))
        self.label_36.setObjectName("label_36")
        self.inputPhone = QtWidgets.QLineEdit(self.frame_5)
        self.inputPhone.setGeometry(QtCore.QRect(50, 200, 131, 31))
        self.inputPhone.setObjectName("inputPhone")
        self.label_37 = QtWidgets.QLabel(self.frame_5)
        self.label_37.setGeometry(QtCore.QRect(230, 180, 131, 16))
        self.label_37.setObjectName("label_37")
        self.inputPlace = QtWidgets.QLineEdit(self.frame_5)
        self.inputPlace.setGeometry(QtCore.QRect(220, 200, 211, 31))
        self.inputPlace.setObjectName("inputPlace")
        self.label_38 = QtWidgets.QLabel(self.frame_5)
        self.label_38.setGeometry(QtCore.QRect(450, 180, 71, 16))
        self.label_38.setObjectName("label_38")
        self.inputContact = QtWidgets.QLineEdit(self.frame_5)
        self.inputContact.setGeometry(QtCore.QRect(450, 200, 191, 31))
        self.inputContact.setObjectName("inputContact")
        self.buttonAdd = QtWidgets.QPushButton(self.frame_5)
        self.buttonAdd.setGeometry(QtCore.QRect(560, 240, 75, 23))
        self.buttonAdd.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.buttonAdd.setObjectName("buttonAdd")
        self.tablePlaces = QtWidgets.QTableWidget(self.frame_5)
        self.tablePlaces.setGeometry(QtCore.QRect(20, 300, 621, 171))
        self.tablePlaces.setObjectName("tablePlaces")
        self.tablePlaces.setColumnCount(6)
        self.tablePlaces.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablePlaces.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablePlaces.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablePlaces.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablePlaces.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablePlaces.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablePlaces.setHorizontalHeaderItem(5, item)
        self.BSalirAlojamientos = QtWidgets.QPushButton(self.frame_5)
        self.BSalirAlojamientos.setGeometry(QtCore.QRect(40, 50, 75, 23))
        self.BSalirAlojamientos.setStyleSheet(
            "background-color: rgb(255, 0, 0);")
        self.BSalirAlojamientos.setObjectName("BSalirAlojamientos")
        self.widget_18 = QtWidgets.QWidget(self.frame_2)
        self.widget_18.setGeometry(QtCore.QRect(20, 480, 651, 16))
        self.widget_18.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_18.setObjectName("widget_18")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_19.setText(_translate(
            "MainWindow", "INGRESE LA SIGUIENTE INFORMACION:"))
        self.label_20.setText(_translate(
            "MainWindow", "INGRESE EL ID PARA BUSCAR,ELIMINAR O MODIFICAR"))
        self.label_21.setText(_translate("MainWindow", "ID:"))
        self.buttonSearch.setText(_translate("MainWindow", "BUSCAR"))
        self.buttonSearch.clicked.connect(self.searchByID)
        self.buttonDelete.setText(_translate("MainWindow", "ELIMINAR"))
        self.buttonDelete.clicked.connect(self.deleteByID)
        self.buttonModify.setText(_translate("MainWindow", "MODIFICAR"))
        self.buttonModify.clicked.connect(self.modifyByID)
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ff0000;\">MENU ALOJAMIENTOS</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "ID:"))
        self.label_34.setText(_translate("MainWindow", "NOMBRE:"))
        self.label_35.setText(_translate("MainWindow", "DIRECCION:"))
        self.label_36.setText(_translate("MainWindow", "TELEFONO:"))
        self.label_37.setText(_translate(
            "MainWindow", "NUMERO DE HABITACION:"))
        self.label_38.setText(_translate("MainWindow", "CONTACTO:"))
        self.buttonAdd.setText(_translate("MainWindow", "AGREGAR"))
        self.buttonAdd.clicked.connect(self.addPlace)
        item = self.tablePlaces.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tablePlaces.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tablePlaces.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Direccion"))
        item = self.tablePlaces.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.tablePlaces.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Numero de habitacion"))
        item = self.tablePlaces.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Contacto"))
        self.BSalirAlojamientos.setText(_translate("MainWindow", "SALIR:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
