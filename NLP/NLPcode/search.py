# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\search.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from showvid import Ui_MainWindow
from default_class import model

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(666, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 51))
        self.label.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(280, 10, 301, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 10, 75, 31))
        self.pushButton.setStyleSheet("background-color: rgb(72, 144, 216);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("2.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 651, 411))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("unnamed.png"))
        self.label_3.setObjectName("label_3")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 21))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)
        self.pushButton.clicked.connect(self.btnclick)
    def btnclick(self):
        m=model()
        lst, lst_id=m.start(self.textEdit.toPlainText())
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.setVideo(lst, lst_id)
        MainWindow.exec_()
    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow1", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())

