# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '../platforms'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 40, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 290, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 130, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 290, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txt_plaintext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plaintext.setGeometry(QtCore.QRect(110, 130, 281, 101))
        self.txt_plaintext.setObjectName("txt_plaintext")
        self.txt_ciphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_ciphertext.setGeometry(QtCore.QRect(110, 290, 281, 101))
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(470, 130, 291, 101))
        self.txt_sign.setObjectName("txt_sign")
        self.txt_verify = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_verify.setGeometry(QtCore.QRect(470, 290, 291, 101))
        self.txt_verify.setObjectName("txt_verify")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(120, 440, 93, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(270, 440, 93, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(650, 440, 93, 28))
        self.btn_verify.setObjectName("btn_verify")
        self.btn_generatekeys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generatekeys.setGeometry(QtCore.QRect(360, 500, 93, 28))
        self.btn_generatekeys.setObjectName("btn_generatekeys")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(470, 440, 93, 28))
        self.btn_sign.setObjectName("btn_sign")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "RSA"))
        self.label_2.setText(_translate("MainWindow", "Plain text:"))
        self.label_3.setText(_translate("MainWindow", "Cipher text:"))
        self.label_4.setText(_translate("MainWindow", "Sign:"))
        self.label_5.setText(_translate("MainWindow", "Signature:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decypt"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.btn_generatekeys.setText(_translate("MainWindow", "Generate key"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
