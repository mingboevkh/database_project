# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbConnection.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_connectDatabase(object):
    def setupUi(self, connectDatabase):
        connectDatabase.setObjectName("connectDatabase")
        connectDatabase.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(connectDatabase)
        self.centralwidget.setObjectName("centralwidget")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(80, 290, 241, 51))
        self.connectButton.setObjectName("connectButton")
        self.passwordText = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordText.setGeometry(QtCore.QRect(80, 100, 241, 41))
        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordText.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordText.setObjectName("passwordText")
        self.userNameText = QtWidgets.QLineEdit(self.centralwidget)
        self.userNameText.setGeometry(QtCore.QRect(80, 40, 241, 41))
        self.userNameText.setAlignment(QtCore.Qt.AlignCenter)
        self.userNameText.setObjectName("userNameText")
        self.databaseNameText = QtWidgets.QLineEdit(self.centralwidget)
        self.databaseNameText.setGeometry(QtCore.QRect(80, 160, 241, 41))
        self.databaseNameText.setAlignment(QtCore.Qt.AlignCenter)
        self.databaseNameText.setObjectName("databaseNameText")
        self.hostNameText = QtWidgets.QLineEdit(self.centralwidget)
        self.hostNameText.setGeometry(QtCore.QRect(80, 220, 241, 41))
        self.hostNameText.setAlignment(QtCore.Qt.AlignCenter)
        self.hostNameText.setObjectName("hostNameText")
        connectDatabase.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(connectDatabase)
        self.statusbar.setObjectName("statusbar")
        connectDatabase.setStatusBar(self.statusbar)

        self.retranslateUi(connectDatabase)
        QtCore.QMetaObject.connectSlotsByName(connectDatabase)

    def retranslateUi(self, connectDatabase):
        _translate = QtCore.QCoreApplication.translate
        connectDatabase.setWindowTitle(_translate("connectDatabase", "Database connection"))
        self.connectButton.setText(_translate("connectDatabase", "Connect"))
        self.passwordText.setPlaceholderText(_translate("connectDatabase", "Password"))
        self.userNameText.setPlaceholderText(_translate("connectDatabase", "User name"))
        self.databaseNameText.setPlaceholderText(_translate("connectDatabase", "Database name"))
        self.hostNameText.setPlaceholderText(_translate("connectDatabase", "Host"))


