from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


def connect():
    connection = pymysql.connect(
        host="localhost", port=3306, user="root", password="", db="basealojamientos(pf)"
    )
    print("Database is Connected!")
    return connection


class Ui_MainWindow(object):

    def addGuest(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL newhuesped("+self.inputID.text() + \
            ",'"+self.inputName.text()+"','"+self.inputDirection.text() + \
            "','"+self.inputPhone.text()+"','"+self.inputOrigin.text()+"')"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure newhuesped")

    def searchByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL gethuespedesxid("+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        objects = myCursor.fetchall()
        print(objects)
        myConnection.commit()
        self.tableGuest.setRowCount(0)
        for row_number, row_data in enumerate(objects):
            self.tableGuest.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableGuest.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        print("Finished SQL Procedure gethuespedesxid")

    def deleteByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL delhuespedes("+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure delhuespedes")

    def modifyByID(self, none):
        myConnection = connect()
        myCursor = myConnection.cursor()
        sql = "CALL modhuespedes("+self.inputID.text() + \
            ",'"+self.inputName.text()+"','"+self.inputDirection.text() + \
            "','"+self.inputPhone.text()+"','"+self.inputOrigin.text() + \
            "', "+self.inputSearchID.text()+")"
        print(sql)
        myCursor.execute(sql)
        myConnection.commit()
        print("Finished SQL Procedure modhuespedes")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 0, 681, 561))
        self.widget_3.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.widget_3.setObjectName("widget_3")
        self.frame_7 = QtWidgets.QFrame(self.widget_3)
        self.frame_7.setGeometry(QtCore.QRect(10, 10, 661, 481))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.frame_7)
        self.textBrowser_5.setGeometry(QtCore.QRect(210, -1, 271, 71))
        self.textBrowser_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.widget_28 = QtWidgets.QWidget(self.frame_7)
        self.widget_28.setGeometry(QtCore.QRect(0, 0, 221, 16))
        self.widget_28.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_28.setObjectName("widget_28")
        self.widget_29 = QtWidgets.QWidget(self.frame_7)
        self.widget_29.setGeometry(QtCore.QRect(0, 10, 16, 471))
        self.widget_29.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_29.setObjectName("widget_29")
        self.widget_31 = QtWidgets.QWidget(self.frame_7)
        self.widget_31.setGeometry(QtCore.QRect(645, 0, 16, 471))
        self.widget_31.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_31.setObjectName("widget_31")
        self.widget_32 = QtWidgets.QWidget(self.frame_7)
        self.widget_32.setGeometry(QtCore.QRect(460, 0, 191, 16))
        self.widget_32.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_32.setObjectName("widget_32")
        self.inputSearchID = QtWidgets.QLineEdit(self.frame_7)
        self.inputSearchID.setGeometry(QtCore.QRect(40, 290, 113, 20))
        self.inputSearchID.setObjectName("inputSearchID")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setGeometry(QtCore.QRect(240, 70, 201, 20))
        self.label_7.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                   "background-color: rgb(255, 0, 127);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        self.label_8.setGeometry(QtCore.QRect(200, 260, 281, 20))
        self.label_8.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setGeometry(QtCore.QRect(20, 290, 16, 16))
        self.label_9.setObjectName("label_9")
        self.buttonSearch = QtWidgets.QPushButton(self.frame_7)
        self.buttonSearch.setGeometry(QtCore.QRect(200, 290, 81, 21))
        self.buttonSearch.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.buttonSearch.setObjectName("buttonSearch")
        self.buttonDelete = QtWidgets.QPushButton(self.frame_7)
        self.buttonDelete.setGeometry(QtCore.QRect(320, 290, 75, 23))
        self.buttonDelete.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonModify = QtWidgets.QPushButton(self.frame_7)
        self.buttonModify.setGeometry(QtCore.QRect(450, 290, 75, 23))
        self.buttonModify.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.buttonModify.setObjectName("buttonModify")
        self.buttonAdd = QtWidgets.QPushButton(self.frame_7)
        self.buttonAdd.setGeometry(QtCore.QRect(550, 260, 75, 23))
        self.buttonAdd.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.buttonAdd.setObjectName("buttonAdd")
        self.label_55 = QtWidgets.QLabel(self.frame_7)
        self.label_55.setGeometry(QtCore.QRect(50, 120, 47, 13))
        self.label_55.setObjectName("label_55")
        self.inputID = QtWidgets.QLineEdit(self.frame_7)
        self.inputID.setGeometry(QtCore.QRect(40, 140, 141, 31))
        self.inputID.setObjectName("inputID")
        self.label_56 = QtWidgets.QLabel(self.frame_7)
        self.label_56.setGeometry(QtCore.QRect(240, 120, 47, 13))
        self.label_56.setObjectName("label_56")
        self.inputName = QtWidgets.QLineEdit(self.frame_7)
        self.inputName.setGeometry(QtCore.QRect(240, 140, 191, 31))
        self.inputName.setObjectName("inputName")
        self.label_57 = QtWidgets.QLabel(self.frame_7)
        self.label_57.setGeometry(QtCore.QRect(460, 120, 71, 16))
        self.label_57.setObjectName("label_57")
        self.inputDirection = QtWidgets.QLineEdit(self.frame_7)
        self.inputDirection.setGeometry(QtCore.QRect(460, 140, 171, 31))
        self.inputDirection.setObjectName("inputDirection")
        self.label_58 = QtWidgets.QLabel(self.frame_7)
        self.label_58.setGeometry(QtCore.QRect(40, 200, 61, 16))
        self.label_58.setObjectName("label_58")
        self.inputPhone = QtWidgets.QLineEdit(self.frame_7)
        self.inputPhone.setGeometry(QtCore.QRect(40, 220, 141, 31))
        self.inputPhone.setObjectName("inputPhone")
        self.label_59 = QtWidgets.QLabel(self.frame_7)
        self.label_59.setGeometry(QtCore.QRect(240, 200, 47, 13))
        self.label_59.setObjectName("label_59")
        self.inputOrigin = QtWidgets.QLineEdit(self.frame_7)
        self.inputOrigin.setGeometry(QtCore.QRect(240, 220, 191, 31))
        self.inputOrigin.setObjectName("inputOrigin")
        self.tableGuest = QtWidgets.QTableWidget(self.frame_7)
        self.tableGuest.setGeometry(QtCore.QRect(20, 320, 621, 141))
        self.tableGuest.setObjectName("tableGuest")
        self.tableGuest.setColumnCount(5)
        self.tableGuest.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableGuest.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableGuest.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableGuest.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableGuest.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableGuest.setHorizontalHeaderItem(4, item)
        self.BSalirHuespedes = QtWidgets.QPushButton(self.frame_7)
        self.BSalirHuespedes.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.BSalirHuespedes.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.BSalirHuespedes.setObjectName("BSalirHuespedes")
        self.widget_30 = QtWidgets.QWidget(self.widget_3)
        self.widget_30.setGeometry(QtCore.QRect(20, 480, 653, 16))
        self.widget_30.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_30.setObjectName("widget_30")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ff007f;\">MENU </span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ff007f;\">HUESPEDES</span></p></body></html>"))
        self.label_7.setText(_translate(
            "MainWindow", "INGRESE LA SIGUIENTE INFORMACION:"))
        self.label_8.setText(_translate(
            "MainWindow", "INGRESE EL ID PARA BUSCAR,ELIMINAR O MODIFICAR"))
        self.label_9.setText(_translate("MainWindow", "ID:"))
        self.buttonSearch.setText(_translate("MainWindow", "BUSCAR"))
        self.buttonSearch.clicked.connect(self.searchByID)
        self.buttonDelete.setText(_translate("MainWindow", "ELIMINAR"))
        self.buttonDelete.clicked.connect(self.deleteByID)
        self.buttonModify.setText(_translate("MainWindow", "MODIFICAR"))
        self.buttonModify.clicked.connect(self.modifyByID)
        self.buttonAdd.setText(_translate("MainWindow", "AGREGAR"))
        self.buttonAdd.clicked.connect(self.addGuest)
        self.label_55.setText(_translate("MainWindow", "ID:"))
        self.label_56.setText(_translate("MainWindow", "NOMBRE:"))
        self.label_57.setText(_translate("MainWindow", "DIRECCION:"))
        self.label_58.setText(_translate("MainWindow", "TELEFONO:"))
        self.label_59.setText(_translate("MainWindow", "ORIGEN:"))
        item = self.tableGuest.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableGuest.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableGuest.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Direccion"))
        item = self.tableGuest.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.tableGuest.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Origen"))
        self.BSalirHuespedes.setText(_translate("MainWindow", "SALIR:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
