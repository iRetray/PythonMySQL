from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


def connect():
    connection = pymysql.connect(
        host="localhost", port=3306, user="root", password="", db="basealojamientos(pf)"
    )
    print("Database is Connected!")
    return connection


class Ui_MainWindow(object):

    def addInscription(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL newinscripcion("+self.inputID.text() + \
            ","+self.inputPlace.text()+","+self.inputGuest.text() + \
            ")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure newinscripcion")

        asdasd

    def searchByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL getinscripciones("+self.inputSearchID.text() + \
            ", "+self.inputSearchPlace.text()+", "+self.inputSearchGuest.text()+")"
        print(sql)
        myCursor.execute(sql)
        objects = myCursor.fetchall()
        print(objects)
        myConnection.commit()
        self.tableInscriptions.setRowCount(0)
        for row_number, row_data in enumerate(objects):
            self.tableInscriptions.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableInscriptions.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        print("Finished SQL Procedure getinscripciones")

    def deleteByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL delinscripciones("+self.inputSearchID.text()+", " + \
            self.inputSearchPlace+", "+self.inputSearchGuest.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure delinscripciones")

    def modifyByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL modinscripciones("+self.inputID.text() + \
            ","+self.inputPlace.text()+","+self.inputGuest.text() + \
            ","+self.inputSearchID.text()+","+self.inputSearchPlace.text() + \
            ", "+self.inputSearchGuest.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure modinscripciones")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 681, 531))
        self.widget_4.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                                    "alternate-background-color: rgb(255, 0, 0);")
        self.widget_4.setObjectName("widget_4")
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setGeometry(QtCore.QRect(8, 10, 661, 481))
        self.widget_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_7.setObjectName("widget_7")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget_7)
        self.textBrowser_7.setGeometry(QtCore.QRect(220, -2, 256, 71))
        self.textBrowser_7.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.widget_38 = QtWidgets.QWidget(self.widget_7)
        self.widget_38.setGeometry(QtCore.QRect(0, 0, 221, 16))
        self.widget_38.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_38.setObjectName("widget_38")
        self.widget_39 = QtWidgets.QWidget(self.widget_7)
        self.widget_39.setGeometry(QtCore.QRect(0, 10, 16, 461))
        self.widget_39.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_39.setObjectName("widget_39")
        self.widget_41 = QtWidgets.QWidget(self.widget_7)
        self.widget_41.setGeometry(QtCore.QRect(645, 0, 16, 471))
        self.widget_41.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_41.setObjectName("widget_41")
        self.widget_42 = QtWidgets.QWidget(self.widget_7)
        self.widget_42.setGeometry(QtCore.QRect(470, 0, 181, 16))
        self.widget_42.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_42.setObjectName("widget_42")
        self.widget_40 = QtWidgets.QWidget(self.widget_7)
        self.widget_40.setGeometry(QtCore.QRect(0, 470, 661, 20))
        self.widget_40.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_40.setObjectName("widget_40")
        self.label_10 = QtWidgets.QLabel(self.widget_7)
        self.label_10.setGeometry(QtCore.QRect(180, 190, 361, 20))
        self.label_10.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                    "background-color: rgb(255, 85, 0);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget_7)
        self.label_11.setGeometry(QtCore.QRect(20, 220, 61, 16))
        self.label_11.setObjectName("label_11")
        self.inputSearchID = QtWidgets.QLineEdit(self.widget_7)
        self.inputSearchID.setGeometry(QtCore.QRect(80, 220, 51, 20))
        self.inputSearchID.setObjectName("inputSearchID")
        self.buttonSearch = QtWidgets.QPushButton(self.widget_7)
        self.buttonSearch.setGeometry(QtCore.QRect(420, 220, 61, 21))
        self.buttonSearch.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(255, 85, 0);")
        self.buttonSearch.setObjectName("buttonSearch")
        self.buttonDelete = QtWidgets.QPushButton(self.widget_7)
        self.buttonDelete.setGeometry(QtCore.QRect(490, 220, 61, 23))
        self.buttonDelete.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(255, 85, 0);")
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonModify = QtWidgets.QPushButton(self.widget_7)
        self.buttonModify.setGeometry(QtCore.QRect(560, 220, 75, 23))
        self.buttonModify.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(255, 85, 0);")
        self.buttonModify.setObjectName("buttonModify")
        self.label_12 = QtWidgets.QLabel(self.widget_7)
        self.label_12.setGeometry(QtCore.QRect(240, 70, 211, 20))
        self.label_12.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                    "background-color: rgb(255, 85, 0);\n"
                                    "background-color: rgb(255, 85, 0);")
        self.label_12.setObjectName("label_12")
        self.label_60 = QtWidgets.QLabel(self.widget_7)
        self.label_60.setGeometry(QtCore.QRect(50, 120, 71, 16))
        self.label_60.setObjectName("label_60")
        self.inputID = QtWidgets.QLineEdit(self.widget_7)
        self.inputID.setGeometry(QtCore.QRect(40, 140, 151, 31))
        self.inputID.setObjectName("inputID")
        self.label_61 = QtWidgets.QLabel(self.widget_7)
        self.label_61.setGeometry(QtCore.QRect(270, 120, 91, 16))
        self.label_61.setObjectName("label_61")
        self.inputPlace = QtWidgets.QLineEdit(self.widget_7)
        self.inputPlace.setGeometry(QtCore.QRect(260, 140, 171, 31))
        self.inputPlace.setObjectName("inputPlace")
        self.label_62 = QtWidgets.QLabel(self.widget_7)
        self.label_62.setGeometry(QtCore.QRect(490, 120, 47, 13))
        self.label_62.setObjectName("label_62")
        self.inputGuest = QtWidgets.QLineEdit(self.widget_7)
        self.inputGuest.setGeometry(QtCore.QRect(480, 140, 161, 31))
        self.inputGuest.setObjectName("inputGuest")
        self.buttonAdd = QtWidgets.QPushButton(self.widget_7)
        self.buttonAdd.setGeometry(QtCore.QRect(560, 190, 75, 23))
        self.buttonAdd.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.buttonAdd.setObjectName("buttonAdd")
        self.tableInscriptions = QtWidgets.QTableWidget(self.widget_7)
        self.tableInscriptions.setGeometry(QtCore.QRect(20, 250, 611, 192))
        self.tableInscriptions.setObjectName("tableInscriptions")
        self.tableInscriptions.setColumnCount(3)
        self.tableInscriptions.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableInscriptions.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInscriptions.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInscriptions.setHorizontalHeaderItem(2, item)
        self.BSalirInscripciones = QtWidgets.QPushButton(self.widget_7)
        self.BSalirInscripciones.setGeometry(QtCore.QRect(60, 50, 75, 23))
        self.BSalirInscripciones.setStyleSheet(
            "background-color: rgb(255, 0, 0);")
        self.BSalirInscripciones.setObjectName("BSalirInscripciones")
        self.label_13 = QtWidgets.QLabel(self.widget_7)
        self.label_13.setGeometry(QtCore.QRect(150, 220, 81, 16))
        self.label_13.setObjectName("label_13")
        self.inputSearchPlace = QtWidgets.QLineEdit(self.widget_7)
        self.inputSearchPlace.setGeometry(QtCore.QRect(230, 220, 51, 20))
        self.inputSearchPlace.setObjectName("inputSearchPlace")
        self.label_14 = QtWidgets.QLabel(self.widget_7)
        self.label_14.setGeometry(QtCore.QRect(290, 220, 81, 16))
        self.label_14.setObjectName("label_14")
        self.inputSearchGuest = QtWidgets.QLineEdit(self.widget_7)
        self.inputSearchGuest.setGeometry(QtCore.QRect(350, 220, 51, 20))
        self.inputSearchGuest.setObjectName("inputSearchGuest")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ff5500;\">MENU </span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ff5500;\">INSCRIPCIONES</span></p></body></html>"))
        self.label_10.setText(_translate(
            "MainWindow", "INGRESE EL ID PARA BUSCAR,ELIMINAR O MODIFICAR"))
        self.label_11.setText(_translate("MainWindow", "ACTIVIDAD:"))
        self.buttonSearch.setText(_translate("MainWindow", "BUSCAR"))
        self.buttonSearch.clicked.connect(self.searchByID)
        self.buttonDelete.setText(_translate("MainWindow", "ELIMINAR"))
        self.buttonDelete.clicked.connect(self.deleteByID)
        self.buttonModify.setText(_translate("MainWindow", "MODIFICAR"))
        self.buttonModify.clicked.connect(self.modifyByID)
        self.label_12.setText(_translate(
            "MainWindow", "INGRESE LA SIGUIENTE INFORMACION :"))
        self.label_60.setText(_translate("MainWindow", "ACTIVIDAD:"))
        self.label_61.setText(_translate("MainWindow", "ALOJAMIENTO:"))
        self.label_62.setText(_translate("MainWindow", "HUESPED:"))
        self.buttonAdd.setText(_translate("MainWindow", "AGREGAR"))
        self.buttonAdd.clicked.connect(self.addInscription)
        item = self.tableInscriptions.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ACTIVIDAD"))
        item = self.tableInscriptions.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ALOJAMIENTO"))
        item = self.tableInscriptions.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "HUESPED"))
        self.BSalirInscripciones.setText(_translate("MainWindow", "SALIR:"))
        self.label_13.setText(_translate("MainWindow", "ALOJAMIENTO:"))
        self.label_14.setText(_translate("MainWindow", "HUESPED:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
