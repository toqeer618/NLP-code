# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\showvid.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from results import Ui_MainWindow1
from default_class import model

lst_id=["Kkkkkd"]
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
      
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 461)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -5, 671, 51))
        self.label.setStyleSheet("background-color: rgb(116, 116, 116);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(250, 10, 331, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(580, 10, 75, 31))
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 147, 220);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 110, 231, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 110, 231, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 160, 231, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 160, 231, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 210, 231, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 210, 231, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(310, 260, 231, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 260, 231, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(310, 310, 231, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(70, 310, 231, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 111, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("2.png"))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.btnclick1)
        self.pushButton_2.clicked.connect(self.btnclick2)
        self.pushButton_3.clicked.connect(self.btnclick3)
        self.pushButton_4.clicked.connect(self.btnclick4)
        self.pushButton_5.clicked.connect(self.btnclick5)
        self.pushButton_6.clicked.connect(self.btnclick6)
        self.pushButton_7.clicked.connect(self.btnclick7)
        self.pushButton_8.clicked.connect(self.btnclick8)
        self.pushButton_9.clicked.connect(self.btnclick9)
        self.pushButton_10.clicked.connect(self.btnclick10)
        
      
    def btnclick1(self):
        m=model()
        m.getComentsData(lst_id[0])
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    def btnclick2(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    def btnclick3(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    def btnclick4(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    def btnclick5(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    def btnclick6(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    def btnclick7(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    def btnclick8(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    def btnclick9(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    def btnclick10(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    def setVideo(self, lst, lst_id1 ):
        lst_id=lst_id1
        _translate = QtCore.QCoreApplication.translate
       # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
       # self.pushButton_11.setText(_translate("MainWindow", "Search"))
        self.pushButton.setText(_translate("MainWindow", lst[0]))
        self.pushButton_2.setText(_translate("MainWindow", lst[1]))
        self.pushButton_3.setText(_translate("MainWindow", lst[2]))
        self.pushButton_4.setText(_translate("MainWindow", lst[3]))
        self.pushButton_5.setText(_translate("MainWindow", lst[4]))
        self.pushButton_6.setText(_translate("MainWindow", lst[5]))
        self.pushButton_7.setText(_translate("MainWindow", lst[6]))
        self.pushButton_8.setText(_translate("MainWindow", lst[7]))
        self.pushButton_9.setText(_translate("MainWindow", lst[8]))
        self.pushButton_10.setText(_translate("MainWindow", lst[9]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_11.setText(_translate("MainWindow", "Search"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

