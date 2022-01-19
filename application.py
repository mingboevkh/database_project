from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem
from database import DataBase

import userInterface
import dbConnection


class ConnectWindow(QtWidgets.QMainWindow, dbConnection.Ui_connectDatabase):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)

        self.app = app
        self.connectButton.clicked.connect(self.connect_to)

    def connect_to(self):
        self.app.connect_to_database(self.userNameText.text(), self.passwordText.text(), self.databaseNameText.text())
        self.close()


class MainWindow(QtWidgets.QMainWindow, userInterface.Ui_MainWindow):
    def __init__(self, ):
        super().__init__()
        self.setupUi(self)
        self.db = None
        self.changed = False
        self.connectWindow = ConnectWindow(self)
        self.columns_lounge_bars = ['name', 'address', 'supplier', 'owner', 'common_tobacco']
        self.columns_ratings = ['lounge_bar_name', 'feedback', 'grade']
        self.columns_owners = ['name', 'foundation_date', 'email']
        self.columns_suppliers = ['organisation', 'volume_purchase_per_month', 'phone_number']

        # Toolbar
        self.actionConnect.triggered.connect(self.connectWindow.show)
        self.actionClear_Tables.triggered.connect(self.clear_all)
        self.actionDelete_database.triggered.connect(self.drop_database)

        # Owners
        self.ownersTable.setColumnCount(len(self.columns_owners))
        self.ownersTable.setHorizontalHeaderLabels(self.columns_owners)
        self.ownersTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addOwnersButton.clicked.connect(self.add_owner)
        self.deleteOwnersButton.clicked.connect(self.delete_owner)
        self.searchOwnersButton.clicked.connect(self.search_owner)
        self.clearOwnersButton.clicked.connect(self.delete_owners)
        self.ownersTable.itemChanged.connect(self.update_owner)

        # Suppliers
        self.suppliersTable.setColumnCount(len(self.columns_suppliers))
        self.suppliersTable.setHorizontalHeaderLabels(self.columns_suppliers)
        self.suppliersTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addSuppliersButton.clicked.connect(self.add_supplier)
        self.deleteSuppliersButton.clicked.connect(self.delete_supplier)
        self.searchSuppliersButton.clicked.connect(self.search_supplier)
        self.clearSuppliersButton.clicked.connect(self.delete_suppliers)
        self.suppliersTable.itemChanged.connect(self.update_supplier)

        # Ratings
        self.ratingsTable.setColumnCount(len(self.columns_ratings))
        self.ratingsTable.setHorizontalHeaderLabels(self.columns_ratings)
        self.ratingsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addRatingsButton.clicked.connect(self.add_rating)

        # Lounge bars
        self.loungeBarsTable.setColumnCount(len(self.columns_lounge_bars))
        self.loungeBarsTable.setHorizontalHeaderLabels(self.columns_lounge_bars)
        self.loungeBarsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addLoungeBarButton.clicked.connect(self.add_lounge_bar)
        self.deleteLoungeBarButton.clicked.connect(self.delete_lounge_bar)
        self.searchLoungeButton.clicked.connect(self.search_lounge_bar)
        self.clearLoungeBarButton.clicked.connect(self.delete_lounge_bars)
        self.loungeBarsTable.itemChanged.connect(self.update_lounge_bar)

    def connect_to_database(self, user, pswd, name, host='localhost'):
        self.db = DataBase(
            user=user,
            password=pswd,
            name=name,
            host=host
        )
        self.lounge_bars = self.db.get_lounge_bars()
        self.owners = self.db.get_owners()
        self.suppliers = self.db.get_suppliers()
        self.ratings = self.db.get_ratings()
        self.set_data(self.loungeBarsTable, self.columns_lounge_bars, self.lounge_bars)
        self.set_data(self.ownersTable, self.columns_owners, self.owners)
        self.set_data(self.suppliersTable, self.columns_suppliers, self.suppliers)
        self.set_data(self.ratingsTable, self.columns_ratings, self.ratings)

    def drop_database(self):
        self.db.drop_database()
        self.connectWindow.show()

    def clear_all(self):
        self.db.delete_lounge_bars()
        self.lounge_bars = self.db.get_lounge_bars()
        self.set_data(self.loungeBarsTable, self.columns_lounge_bars, self.lounge_bars)

        self.db.delete_owners()
        self.owners = self.db.get_owners()
        self.set_data(self.ownersTable, self.columns_owners, self.owners)

        self.db.delete_suppliers()
        self.suppliers = self.db.get_suppliers()
        self.set_data(self.suppliersTable, self.columns_suppliers, self.suppliers)

        self.db.delete_ratings()
        self.ratings = self.db.get_ratings()
        self.set_data(self.ratingsTable, self.columns_ratings, self.ratings)

    def set_data(self, table, columns, data):
        self.changed = True
        if data is not None:
            table.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, col in enumerate(columns):
                    table.setItem(i, j, QTableWidgetItem(str(row[col])))
        else:
            table.setRowCount(0)
        self.changed = False

    # ----------------- Lounge bar functions --------------------
    def add_lounge_bar(self):
        self.db.add_lounge_bar(
            name=self.nameLoungeBarText.text(),
            address=self.addressLoungeText.text(),
            supplier=self.supplierLoungeText.text(),
            owner=self.ownerNameLoungeText.text(),
            common_tobacco=self.commonTobaccoText.text()
        )
        self.lounge_bars = self.db.get_lounge_bars()
        self.set_data(self.loungeBarsTable, self.columns_lounge_bars, self.lounge_bars)
        self.nameLoungeBarText.clear()
        self.ownerNameLoungeText.clear()
        self.supplierLoungeText.clear()
        self.commonTobaccoText.clear()
        self.addressLoungeText.clear()

    def delete_lounge_bar(self):
        if len(self.loungeBarsTable.selectedIndexes()):
            for i in self.loungeBarsTable.selectedIndexes():
                self.db.delete_lounge_bar(self.lounge_bars[i.row()]['name'])
                self.lounge_bars = self.db.get_lounge_bars()
                self.set_data(self.loungeBarsTable, self.columns_lounge_bars, self.lounge_bars)

    def delete_lounge_bars(self):
        self.db.delete_lounge_bars()
        self.lounge_bars = self.db.get_lounge_bars()
        self.set_data(self.loungeBarsTable, self.columns_lounge_bars, self.lounge_bars)

    def search_lounge_bar(self):
        if (self.nameLoungeBarText.text() == ''):
            self.lounge_bars = self.db.get_lounge_bars()
        else:
            self.lounge_bars = self.db.search_lounge_bar(self.nameLoungeBarText.text())
        self.set_data(self.loungeBarsTable, self.columns_lounge_bars, self.lounge_bars)

    def update_lounge_bar(self, item):
        if not self.changed:
            self.db.update_lounge_bar(item.text(), self.lounge_bars[item.row()]['name'])
            self.lounge_bars = self.db.get_lounge_bars()
            self.set_data(self.loungeBarsTable, self.columns_lounge_bars, self.lounge_bars)
            self.ratings = self.db.get_ratings()
            self.set_data(self.ratingsTable, self.columns_ratings, self.ratings)

    # --------------------- Owner functions -----------------------
    def add_owner(self):
        self.db.add_owner(
            owner_name=self.ownerNameText.text(),
            f_date=self.foundationDate.text(),
            email=self.emailText.text()
        )
        self.owners = self.db.get_owners()
        self.set_data(self.ownersTable, self.columns_owners, self.owners)
        self.ownerNameText.clear()
        self.emailText.clear()

    def delete_owner(self):
        if len(self.ownersTable.selectedIndexes()):
            for i in self.ownersTable.selectedIndexes():
                self.db.delete_owner(self.owners[i.row()]['name'])
                self.owners = self.db.get_owners()
                self.set_data(self.ownersTable, self.columns_owners, self.owners)

    def delete_owners(self):
        self.db.delete_owners()
        self.owners = self.db.get_owners()
        self.set_data(self.ownersTable, self.columns_owners, self.owners)

    def search_owner(self):
        if (self.emailText.text() == ''):
            self.owners = self.db.get_owners()
        else:
            self.owners = self.db.search_owner(self.emailText.text())
        self.set_data(self.ownersTable, self.columns_owners, self.owners)

    def update_owner(self, item):
        if not self.changed:
            self.db.update_owner(item.text(), self.owners[item.row()]['name'])
            self.owners = self.db.get_owners()
            self.set_data(self.ownersTable, self.columns_owners, self.owners)
            self.lounge_bars = self.db.get_lounge_bars()
            self.set_data(self.loungeBarsTable, self.columns_lounge_bars, self.lounge_bars)

    # --------------------- Supplier functions -----------------------
    def add_supplier(self):
        self.db.add_supplier(
            organisation=self.organisationText.text(),
            volume_purchase=self.volumePurchaseText.text(),
            phone_number=self.phoneNumberText.text()
        )
        self.suppliers = self.db.get_suppliers()
        self.set_data(self.suppliersTable, self.columns_suppliers, self.suppliers)
        self.organisationText.clear()
        self.volumePurchaseText.clear()
        self.phoneNumberText.clear()

    def delete_supplier(self):
        if len(self.suppliersTable.selectedIndexes()):
            for i in self.suppliersTable.selectedIndexes():
                self.db.delete_supplier(self.suppliers[i.row()]['organisation'])
                self.suppliers = self.db.get_suppliers()
                self.set_data(self.suppliersTable, self.columns_suppliers, self.suppliers)

    def delete_suppliers(self):
        self.db.delete_suppliers()
        self.suppliers = self.db.get_suppliers()
        self.set_data(self.suppliersTable, self.columns_suppliers, self.suppliers)

    def search_supplier(self):
        if self.phoneNumberText.text() == '':
            self.suppliers = self.db.get_suppliers()
        else:
            self.suppliers = self.db.search_supplier(self.phoneNumberText.text())
        self.set_data(self.suppliersTable, self.columns_suppliers, self.suppliers)

    def update_supplier(self, item):
        if not self.changed:
            self.db.update_supplier(item.text(), self.suppliers[item.row()]['organisation'])
            self.suppliers = self.db.get_suppliers()
            self.set_data(self.suppliersTable, self.columns_suppliers, self.suppliers)
            self.lounge_bars = self.db.get_lounge_bars()
            self.set_data(self.loungeBarsTable, self.columns_lounge_bars, self.lounge_bars)

    # --------------------- Ratings functions -----------------------
    def add_rating(self):
        self.db.add_rating(
            lounge_bar_name=self.loungeBarRatingsText.text(),
            feedback=self.feedbackText.text(),
            grade=int(self.gradeText.text())
        )
        self.ratings = self.db.get_ratings()
        self.set_data(self.ratingsTable, self.columns_ratings, self.ratings)
        self.loungeBarRatingsText.clear()
        self.feedbackText.clear()
        self.gradeText.clear()
