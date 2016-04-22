# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

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

class Catalog(QMainWindow):

    def __init__(self, itemButton, label, checkoutButton, checkoutLabel, itemLabel):
        self.slot = itemButton
        self.checkoutButton = checkoutButton
        self.checkoutLabel = checkoutLabel
        self.picture = label
        self.itemLabel = itemLabel
        QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("self"))
        self.resize(1261, 283)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 10, 1191, 221))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("jackets.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(170, 182, 61, 41))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("cartPlus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 180, 61, 41))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 180, 61, 41))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 180, 61, 41))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(970, 180, 61, 41))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(1160, 180, 61, 41))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.pushButton_7 = QtGui.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(490, 230, 111, 41))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self)
        self.pushButton_8.setGeometry(QtCore.QRect(690, 230, 61, 41))
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 70, 41, 91))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self)
        self.pushButton_10.setGeometry(QtCore.QRect(1220, 60, 41, 91))
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(770, 240, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_11 = QtGui.QPushButton(self)
        self.pushButton_11.setGeometry(QtCore.QRect(820, 230, 71, 41))
        self.pushButton_11.setText(_fromUtf8(""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        iconPlus = QIcon("plus.png")
        iconMinus = QIcon("minus.png")
        iconBack = QIcon("back.png")
        iconPrev = QIcon("prev.png")
        iconNext = QIcon("next.png")

        self.pushButton_7.setIcon(iconBack)
        self.pushButton_8.setIcon(iconPlus)
        self.pushButton_9.setIcon(iconPrev)
        self.pushButton_10.setIcon(iconNext)
        self.pushButton_11.setIcon(iconMinus)
        self.pushButton_7.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_8.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_9.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_10.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_11.setIconSize(QtCore.QSize(70, 70))

        self.pushButton.clicked.connect(self.addToChart)
        self.pushButton_7.clicked.connect(self.close)


    def addToChart(self):
        self.picture.setPixmap(QtGui.QPixmap(
            _fromUtf8("victorias-secret-black-leather-bomber-jacket-product-1-13840923-032944154")))
        icon = QIcon("jacket.png")
        self.checkoutLabel.setText(_translate("MainWindow", "Checkout: £666", None))
        self.itemLabel.setText(_translate("MainWindow", "Leather Jacket:               £666", None))
        self.checkoutButton.setEnabled(True)
        self.slot.setIcon(icon)
        self.slot.setIconSize(QtCore.QSize(70, 70))
        self.close()

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "self", None))
        self.label_2.setText(_translate("self", "Size 45", None))

