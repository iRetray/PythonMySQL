from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


def connect():
    connection = pymysql.connect(
        host="localhost", port=3306, user="root", password="", db="basealojamientos(pf)"
    )
    print("Database is Connected!")
    return connection


class Ui_MainWindow(object):

    def addRoom(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL newhabitacion("+self.inputID.text() + \
            ",'"+self.inputType.text()+"','"+self.inputTemperature.text() + \
            "','"+self.inputPrice.text()+"',"+self.inputPlace.text() + \
            ", "+self.inputKeeper.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure newhabitacion")

    def searchByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL gethabitacionesxid("+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        objects = myCursor.fetchall()
        print(objects)
        myConnection.commit()
        self.tableRooms.setRowCount(0)
        for row_number, row_data in enumerate(objects):
            self.tableRooms.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableRooms.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        print("Finished SQL Procedure gethabitacionesxid")

    def deleteByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL delhabitaciones("+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure delhabitaciones")

    def modifyByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL modhabitaciones("+self.inputID.text() + \
            ",'"+self.inputType.text()+"','"+self.inputTemperature.text() + \
            "','"+self.inputPrice.text()+"',"+self.inputPlace.text() + \
            ", "+self.inputKeeper.text()+", "+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure modhabitaciones")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 681, 531))
        self.frame_4.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.widget_6 = QtWidgets.QWidget(self.frame_4)
        self.widget_6.setGeometry(QtCore.QRect(10, 10, 661, 481))
        self.widget_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_6.setObjectName("widget_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget_6)
        self.textBrowser_6.setGeometry(QtCore.QRect(210, -2, 256, 71))
        self.textBrowser_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.widget_33 = QtWidgets.QWidget(self.widget_6)
        self.widget_33.setGeometry(QtCore.QRect(0, -1, 211, 16))
        self.widget_33.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_33.setObjectName("widget_33")
        self.widget_34 = QtWidgets.QWidget(self.widget_6)
        self.widget_34.setGeometry(QtCore.QRect(460, 0, 201, 16))
        self.widget_34.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_34.setObjectName("widget_34")
        self.widget_35 = QtWidgets.QWidget(self.widget_6)
        self.widget_35.setGeometry(QtCore.QRect(645, 10, 20, 471))
        self.widget_35.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_35.setObjectName("widget_35")
        self.widget_36 = QtWidgets.QWidget(self.widget_6)
        self.widget_36.setGeometry(QtCore.QRect(0, 470, 651, 16))
        self.widget_36.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_36.setObjectName("widget_36")
        self.widget_37 = QtWidgets.QWidget(self.widget_6)
        self.widget_37.setGeometry(QtCore.QRect(0, 10, 16, 461))
        self.widget_37.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_37.setObjectName("widget_37")
        self.label_13 = QtWidgets.QLabel(self.widget_6)
        self.label_13.setGeometry(QtCore.QRect(230, 70, 201, 20))
        self.label_13.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                    "background-color: rgb(85, 170, 255);\n"
                                    "background-color: rgb(0, 0, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget_6)
        self.label_14.setGeometry(QtCore.QRect(230, 250, 291, 20))
        self.label_14.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget_6)
        self.label_15.setGeometry(QtCore.QRect(30, 280, 16, 16))
        self.label_15.setObjectName("label_15")
        self.inputSearchID = QtWidgets.QLineEdit(self.widget_6)
        self.inputSearchID.setGeometry(QtCore.QRect(70, 280, 113, 20))
        self.inputSearchID.setObjectName("inputSearchID")
        self.buttonSearch = QtWidgets.QPushButton(self.widget_6)
        self.buttonSearch.setGeometry(QtCore.QRect(220, 280, 81, 21))
        self.buttonSearch.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.buttonSearch.setObjectName("buttonSearch")
        self.buttonDelete = QtWidgets.QPushButton(self.widget_6)
        self.buttonDelete.setGeometry(QtCore.QRect(360, 280, 75, 23))
        self.buttonDelete.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonModify = QtWidgets.QPushButton(self.widget_6)
        self.buttonModify.setGeometry(QtCore.QRect(490, 280, 75, 23))
        self.buttonModify.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.buttonModify.setObjectName("buttonModify")
        self.label_49 = QtWidgets.QLabel(self.widget_6)
        self.label_49.setGeometry(QtCore.QRect(60, 110, 47, 13))
        self.label_49.setObjectName("label_49")
        self.inputID = QtWidgets.QLineEdit(self.widget_6)
        self.inputID.setGeometry(QtCore.QRect(50, 130, 151, 31))
        self.inputID.setObjectName("inputID")
        self.label_50 = QtWidgets.QLabel(self.widget_6)
        self.label_50.setGeometry(QtCore.QRect(230, 110, 47, 13))
        self.label_50.setObjectName("label_50")
        self.inputType = QtWidgets.QLineEdit(self.widget_6)
        self.inputType.setGeometry(QtCore.QRect(230, 130, 171, 31))
        self.inputType.setObjectName("inputType")
        self.label_51 = QtWidgets.QLabel(self.widget_6)
        self.label_51.setGeometry(QtCore.QRect(440, 110, 151, 16))
        self.label_51.setObjectName("label_51")
        self.inputTemperature = QtWidgets.QLineEdit(self.widget_6)
        self.inputTemperature.setGeometry(QtCore.QRect(440, 130, 171, 31))
        self.inputTemperature.setObjectName("inputTemperature")
        self.label_52 = QtWidgets.QLabel(self.widget_6)
        self.label_52.setGeometry(QtCore.QRect(60, 190, 47, 13))
        self.label_52.setObjectName("label_52")
        self.inputPrice = QtWidgets.QLineEdit(self.widget_6)
        self.inputPrice.setGeometry(QtCore.QRect(50, 210, 151, 31))
        self.inputPrice.setObjectName("inputPrice")
        self.inputPlace = QtWidgets.QLineEdit(self.widget_6)
        self.inputPlace.setGeometry(QtCore.QRect(230, 210, 171, 31))
        self.inputPlace.setObjectName("inputPlace")
        self.label_53 = QtWidgets.QLabel(self.widget_6)
        self.label_53.setGeometry(QtCore.QRect(230, 190, 81, 16))
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.widget_6)
        self.label_54.setGeometry(QtCore.QRect(440, 190, 47, 13))
        self.label_54.setObjectName("label_54")
        self.inputKeeper = QtWidgets.QLineEdit(self.widget_6)
        self.inputKeeper.setGeometry(QtCore.QRect(440, 210, 171, 31))
        self.inputKeeper.setObjectName("inputKeeper")
        self.buttonAdd = QtWidgets.QPushButton(self.widget_6)
        self.buttonAdd.setGeometry(QtCore.QRect(560, 250, 75, 23))
        self.buttonAdd.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.buttonAdd.setObjectName("buttonAdd")
        self.tableRooms = QtWidgets.QTableWidget(self.widget_6)
        self.tableRooms.setGeometry(QtCore.QRect(20, 310, 621, 161))
        self.tableRooms.setObjectName("tableRooms")
        self.tableRooms.setColumnCount(6)
        self.tableRooms.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setHorizontalHeaderItem(5, item)
        self.BSalirHabitaciones = QtWidgets.QPushButton(self.widget_6)
        self.BSalirHabitaciones.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.BSalirHabitaciones.setStyleSheet(
            "background-color: rgb(255, 0, 0);")
        self.BSalirHabitaciones.setObjectName("BSalirHabitaciones")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">MENU </span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">HABITACIONES</span></p></body></html>"))
        self.label_13.setText(_translate(
            "MainWindow", "INGRESE LA SIGUIENTE INFORMACION:"))
        self.label_14.setText(_translate(
            "MainWindow", "INGRESE EL ID PARA BUSCAR,ELIMINAR O MODIFICAR"))
        self.label_15.setText(_translate("MainWindow", "ID:"))
        self.buttonSearch.setText(_translate("MainWindow", "BUSCAR"))
        self.buttonSearch.clicked.connect(self.searchByID)
        self.buttonDelete.setText(_translate("MainWindow", "ELIMINAR"))
        self.buttonDelete.clicked.connect(self.deleteByID)
        self.buttonModify.setText(_translate("MainWindow", "MODIFICAR"))
        self.buttonModify.clicked.connect(self.modifyByID)
        self.label_49.setText(_translate("MainWindow", "ID:"))
        self.label_50.setText(_translate("MainWindow", "TIPO:"))
        self.label_51.setText(_translate(
            "MainWindow", "REGULACION TEMPERATURA: "))
        self.label_52.setText(_translate("MainWindow", "PRECIO:"))
        self.label_53.setText(_translate("MainWindow", "ALOJAMIENTO:"))
        self.label_54.setText(_translate("MainWindow", "KEEPER:"))
        self.buttonAdd.setText(_translate("MainWindow", "AGREGAR"))
        self.buttonAdd.clicked.connect(self.addRoom)
        item = self.tableRooms.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableRooms.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo"))
        item = self.tableRooms.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Temperatura"))
        item = self.tableRooms.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.tableRooms.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Alojamiento"))
        item = self.tableRooms.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Keeper"))
        self.BSalirHabitaciones.setText(_translate("MainWindow", "SALIR:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
