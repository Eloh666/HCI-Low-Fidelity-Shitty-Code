# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'whip.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import catalog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setGeometry(200,200,1470,1030)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 140, 651, 781))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Layer 1.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 670, 211, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 710, 211, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 870, 490, 200))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 310, 101, 71))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 310, 101, 71))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(700, 30, 801, 931))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("victorias-secret-blonde-heather-cotton-thermal-vneck-sweater-product-1-14395986-276354505.jpeg")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 10, 101, 101))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 10, 101, 101))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 10, 101, 101))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 930, 161, 81))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 270, 50, 50))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1474, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.setupLogic()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "TextLabel", None))
        self.label_3.setText(_translate("MainWindow", "", None))
        self.label_4.setText(_translate("MainWindow", "", None))
        self.label_3.setStyleSheet("color: white;"
                                   "font-size: 15px;")
        self.label_4.setStyleSheet("color: black;"
                                   "font-size: 25px;")
        iconCart = QIcon("cart.png")
        iconCartPlus = QIcon("cartPlus.png")
        iconCheckout = QIcon("checkout.png")
        iconJacket = QIcon("jacket.png")
        iconCatal = QIcon("catal.png")
        iconAsk = QIcon("askToBring.png")
        iconHelp = QIcon("help.png")
        iconRemove = QIcon("remove.png")
        self.pushButton.setIcon(iconCart)
        self.pushButton_6.setIcon(iconCart)
        self.pushButton_2.setIcon(iconHelp)
        self.pushButton_3.setIcon(iconAsk)
        self.pushButton_4.setIcon(iconCatal)
        self.pushButton_5.setIcon(iconCheckout)
        self.pushButton_7.setIcon(iconRemove)
        self.pushButton.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_2.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_3.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_4.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_5.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_6.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))

    def setupLogic(self):
        self.pushButton.clicked.connect(self.spawnCatalog)
        self.pushButton_7.clicked.connect(self.removeArticle)

    def spawnCatalog(self):
        self.myOtherWindow = catalog.Catalog(self.pushButton, self.label_5, self.pushButton_5, self.label_4, self.label_3)
        self.myOtherWindow.setWindowModality(Qt.ApplicationModal)
        self.myOtherWindow.show()

    def removeArticle(self):
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(
            "victorias-secret-blonde-heather-cotton-thermal-vneck-sweater-product-1-14395986-276354505.jpeg")))
        iconCart = QIcon("cart.png")
        self.pushButton.setIcon(iconCart)
        self.label_3.setText(_translate("MainWindow", "", None))
        self.pushButton_5.setEnabled(False)
        self.label_4.setText(_translate("MainWindow", "", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

