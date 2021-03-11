import mysql.connector


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="", database="store")
        self.mycursor = self.connection.cursor()
        self.mycursor.execute(
            "CREATE TABLE IF NOT EXISTS Parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.connection.commit()

    def fetch(self):
        self.mycursor.execute("SELECT * FROM parts")
        rows = self.mycursor.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.mycursor.execute("INSERT INTO parts (part, customer, retailer, price) VALUES('{}', '{}', '{}', '{}')" .format(part, customer, retailer, price))
        # ("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)", (part, customer, retailer, price))
        self.connection.commit()

    def remove(self, id):
        self.mycursor.execute("DELETE FROM parts WHERE id ='{}'" .format(id))
        # ("DELETE FROM parts WHERE id =?", id)
        self.connection.commit()

    def update(self, id, part, customer, retailer, price):
        self.mycursor.execute("UPDATE parts SET part='{}', customer='{}', retailer='{}', price='{}' WHERE id='{}'" .format(part, customer, retailer, price, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()


# db = Database(host="localhost", user="root", password="", database="store.db")
# db = Database().fetch()
# for i in db:
#     print(i)
# db = Database()
# db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
# db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
# db.insert("500w PSU", "Karen Johnson", "Newegg", "80")
# db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
# db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
# db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
# db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", "130")

