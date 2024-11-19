# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criptomoedas.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 590)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#ffffff;")
        self.label.setObjectName("label")
        self.BTC = QtWidgets.QPushButton(self.centralwidget)
        self.BTC.setGeometry(QtCore.QRect(240, 190, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BTC.setFont(font)
        self.BTC.setStyleSheet("background:transparent;color:white;")
        self.BTC.setObjectName("BTC")
        self.dero = QtWidgets.QPushButton(self.centralwidget)
        self.dero.setGeometry(QtCore.QRect(450, 190, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dero.setFont(font)
        self.dero.setStyleSheet("background:transparent;color:white;")
        self.dero.setObjectName("dero")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.dero)
        self.shiba = QtWidgets.QPushButton(self.centralwidget)
        self.shiba.setGeometry(QtCore.QRect(240, 440, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.shiba.setFont(font)
        self.shiba.setStyleSheet("background:transparent;color:white;")
        self.shiba.setObjectName("shiba")
        self.dogecoin = QtWidgets.QPushButton(self.centralwidget)
        self.dogecoin.setGeometry(QtCore.QRect(450, 310, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dogecoin.setFont(font)
        self.dogecoin.setStyleSheet("background:transparent;color:white;")
        self.dogecoin.setObjectName("dogecoin")
        self.buttonGroup.addButton(self.dogecoin)
        self.solana = QtWidgets.QPushButton(self.centralwidget)
        self.solana.setGeometry(QtCore.QRect(240, 310, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.solana.setFont(font)
        self.solana.setStyleSheet("background:transparent;color:white;")
        self.solana.setObjectName("solana")
        self.zcash = QtWidgets.QPushButton(self.centralwidget)
        self.zcash.setGeometry(QtCore.QRect(630, 440, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.zcash.setFont(font)
        self.zcash.setStyleSheet("background:transparent;color:white;")
        self.zcash.setObjectName("zcash")
        self.monero = QtWidgets.QPushButton(self.centralwidget)
        self.monero.setGeometry(QtCore.QRect(630, 190, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.monero.setFont(font)
        self.monero.setStyleSheet("background:transparent;color:white;")
        self.monero.setObjectName("monero")
        self.buttonGroup.addButton(self.monero)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 130, 61, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../Pictures/giphy.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 120, 61, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../Pictures/dero.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 370, 61, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../Pictures/shiba.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 120, 61, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../Pictures/monero.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 370, 51, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../../Pictures/zcash.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 250, 51, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../../../Pictures/Dogecoin_Logo.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 250, 91, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../../../Pictures/Solana-Logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(640, 250, 61, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../../Pictures/usdt.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(460, 370, 61, 51))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../../../Pictures/xelis.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.usdt = QtWidgets.QPushButton(self.centralwidget)
        self.usdt.setGeometry(QtCore.QRect(630, 310, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.usdt.setFont(font)
        self.usdt.setStyleSheet("background:transparent;color:white;")
        self.usdt.setObjectName("usdt")
        self.buttonGroup.addButton(self.usdt)
        self.xelis = QtWidgets.QPushButton(self.centralwidget)
        self.xelis.setGeometry(QtCore.QRect(450, 440, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.xelis.setFont(font)
        self.xelis.setStyleSheet("background:transparent;color:white;")
        self.xelis.setObjectName("xelis")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 921, 541))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../../../Pictures/mineracao-de-criptomoedas-min.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.Resultado = QtWidgets.QLabel(self.centralwidget)
        self.Resultado.setGeometry(QtCore.QRect(430, 500, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Resultado.setFont(font)
        self.Resultado.setStyleSheet("color:#ffffff;")
        self.Resultado.setObjectName("Resultado")
        self.label_11.raise_()
        self.label.raise_()
        self.BTC.raise_()
        self.shiba.raise_()
        self.dogecoin.raise_()
        self.solana.raise_()
        self.zcash.raise_()
        self.monero.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.usdt.raise_()
        self.xelis.raise_()
        self.dero.raise_()
        self.Resultado.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 21))
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
        self.label.setText(_translate("MainWindow", "Mineração Criptomoeda CPU"))
        self.BTC.setText(_translate("MainWindow", "Bitcoin BTC"))
        self.dero.setText(_translate("MainWindow", "Dero"))
        self.shiba.setText(_translate("MainWindow", "ShibaInu"))
        self.dogecoin.setText(_translate("MainWindow", "Dogecoin"))
        self.solana.setText(_translate("MainWindow", "Solana"))
        self.zcash.setText(_translate("MainWindow", "Zcash"))
        self.monero.setText(_translate("MainWindow", "Monero XMR"))
        self.usdt.setText(_translate("MainWindow", "USDT"))
        self.xelis.setText(_translate("MainWindow", "Xélis"))
        self.Resultado.setText(_translate("MainWindow", "..."))
