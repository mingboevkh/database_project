import psycopg2 as ps


class DataBase:
    def __init__(self, user, password, name, host='localhost'):
        self.user = user
        self.password = password
        self.name = name
        self.host = host

        con = ps.connect(
            user=user,
            password=password,
            database='postgres',
            host=host
        )

        con.autocommit = True
        cur = con.cursor()
        cur.execute("SELECT datname FROM pg_database;")

        if (name,) not in cur.fetchall():
            cur.execute(f"CREATE DATABASE {name};")
        con.close()
        cur.close()

        self.connection = ps.connect(
            user=user,
            password=password,
            database=name,
            host=host
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.cursor.execute(open('initdb.sql', 'r').read())
        self.init_tables()
        self.cursor.execute(open('functions.sql', 'r').read())

    def drop_database(self):
        self.connection = ps.connect(
            user=self.user,
            password=self.password,
            database='postgres',
            host=self.host
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"DROP DATABASE {self.name}")

    def init_tables(self):
        self.cursor.callproc("init_tables")

    # Owners ---------------------------------------------------------
    def add_owner(self, owner_name, f_date, email):
        self.cursor.callproc("add_owner", (owner_name, f_date, email,))

    def get_owners(self):
        self.cursor.callproc("get_owners")
        return self.cursor.fetchone()[0]

    def delete_owner(self, name):
        self.cursor.callproc("delete_owner", (name,))

    def delete_owners(self):
        self.cursor.callproc("delete_owners")

    def search_owner(self, email):
        self.cursor.callproc("search_owner", (email,))
        return self.cursor.fetchone()[0]

    def update_owner(self, new_name, previous_name):
        self.cursor.callproc("update_owner", (new_name, previous_name,))

    # -------------------------------------------------------------

    # Suppliers ---------------------------------------------------------
    def add_supplier(self, organisation, volume_purchase, phone_number):
        self.cursor.callproc("add_supplier", (organisation, volume_purchase, phone_number,))

    def get_suppliers(self):
        self.cursor.callproc("get_suppliers")
        return self.cursor.fetchone()[0]

    def delete_supplier(self, name):
        self.cursor.callproc("delete_supplier", (name,))

    def delete_suppliers(self):
        self.cursor.callproc("delete_suppliers")

    def search_supplier(self, phone_number):
        self.cursor.callproc("search_supplier", (phone_number,))
        return self.cursor.fetchone()[0]

    def update_supplier(self, new_name, previous_name):
        self.cursor.callproc("update_supplier", (new_name, previous_name,))

    # -------------------------------------------------------------

    # Ratings ---------------------------------------------------------
    def add_rating(self, lounge_bar_name, feedback, grade):
        self.cursor.callproc("add_rating", (lounge_bar_name, feedback, grade,))

    def get_ratings(self):
        self.cursor.callproc("get_ratings")
        return self.cursor.fetchone()[0]

    def delete_ratings(self):
        self.cursor.callproc("delete_ratings")
    # -------------------------------------------------------------

    # Lounge bars ---------------------------------------------------------
    def add_lounge_bar(self, name, address, supplier, owner, common_tobacco):
        self.cursor.callproc("add_lounge_bar", (name, address, supplier, owner, common_tobacco,))

    def search_lounge_bar(self, name):
        self.cursor.callproc("search_lounge_bar", (name,))
        return self.cursor.fetchone()[0]

    def get_lounge_bars(self):
        self.cursor.callproc("get_lounge_bars")
        return self.cursor.fetchone()[0]

    def delete_lounge_bar(self, name):
        self.cursor.callproc("delete_lounge_bar", (name,))

    def delete_lounge_bars(self):
        self.cursor.callproc("delete_lounge_bars")

    def update_lounge_bar(self, new_name, previous_name):
        self.cursor.callproc("update_lounge_bar", (new_name, previous_name,))
