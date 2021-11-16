from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


def connect():
    connection = pymysql.connect(
        host="localhost", port=3306, user="root", password="", db="basealojamientos(pf)"
    )
    print("Database is Connected!")
    return connection


class Ui_MainWindow(object):

    def addSchedule(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL newcronograma("+self.inputID.text()+", " + \
            self.inputPlace.text()+", '"+self.inputDay.text()+"')"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure newcronograma")

    def searchByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL getcronogramas("+self.inputSearchID.text() + \
            ", "+self.inputPlaceOld.text()+")"
        print(sql)
        myCursor.execute(sql)
        objects = myCursor.fetchall()
        print(objects)
        myConnection.commit()
        self.tableSchedules.setRowCount(0)
        for row_number, row_data in enumerate(objects):
            self.tableSchedules.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableSchedules.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        print("Finished SQL Procedure getcronogramas")

    def deleteByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL delcronogramas("+self.inputSearchID.text() + \
            ","+self.inputPlaceOld.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure delcronogramas")

    def modifyByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL modcronogramas("+self.inputID.text() + \
            ",'"+self.inputPlace.text()+"',"+self.inputSearchID.text() + \
            ","+self.inputPlaceOld.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure modcronogramas")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 681, 531))
        self.frame.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.L_ActividadCronogramas = QtWidgets.QWidget(self.frame)
        self.L_ActividadCronogramas.setGeometry(QtCore.QRect(9, 10, 661, 491))
        self.L_ActividadCronogramas.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.L_ActividadCronogramas.setObjectName("L_ActividadCronogramas")
        self.widget_20 = QtWidgets.QWidget(self.L_ActividadCronogramas)
        self.widget_20.setGeometry(QtCore.QRect(0, 0, 141, 16))
        self.widget_20.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_20.setObjectName("widget_20")
        self.widget_21 = QtWidgets.QWidget(self.L_ActividadCronogramas)
        self.widget_21.setGeometry(QtCore.QRect(500, 0, 161, 16))
        self.widget_21.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_21.setObjectName("widget_21")
        self.widget_13 = QtWidgets.QWidget(self.L_ActividadCronogramas)
        self.widget_13.setGeometry(QtCore.QRect(0, 10, 16, 471))
        self.widget_13.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_13.setObjectName("widget_13")
        self.widget_14 = QtWidgets.QWidget(self.L_ActividadCronogramas)
        self.widget_14.setGeometry(QtCore.QRect(0, 480, 661, 20))
        self.widget_14.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_14.setObjectName("widget_14")
        self.widget_15 = QtWidgets.QWidget(self.L_ActividadCronogramas)
        self.widget_15.setGeometry(QtCore.QRect(648, 10, 16, 471))
        self.widget_15.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_15.setObjectName("widget_15")
        self.label_25 = QtWidgets.QLabel(self.L_ActividadCronogramas)
        self.label_25.setGeometry(QtCore.QRect(220, 60, 201, 20))
        self.label_25.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                    "background-color: rgb(85, 255, 0);\n"
                                    "background-color: rgb(85, 255, 0);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.L_ActividadCronogramas)
        self.label_26.setGeometry(QtCore.QRect(150, 250, 361, 20))
        self.label_26.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                    "background-color: rgb(85, 255, 0);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.L_ActividadCronogramas)
        self.label_27.setGeometry(QtCore.QRect(20, 280, 61, 20))
        self.label_27.setObjectName("label_27")
        self.inputSearchID = QtWidgets.QLineEdit(self.L_ActividadCronogramas)
        self.inputSearchID.setGeometry(QtCore.QRect(80, 280, 91, 20))
        self.inputSearchID.setObjectName("inputSearchID")
        self.buttonSearch = QtWidgets.QPushButton(self.L_ActividadCronogramas)
        self.buttonSearch.setGeometry(QtCore.QRect(380, 280, 81, 21))
        self.buttonSearch.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(85, 255, 0);")
        self.buttonSearch.setObjectName("buttonSearch")
        self.buttonDelete = QtWidgets.QPushButton(self.L_ActividadCronogramas)
        self.buttonDelete.setGeometry(QtCore.QRect(470, 280, 75, 23))
        self.buttonDelete.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(85, 255, 0);")
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonModify = QtWidgets.QPushButton(self.L_ActividadCronogramas)
        self.buttonModify.setGeometry(QtCore.QRect(560, 280, 75, 23))
        self.buttonModify.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(85, 255, 0);")
        self.buttonModify.setObjectName("buttonModify")
        self.textBrowser_2 = QtWidgets.QTextBrowser(
            self.L_ActividadCronogramas)
        self.textBrowser_2.setGeometry(QtCore.QRect(140, 0, 361, 61))
        self.textBrowser_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_39 = QtWidgets.QLabel(self.L_ActividadCronogramas)
        self.label_39.setGeometry(QtCore.QRect(60, 110, 61, 16))
        self.label_39.setObjectName("label_39")
        self.inputID = QtWidgets.QLineEdit(self.L_ActividadCronogramas)
        self.inputID.setGeometry(QtCore.QRect(60, 130, 151, 31))
        self.inputID.setObjectName("inputID")
        self.label_40 = QtWidgets.QLabel(self.L_ActividadCronogramas)
        self.label_40.setGeometry(QtCore.QRect(270, 110, 91, 16))
        self.label_40.setObjectName("label_40")
        self.inputPlace = QtWidgets.QLineEdit(self.L_ActividadCronogramas)
        self.inputPlace.setGeometry(QtCore.QRect(260, 130, 151, 31))
        self.inputPlace.setObjectName("inputPlace")
        self.label_41 = QtWidgets.QLabel(self.L_ActividadCronogramas)
        self.label_41.setGeometry(QtCore.QRect(60, 180, 47, 13))
        self.label_41.setObjectName("label_41")
        self.inputDay = QtWidgets.QLineEdit(self.L_ActividadCronogramas)
        self.inputDay.setGeometry(QtCore.QRect(60, 200, 151, 31))
        self.inputDay.setObjectName("inputDay")
        self.label_42 = QtWidgets.QLabel(self.L_ActividadCronogramas)
        self.label_42.setGeometry(QtCore.QRect(260, 180, 47, 13))
        self.label_42.setObjectName("label_42")
        self.inputHour = QtWidgets.QLineEdit(self.L_ActividadCronogramas)
        self.inputHour.setGeometry(QtCore.QRect(260, 200, 151, 31))
        self.inputHour.setObjectName("inputHour")
        self.buttonAdd = QtWidgets.QPushButton(self.L_ActividadCronogramas)
        self.buttonAdd.setGeometry(QtCore.QRect(560, 250, 75, 23))
        self.buttonAdd.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.buttonAdd.setObjectName("buttonAdd")
        self.tableSchedules = QtWidgets.QTableWidget(
            self.L_ActividadCronogramas)
        self.tableSchedules.setGeometry(QtCore.QRect(20, 310, 621, 161))
        self.tableSchedules.setObjectName("tableSchedules")
        self.tableSchedules.setColumnCount(4)
        self.tableSchedules.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSchedules.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSchedules.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSchedules.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSchedules.setHorizontalHeaderItem(3, item)
        self.BSalirCrongramas = QtWidgets.QPushButton(
            self.L_ActividadCronogramas)
        self.BSalirCrongramas.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.BSalirCrongramas.setStyleSheet(
            "background-color: rgb(255, 0, 0);")
        self.BSalirCrongramas.setObjectName("BSalirCrongramas")
        self.label_28 = QtWidgets.QLabel(self.L_ActividadCronogramas)
        self.label_28.setGeometry(QtCore.QRect(180, 280, 81, 20))
        self.label_28.setObjectName("label_28")
        self.inputPlaceOld = QtWidgets.QLineEdit(self.L_ActividadCronogramas)
        self.inputPlaceOld.setGeometry(QtCore.QRect(260, 280, 113, 20))
        self.inputPlaceOld.setObjectName("inputPlaceOld")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_25.setText(_translate(
            "MainWindow", "INGRESE LA SIGUIENTE INFORMACION:"))
        self.label_26.setText(_translate(
            "MainWindow", "INGRESE EL ID PARA BUSCAR,ELIMINAR O MODIFICAR"))
        self.label_27.setText(_translate("MainWindow", "ACTIVIDAD:"))
        self.buttonSearch.setText(_translate("MainWindow", "BUSCAR"))
        self.buttonSearch.clicked.connect(self.searchByID)
        self.buttonDelete.setText(_translate("MainWindow", "ELIMINAR"))
        self.buttonDelete.clicked.connect(self.deleteByID)
        self.buttonModify.setText(_translate("MainWindow", "MODIFICAR"))
        self.buttonModify.clicked.connect(self.modifyByID)
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline; color:#00ff00;\">MENU </span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline; color:#00ff00;\">CRONOGRAMAS</span></p></body></html>"))
        self.label_39.setText(_translate("MainWindow", "ACTIVIDAD:"))
        self.label_40.setText(_translate("MainWindow", "ALOJAMIENTO:"))
        self.label_41.setText(_translate("MainWindow", "DIA:"))
        self.label_42.setText(_translate("MainWindow", "HORA:"))
        self.buttonAdd.setText(_translate("MainWindow", "AGREGAR"))
        self.buttonAdd.clicked.connect(self.addSchedule)
        item = self.tableSchedules.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Actividad"))
        item = self.tableSchedules.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Alojamiento"))
        item = self.tableSchedules.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Dia"))
        item = self.tableSchedules.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Hora"))
        self.BSalirCrongramas.setText(_translate("MainWindow", "SALIR:"))
        self.label_28.setText(_translate("MainWindow", "ALOJAMIENTO:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
