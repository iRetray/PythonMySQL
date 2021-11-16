from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


def connect():
    connection = pymysql.connect(
        host="localhost", port=3306, user="root", password="", db="basealojamientos(pf)"
    )
    print("Database is Connected!")
    return connection


class Ui_MainWindow(object):

    def addRegister(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL newregistro("+self.inputID.text() + \
            ","+self.inputRoom.text()+",'"+self.inputDateIn.text() + \
            "','"+self.inputDateOut.text()+"', '"+self.inputAccount.text()+"')"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure newregistro")

    def searchByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL getregistros("+self.inputSearchID.text() + \
            ", "+self.inputSearchRoom.text()+")"
        print(sql)
        myCursor.execute(sql)
        objects = myCursor.fetchall()
        print(objects)
        myConnection.commit()
        self.tableRegister.setRowCount(0)
        for row_number, row_data in enumerate(objects):
            self.tableRegister.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableRegister.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        print("Finished SQL Procedure getregistros")

    def deleteByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL delregistros("+self.inputSearchID.text() + \
            ", "+self.inputSearchRoom.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure delregistros")

    def modifyByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL modregistro("+self.inputID.text() + \
            ","+self.inputRoom.text()+",'"+self.inputDateIn.text() + \
            "','"+self.inputDateOut.text()+"','"+self.inputAccount.text()+"', " + \
            self.inputSearchRoom.text()+", "+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure modregistro")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_47 = QtWidgets.QWidget(self.centralwidget)
        self.widget_47.setGeometry(QtCore.QRect(10, 0, 681, 531))
        self.widget_47.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                                     "background-color: rgb(170, 85, 255);\n"
                                     "background-color: rgb(170, 85, 255);")
        self.widget_47.setObjectName("widget_47")
        self.widget_48 = QtWidgets.QWidget(self.widget_47)
        self.widget_48.setGeometry(QtCore.QRect(8, 10, 661, 481))
        self.widget_48.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_48.setObjectName("widget_48")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.widget_48)
        self.textBrowser_9.setGeometry(QtCore.QRect(220, -2, 256, 71))
        self.textBrowser_9.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.widget_49 = QtWidgets.QWidget(self.widget_48)
        self.widget_49.setGeometry(QtCore.QRect(0, 0, 221, 16))
        self.widget_49.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_49.setObjectName("widget_49")
        self.widget_50 = QtWidgets.QWidget(self.widget_48)
        self.widget_50.setGeometry(QtCore.QRect(0, 10, 16, 461))
        self.widget_50.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_50.setObjectName("widget_50")
        self.widget_51 = QtWidgets.QWidget(self.widget_48)
        self.widget_51.setGeometry(QtCore.QRect(645, 0, 16, 471))
        self.widget_51.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_51.setObjectName("widget_51")
        self.widget_52 = QtWidgets.QWidget(self.widget_48)
        self.widget_52.setGeometry(QtCore.QRect(470, 0, 181, 16))
        self.widget_52.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_52.setObjectName("widget_52")
        self.widget_53 = QtWidgets.QWidget(self.widget_48)
        self.widget_53.setGeometry(QtCore.QRect(0, 470, 661, 20))
        self.widget_53.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_53.setObjectName("widget_53")
        self.label_31 = QtWidgets.QLabel(self.widget_48)
        self.label_31.setGeometry(QtCore.QRect(170, 250, 361, 20))
        self.label_31.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                    "background-color: rgb(0, 85, 0);\n"
                                    "background-color: rgb(170, 85, 255);")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.widget_48)
        self.label_32.setGeometry(QtCore.QRect(30, 280, 51, 16))
        self.label_32.setObjectName("label_32")
        self.inputSearchID = QtWidgets.QLineEdit(self.widget_48)
        self.inputSearchID.setGeometry(QtCore.QRect(90, 280, 81, 20))
        self.inputSearchID.setObjectName("inputSearchID")
        self.buttonSearch = QtWidgets.QPushButton(self.widget_48)
        self.buttonSearch.setGeometry(QtCore.QRect(380, 280, 81, 21))
        self.buttonSearch.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(0, 85, 0);\n"
                                        "background-color: rgb(170, 85, 255);")
        self.buttonSearch.setObjectName("buttonSearch")
        self.buttonDelete = QtWidgets.QPushButton(self.widget_48)
        self.buttonDelete.setGeometry(QtCore.QRect(470, 280, 75, 23))
        self.buttonDelete.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(0, 85, 0);\n"
                                        "background-color: rgb(170, 85, 255);")
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonModify = QtWidgets.QPushButton(self.widget_48)
        self.buttonModify.setGeometry(QtCore.QRect(560, 280, 75, 23))
        self.buttonModify.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(255, 255, 127);\n"
                                        "background-color: rgb(170, 85, 255);")
        self.buttonModify.setObjectName("buttonModify")
        self.label_33 = QtWidgets.QLabel(self.widget_48)
        self.label_33.setGeometry(QtCore.QRect(250, 70, 201, 20))
        self.label_33.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                    "background-color: rgb(0, 85, 0);\n"
                                    "background-color: rgb(170, 85, 255);")
        self.label_33.setObjectName("label_33")
        self.label_63 = QtWidgets.QLabel(self.widget_48)
        self.label_63.setGeometry(QtCore.QRect(40, 120, 61, 16))
        self.label_63.setObjectName("label_63")
        self.inputID = QtWidgets.QLineEdit(self.widget_48)
        self.inputID.setGeometry(QtCore.QRect(30, 140, 161, 31))
        self.inputID.setObjectName("inputID")
        self.label_64 = QtWidgets.QLabel(self.widget_48)
        self.label_64.setGeometry(QtCore.QRect(240, 120, 81, 16))
        self.label_64.setObjectName("label_64")
        self.inputRoom = QtWidgets.QLineEdit(self.widget_48)
        self.inputRoom.setGeometry(QtCore.QRect(230, 140, 181, 31))
        self.inputRoom.setObjectName("inputRoom")
        self.label_65 = QtWidgets.QLabel(self.widget_48)
        self.label_65.setGeometry(QtCore.QRect(460, 120, 101, 16))
        self.label_65.setObjectName("label_65")
        self.inputDateIn = QtWidgets.QLineEdit(self.widget_48)
        self.inputDateIn.setGeometry(QtCore.QRect(450, 140, 151, 31))
        self.inputDateIn.setObjectName("inputDateIn")
        self.label_66 = QtWidgets.QLabel(self.widget_48)
        self.label_66.setGeometry(QtCore.QRect(40, 190, 101, 16))
        self.label_66.setObjectName("label_66")
        self.inputDateOut = QtWidgets.QLineEdit(self.widget_48)
        self.inputDateOut.setGeometry(QtCore.QRect(30, 210, 161, 31))
        self.inputDateOut.setObjectName("inputDateOut")
        self.label_67 = QtWidgets.QLabel(self.widget_48)
        self.label_67.setGeometry(QtCore.QRect(240, 190, 47, 13))
        self.label_67.setObjectName("label_67")
        self.inputAccount = QtWidgets.QLineEdit(self.widget_48)
        self.inputAccount.setGeometry(QtCore.QRect(230, 210, 181, 31))
        self.inputAccount.setObjectName("inputAccount")
        self.buttonAdd = QtWidgets.QPushButton(self.widget_48)
        self.buttonAdd.setGeometry(QtCore.QRect(560, 250, 75, 23))
        self.buttonAdd.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.buttonAdd.setObjectName("buttonAdd")
        self.tableRegister = QtWidgets.QTableWidget(self.widget_48)
        self.tableRegister.setGeometry(QtCore.QRect(30, 320, 611, 151))
        self.tableRegister.setObjectName("tableRegister")
        self.tableRegister.setColumnCount(5)
        self.tableRegister.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableRegister.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRegister.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRegister.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRegister.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRegister.setHorizontalHeaderItem(4, item)
        self.BSalirRegistro = QtWidgets.QPushButton(self.widget_48)
        self.BSalirRegistro.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.BSalirRegistro.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.BSalirRegistro.setObjectName("BSalirRegistro")
        self.label_34 = QtWidgets.QLabel(self.widget_48)
        self.label_34.setGeometry(QtCore.QRect(180, 280, 71, 20))
        self.label_34.setObjectName("label_34")
        self.inputSearchRoom = QtWidgets.QLineEdit(self.widget_48)
        self.inputSearchRoom.setGeometry(QtCore.QRect(260, 280, 101, 20))
        self.inputSearchRoom.setObjectName("inputSearchRoom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#aa00ff;\">MENU </span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#aa00ff;\">REGISTRO</span></p></body></html>"))
        self.label_31.setText(_translate(
            "MainWindow", "INGRESE EL ID PARA BUSCAR,ELIMINAR O MODIFICAR"))
        self.label_32.setText(_translate("MainWindow", "HUESPED:"))
        self.buttonSearch.setText(_translate("MainWindow", "BUSCAR"))
        self.buttonSearch.clicked.connect(self.searchByID)
        self.buttonDelete.setText(_translate("MainWindow", "ELIMINAR"))
        self.buttonDelete.clicked.connect(self.deleteByID)
        self.buttonModify.setText(_translate("MainWindow", "MODIFICAR"))
        self.buttonModify.clicked.connect(self.modifyByID)
        self.label_33.setText(_translate(
            "MainWindow", "INGRESE LA SIGUIENTE INFORMACION:"))
        self.label_63.setText(_translate("MainWindow", "HUESPED:"))
        self.label_64.setText(_translate("MainWindow", "HABITACION:"))
        self.label_65.setText(_translate("MainWindow", "FECHA DE ENTRADA:"))
        self.label_66.setText(_translate("MainWindow", "FECHA DE SALIDA:"))
        self.label_67.setText(_translate("MainWindow", "CUENTA:"))
        self.buttonAdd.setText(_translate("MainWindow", "AGREGAR"))
        self.buttonAdd.clicked.connect(self.addRegister)
        item = self.tableRegister.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Huesped"))
        item = self.tableRegister.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Habitacion"))
        item = self.tableRegister.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fecha entrada"))
        item = self.tableRegister.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fecha salida"))
        item = self.tableRegister.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cuenta"))
        self.BSalirRegistro.setText(_translate("MainWindow", "SALIR:"))
        self.label_34.setText(_translate("MainWindow", "HABITACION:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
