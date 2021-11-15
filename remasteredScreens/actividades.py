from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


def connect():
    connection = pymysql.connect(
        host="localhost", port=3306, user="root", password="", db="basealojamientos(pf)"
    )
    print("Database is Connected!")
    return connection


class Ui_MainWindow(object):

    def addActivity(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL newactividad("+self.inputID.text() + \
            ",'"+self.inputName.text()+"','"+self.inputDescription.text() + \
            "','"+self.inputDifficulty.text()+"',NULL)"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure newactividad")

    def searchByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL getactividadxid("+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        objects = myCursor.fetchall()
        print(objects)
        myConnection.commit()
        self.tableActivities.setRowCount(0)
        for row_number, row_data in enumerate(objects):
            self.tableActivities.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableActivities.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        print("Finished SQL Procedure getactividadxid")

    def deleteByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL delactividades("+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure delactividades")

    def modifyByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL modactividades("+self.inputID.text() + \
            ",'"+self.inputName.text()+"','"+self.inputDescription.text() + \
            "','"+self.inputDifficulty.text()+"',NULL,"+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure modactividades")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 681, 531))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 661, 481))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-color: rgb(255, 0, 0);\n"
                                    "alternate-background-color: rgb(255, 0, 0);")
        self.widget_2.setObjectName("widget_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser.setGeometry(QtCore.QRect(200, 0, 281, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("\n"
                                       "background-color: rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.widget_12 = QtWidgets.QWidget(self.widget_2)
        self.widget_12.setGeometry(QtCore.QRect(0, -6, 16, 481))
        self.widget_12.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_12.setObjectName("widget_12")
        self.widget_8 = QtWidgets.QWidget(self.widget_2)
        self.widget_8.setGeometry(QtCore.QRect(9, 0, 191, 16))
        self.widget_8.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_8.setObjectName("widget_8")
        self.widget_9 = QtWidgets.QWidget(self.widget_2)
        self.widget_9.setGeometry(QtCore.QRect(480, 0, 181, 16))
        self.widget_9.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_9.setObjectName("widget_9")
        self.widget_10 = QtWidgets.QWidget(self.widget_2)
        self.widget_10.setGeometry(QtCore.QRect(645, 11, 16, 471))
        self.widget_10.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_10.setObjectName("widget_10")
        self.widget_11 = QtWidgets.QWidget(self.widget_2)
        self.widget_11.setGeometry(QtCore.QRect(0, 470, 651, 16))
        self.widget_11.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_11.setObjectName("widget_11")
        self.label_28 = QtWidgets.QLabel(self.widget_2)
        self.label_28.setGeometry(QtCore.QRect(240, 80, 201, 20))
        self.label_28.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                    "background-color: rgb(255, 255, 0);\n"
                                    "background-color: rgb(255, 255, 0);")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.widget_2)
        self.label_29.setGeometry(QtCore.QRect(160, 250, 361, 20))
        self.label_29.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                    "background-color: rgb(255, 255, 0);")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.widget_2)
        self.label_30.setGeometry(QtCore.QRect(20, 280, 20, 20))
        self.label_30.setObjectName("label_30")
        self.inputSearchID = QtWidgets.QLineEdit(self.widget_2)
        self.inputSearchID.setGeometry(QtCore.QRect(50, 280, 113, 20))
        self.inputSearchID.setObjectName("inputSearchID")
        self.buttonSearch = QtWidgets.QPushButton(self.widget_2)
        self.buttonSearch.setGeometry(QtCore.QRect(210, 280, 81, 21))
        self.buttonSearch.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(255, 255, 0);")
        self.buttonSearch.setObjectName("buttonSearch")
        self.buttonDelete = QtWidgets.QPushButton(self.widget_2)
        self.buttonDelete.setGeometry(QtCore.QRect(320, 280, 75, 23))
        self.buttonDelete.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(255, 255, 0);")
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonModify = QtWidgets.QPushButton(self.widget_2)
        self.buttonModify.setGeometry(QtCore.QRect(420, 280, 75, 23))
        self.buttonModify.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "background-color: rgb(255, 255, 0);")
        self.buttonModify.setObjectName("buttonModify")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(50, 120, 21, 16))
        self.label.setObjectName("label")
        self.inputID = QtWidgets.QLineEdit(self.widget_2)
        self.inputID.setGeometry(QtCore.QRect(50, 140, 151, 31))
        self.inputID.setObjectName("inputID")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(220, 120, 47, 13))
        self.label_2.setObjectName("label_2")
        self.inputName = QtWidgets.QLineEdit(self.widget_2)
        self.inputName.setGeometry(QtCore.QRect(220, 140, 141, 31))
        self.inputName.setObjectName("inputName")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(380, 120, 71, 16))
        self.label_3.setObjectName("label_3")
        self.inputDescription = QtWidgets.QLineEdit(self.widget_2)
        self.inputDescription.setGeometry(QtCore.QRect(380, 140, 141, 31))
        self.inputDescription.setObjectName("inputDescription")
        self.inputDifficulty = QtWidgets.QLineEdit(self.widget_2)
        self.inputDifficulty.setGeometry(QtCore.QRect(50, 210, 151, 31))
        self.inputDifficulty.setObjectName("inputDifficulty")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(220, 190, 81, 16))
        self.label_5.setObjectName("label_5")
        self.inputCoordinator = QtWidgets.QLineEdit(self.widget_2)
        self.inputCoordinator.setGeometry(QtCore.QRect(220, 210, 141, 31))
        self.inputCoordinator.setObjectName("inputCoordinator")
        self.buttonAddActivity = QtWidgets.QPushButton(self.widget_2)
        self.buttonAddActivity.setGeometry(QtCore.QRect(560, 250, 75, 23))
        self.buttonAddActivity.setStyleSheet(
            "background-color: rgb(255, 255, 0);")
        self.buttonAddActivity.setObjectName("buttonAddActivity")
        self.tableActivities = QtWidgets.QTableWidget(self.widget_2)
        self.tableActivities.setEnabled(True)
        self.tableActivities.setGeometry(QtCore.QRect(20, 310, 621, 151))
        self.tableActivities.setObjectName("tableActivities")
        self.tableActivities.setColumnCount(5)
        self.tableActivities.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableActivities.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableActivities.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableActivities.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableActivities.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableActivities.setHorizontalHeaderItem(4, item)
        self.BSalirActividades = QtWidgets.QPushButton(self.widget_2)
        self.BSalirActividades.setGeometry(QtCore.QRect(40, 50, 75, 23))
        self.BSalirActividades.setStyleSheet(
            "background-color: rgb(255, 0, 0);")
        self.BSalirActividades.setObjectName("BSalirActividades")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic; text-decoration: underline; color:#ffff00;\">MENU  </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic; text-decoration: underline; color:#ffff00;\">ACTIVIDADES</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_28.setText(_translate(
            "MainWindow", "INGRESE LA SIGUIENTE INFORMACION:"))
        self.label_29.setText(_translate(
            "MainWindow", "INGRESE EL ID PARA BUSCAR,ELIMINAR O MODIFICAR"))
        self.label_30.setText(_translate("MainWindow", "ID:"))
        self.buttonSearch.setText(_translate("MainWindow", "BUSCAR"))
        self.buttonSearch.clicked.connect(self.searchByID)
        self.buttonDelete.setText(_translate("MainWindow", "ELIMINAR"))
        self.buttonDelete.clicked.connect(self.deleteByID)
        self.buttonModify.setText(_translate("MainWindow", "MODIFICAR"))
        self.buttonModify.clicked.connect(self.modifyByID)
        self.label.setText(_translate("MainWindow", "ID :"))
        self.label_2.setText(_translate("MainWindow", "NOMBRE:"))
        self.label_3.setText(_translate("MainWindow", "DESCRIPCION:"))
        self.label_4.setText(_translate("MainWindow", "DIFICULTAD:"))
        self.label_5.setText(_translate("MainWindow", "COORDINADOR:"))
        self.buttonAddActivity.setText(_translate("MainWindow", "AGREGAR"))
        self.buttonAddActivity.clicked.connect(self.addActivity)
        item = self.tableActivities.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableActivities.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableActivities.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Descripcion"))
        item = self.tableActivities.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dificultad"))
        item = self.tableActivities.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Coordinador"))
        self.BSalirActividades.setText(_translate("MainWindow", "SALIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
