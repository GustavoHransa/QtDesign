# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exerc01.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(263, 276)
        MainWindow.setStyleSheet("background-color:#93c899;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_num1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_num1.setGeometry(QtCore.QRect(100, 90, 51, 20))
        self.lineEdit_num1.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_num1.setObjectName("lineEdit_num1")
        self.lineEdit_num2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_num2.setGeometry(QtCore.QRect(100, 140, 51, 20))
        self.lineEdit_num2.setStyleSheet("background-color:#ffffff;")
        self.lineEdit_num2.setObjectName("lineEdit_num2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(90, 220, 81, 21))
        self.label_resultado.setText("")
        self.label_resultado.setObjectName("label_resultado")
        self.pushButton_somar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_somar.setGeometry(QtCore.QRect(90, 180, 75, 23))
        self.pushButton_somar.setObjectName("pushButton_somar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 263, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Somar dois números inteiros:"))
        self.label_2.setText(_translate("MainWindow", "Primeiro número"))
        self.label_3.setText(_translate("MainWindow", "Segundo  número"))
        self.pushButton_somar.setText(_translate("MainWindow", "Calcular"))