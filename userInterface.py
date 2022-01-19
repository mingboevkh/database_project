# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userInterface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1021, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.LoungeBarsTab = QtWidgets.QWidget()
        self.LoungeBarsTab.setObjectName("LoungeBarsTab")
        self.loungeBarsTable = QtWidgets.QTableWidget(self.LoungeBarsTab)
        self.loungeBarsTable.setGeometry(QtCore.QRect(40, 105, 920, 410))
        self.loungeBarsTable.setObjectName("loungeBarsTable")
        self.loungeBarsTable.setColumnCount(0)
        self.loungeBarsTable.setRowCount(0)
        self.nameLoungeBarText = QtWidgets.QLineEdit(self.LoungeBarsTab)
        self.nameLoungeBarText.setGeometry(QtCore.QRect(570, 60, 241, 30))
        self.nameLoungeBarText.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLoungeBarText.setObjectName("nameLoungeBarText")
        self.addLoungeBarButton = QtWidgets.QPushButton(self.LoungeBarsTab)
        self.addLoungeBarButton.setGeometry(QtCore.QRect(830, 20, 60, 30))
        self.addLoungeBarButton.setObjectName("addLoungeBarButton")
        self.clearLoungeBarButton = QtWidgets.QPushButton(self.LoungeBarsTab)
        self.clearLoungeBarButton.setGeometry(QtCore.QRect(900, 20, 60, 30))
        self.clearLoungeBarButton.setObjectName("clearLoungeBarButton")
        self.searchLoungeButton = QtWidgets.QPushButton(self.LoungeBarsTab)
        self.searchLoungeButton.setGeometry(QtCore.QRect(830, 60, 60, 30))
        self.searchLoungeButton.setObjectName("searchLoungeButton")
        self.deleteLoungeBarButton = QtWidgets.QPushButton(self.LoungeBarsTab)
        self.deleteLoungeBarButton.setGeometry(QtCore.QRect(900, 60, 60, 30))
        self.deleteLoungeBarButton.setObjectName("deleteLoungeBarButton")
        self.addressLoungeText = QtWidgets.QLineEdit(self.LoungeBarsTab)
        self.addressLoungeText.setGeometry(QtCore.QRect(40, 60, 361, 30))
        self.addressLoungeText.setAlignment(QtCore.Qt.AlignCenter)
        self.addressLoungeText.setObjectName("addressLoungeText")
        self.supplierLoungeText = QtWidgets.QLineEdit(self.LoungeBarsTab)
        self.supplierLoungeText.setGeometry(QtCore.QRect(320, 20, 301, 30))
        self.supplierLoungeText.setAlignment(QtCore.Qt.AlignCenter)
        self.supplierLoungeText.setObjectName("supplierLoungeText")
        self.ownerNameLoungeText = QtWidgets.QLineEdit(self.LoungeBarsTab)
        self.ownerNameLoungeText.setGeometry(QtCore.QRect(40, 20, 251, 30))
        self.ownerNameLoungeText.setAlignment(QtCore.Qt.AlignCenter)
        self.ownerNameLoungeText.setObjectName("ownerNameLoungeText")
        self.commonTobaccoText = QtWidgets.QLineEdit(self.LoungeBarsTab)
        self.commonTobaccoText.setGeometry(QtCore.QRect(650, 20, 161, 30))
        self.commonTobaccoText.setAlignment(QtCore.Qt.AlignCenter)
        self.commonTobaccoText.setObjectName("commonTobaccoText")
        self.label = QtWidgets.QLabel(self.LoungeBarsTab)
        self.label.setGeometry(QtCore.QRect(420, 70, 131, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.LoungeBarsTab, "")
        self.OwnersTab = QtWidgets.QWidget()
        self.OwnersTab.setObjectName("OwnersTab")
        self.ownerNameText = QtWidgets.QLineEdit(self.OwnersTab)
        self.ownerNameText.setGeometry(QtCore.QRect(40, 20, 321, 30))
        self.ownerNameText.setAlignment(QtCore.Qt.AlignCenter)
        self.ownerNameText.setObjectName("ownerNameText")
        self.addOwnersButton = QtWidgets.QPushButton(self.OwnersTab)
        self.addOwnersButton.setGeometry(QtCore.QRect(700, 20, 120, 30))
        self.addOwnersButton.setObjectName("addOwnersButton")
        self.deleteOwnersButton = QtWidgets.QPushButton(self.OwnersTab)
        self.deleteOwnersButton.setGeometry(QtCore.QRect(840, 60, 120, 30))
        self.deleteOwnersButton.setObjectName("deleteOwnersButton")
        self.searchOwnersButton = QtWidgets.QPushButton(self.OwnersTab)
        self.searchOwnersButton.setGeometry(QtCore.QRect(700, 60, 120, 30))
        self.searchOwnersButton.setObjectName("searchOwnersButton")
        self.clearOwnersButton = QtWidgets.QPushButton(self.OwnersTab)
        self.clearOwnersButton.setGeometry(QtCore.QRect(840, 20, 120, 30))
        self.clearOwnersButton.setObjectName("clearOwnersButton")
        self.emailText = QtWidgets.QLineEdit(self.OwnersTab)
        self.emailText.setGeometry(QtCore.QRect(400, 60, 281, 30))
        self.emailText.setAlignment(QtCore.Qt.AlignCenter)
        self.emailText.setObjectName("emailText")
        self.ownersTable = QtWidgets.QTableWidget(self.OwnersTab)
        self.ownersTable.setGeometry(QtCore.QRect(40, 105, 920, 410))
        self.ownersTable.setObjectName("ownersTable")
        self.ownersTable.setColumnCount(0)
        self.ownersTable.setRowCount(0)
        self.foundationDate = QtWidgets.QDateEdit(self.OwnersTab)
        self.foundationDate.setGeometry(QtCore.QRect(520, 20, 161, 31))
        self.foundationDate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.foundationDate.setAlignment(QtCore.Qt.AlignCenter)
        self.foundationDate.setDate(QtCore.QDate(2021, 12, 17))
        self.foundationDate.setObjectName("foundationDate")
        self.label_2 = QtWidgets.QLabel(self.OwnersTab)
        self.label_2.setGeometry(QtCore.QRect(400, 30, 111, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.OwnersTab)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 171, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.OwnersTab, "")
        self.SuppliersTab = QtWidgets.QWidget()
        self.SuppliersTab.setObjectName("SuppliersTab")
        self.organisationText = QtWidgets.QLineEdit(self.SuppliersTab)
        self.organisationText.setGeometry(QtCore.QRect(40, 20, 401, 30))
        self.organisationText.setAlignment(QtCore.Qt.AlignCenter)
        self.organisationText.setObjectName("organisationText")
        self.addSuppliersButton = QtWidgets.QPushButton(self.SuppliersTab)
        self.addSuppliersButton.setGeometry(QtCore.QRect(700, 20, 120, 30))
        self.addSuppliersButton.setObjectName("addSuppliersButton")
        self.deleteSuppliersButton = QtWidgets.QPushButton(self.SuppliersTab)
        self.deleteSuppliersButton.setGeometry(QtCore.QRect(840, 60, 120, 30))
        self.deleteSuppliersButton.setObjectName("deleteSuppliersButton")
        self.searchSuppliersButton = QtWidgets.QPushButton(self.SuppliersTab)
        self.searchSuppliersButton.setGeometry(QtCore.QRect(700, 60, 120, 30))
        self.searchSuppliersButton.setObjectName("searchSuppliersButton")
        self.volumePurchaseText = QtWidgets.QLineEdit(self.SuppliersTab)
        self.volumePurchaseText.setGeometry(QtCore.QRect(470, 20, 181, 30))
        self.volumePurchaseText.setAlignment(QtCore.Qt.AlignCenter)
        self.volumePurchaseText.setObjectName("volumePurchaseText")
        self.clearSuppliersButton = QtWidgets.QPushButton(self.SuppliersTab)
        self.clearSuppliersButton.setGeometry(QtCore.QRect(840, 20, 120, 30))
        self.clearSuppliersButton.setObjectName("clearSuppliersButton")
        self.suppliersTable = QtWidgets.QTableWidget(self.SuppliersTab)
        self.suppliersTable.setGeometry(QtCore.QRect(40, 105, 920, 410))
        self.suppliersTable.setObjectName("suppliersTable")
        self.suppliersTable.setColumnCount(0)
        self.suppliersTable.setRowCount(0)
        self.phoneNumberText = QtWidgets.QLineEdit(self.SuppliersTab)
        self.phoneNumberText.setGeometry(QtCore.QRect(40, 60, 401, 30))
        self.phoneNumberText.setText("")
        self.phoneNumberText.setAlignment(QtCore.Qt.AlignCenter)
        self.phoneNumberText.setObjectName("phoneNumberText")
        self.label_7 = QtWidgets.QLabel(self.SuppliersTab)
        self.label_7.setGeometry(QtCore.QRect(460, 65, 221, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.SuppliersTab)
        self.label_4.setGeometry(QtCore.QRect(655, 24, 20, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.SuppliersTab, "")
        self.RatingsTab = QtWidgets.QWidget()
        self.RatingsTab.setObjectName("RatingsTab")
        self.ratingsTable = QtWidgets.QTableWidget(self.RatingsTab)
        self.ratingsTable.setGeometry(QtCore.QRect(40, 105, 920, 410))
        self.ratingsTable.setObjectName("ratingsTable")
        self.ratingsTable.setColumnCount(0)
        self.ratingsTable.setRowCount(0)
        self.feedbackText = QtWidgets.QLineEdit(self.RatingsTab)
        self.feedbackText.setGeometry(QtCore.QRect(480, 20, 481, 61))
        self.feedbackText.setAlignment(QtCore.Qt.AlignCenter)
        self.feedbackText.setObjectName("feedbackText")
        self.addRatingsButton = QtWidgets.QPushButton(self.RatingsTab)
        self.addRatingsButton.setGeometry(QtCore.QRect(40, 50, 120, 30))
        self.addRatingsButton.setObjectName("addRatingsButton")
        self.gradeText = QtWidgets.QLineEdit(self.RatingsTab)
        self.gradeText.setGeometry(QtCore.QRect(340, 50, 111, 30))
        self.gradeText.setAlignment(QtCore.Qt.AlignCenter)
        self.gradeText.setObjectName("gradeText")
        self.label_8 = QtWidgets.QLabel(self.RatingsTab)
        self.label_8.setGeometry(QtCore.QRect(340, 30, 111, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.loungeBarRatingsText = QtWidgets.QLineEdit(self.RatingsTab)
        self.loungeBarRatingsText.setGeometry(QtCore.QRect(180, 50, 141, 30))
        self.loungeBarRatingsText.setAlignment(QtCore.Qt.AlignCenter)
        self.loungeBarRatingsText.setObjectName("loungeBarRatingsText")
        self.tabWidget.addTab(self.RatingsTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionClear_table = QtWidgets.QAction(MainWindow)
        self.actionClear_table.setObjectName("actionClear_table")
        self.actionClear_all = QtWidgets.QAction(MainWindow)
        self.actionClear_all.setObjectName("actionClear_all")
        self.actionClear_Tables = QtWidgets.QAction(MainWindow)
        self.actionClear_Tables.setObjectName("actionClear_Tables")
        self.actionDelete_database = QtWidgets.QAction(MainWindow)
        self.actionDelete_database.setObjectName("actionDelete_database")
        self.menuDatabase.addAction(self.actionConnect)
        self.menuDatabase.addAction(self.actionDelete_database)
        self.menuDatabase.addAction(self.actionClear_Tables)
        self.menubar.addAction(self.menuDatabase.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interface"))
        self.nameLoungeBarText.setPlaceholderText(_translate("MainWindow", "Name of the lounge bar"))
        self.addLoungeBarButton.setText(_translate("MainWindow", "Add"))
        self.clearLoungeBarButton.setText(_translate("MainWindow", "Clear"))
        self.searchLoungeButton.setText(_translate("MainWindow", "Search"))
        self.deleteLoungeBarButton.setText(_translate("MainWindow", "Delete"))
        self.addressLoungeText.setPlaceholderText(_translate("MainWindow", "Address"))
        self.supplierLoungeText.setPlaceholderText(_translate("MainWindow", "Supplier"))
        self.ownerNameLoungeText.setPlaceholderText(_translate("MainWindow", "Owner\'s name"))
        self.commonTobaccoText.setPlaceholderText(_translate("MainWindow", "Common tobacco"))
        self.label.setText(_translate("MainWindow", "Search and delete by"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LoungeBarsTab), _translate("MainWindow", "Lounge bars"))
        self.ownerNameText.setPlaceholderText(_translate("MainWindow", "Owner\'s name"))
        self.addOwnersButton.setText(_translate("MainWindow", "Add"))
        self.deleteOwnersButton.setText(_translate("MainWindow", "Delete"))
        self.searchOwnersButton.setText(_translate("MainWindow", "Search"))
        self.clearOwnersButton.setText(_translate("MainWindow", "Clear"))
        self.emailText.setPlaceholderText(_translate("MainWindow", "email"))
        self.label_2.setText(_translate("MainWindow", "Foundation date"))
        self.label_3.setText(_translate("MainWindow", "Search and delete by email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OwnersTab), _translate("MainWindow", "Owners"))
        self.organisationText.setPlaceholderText(_translate("MainWindow", "Organisation"))
        self.addSuppliersButton.setText(_translate("MainWindow", "Add"))
        self.deleteSuppliersButton.setText(_translate("MainWindow", "Delete"))
        self.searchSuppliersButton.setText(_translate("MainWindow", "Search"))
        self.volumePurchaseText.setPlaceholderText(_translate("MainWindow", "Volume of purchase"))
        self.clearSuppliersButton.setText(_translate("MainWindow", "Clear"))
        self.phoneNumberText.setPlaceholderText(_translate("MainWindow", "Phone number"))
        self.label_7.setText(_translate("MainWindow", "Search and delete by phone number"))
        self.label_4.setText(_translate("MainWindow", "$"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SuppliersTab), _translate("MainWindow", "Suppliers"))
        self.feedbackText.setPlaceholderText(_translate("MainWindow", "Feedback"))
        self.addRatingsButton.setText(_translate("MainWindow", "Add"))
        self.gradeText.setPlaceholderText(_translate("MainWindow", "grade"))
        self.label_8.setText(_translate("MainWindow", "rate from 0 to 10"))
        self.loungeBarRatingsText.setPlaceholderText(_translate("MainWindow", "Lounge bar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RatingsTab), _translate("MainWindow", "Ratings"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionClear_table.setText(_translate("MainWindow", "Clear table"))
        self.actionClear_all.setText(_translate("MainWindow", "Clear all"))
        self.actionClear_Tables.setText(_translate("MainWindow", "Clear Tables"))
        self.actionDelete_database.setText(_translate("MainWindow", "Delete"))

