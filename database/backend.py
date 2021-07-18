import sqlite3

"""
In case of a remote mysql Use below 
pip install mysql-connector
con = mysql.connector.connect(
    user="abrao", 
    password = "abrao", 
    host="a.b.c.d", 
    database = "abrao_database"
"""


def connect_todb():
    connect = sqlite3.connect("lite.db")
    cur = connect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
    connect.commit()
    connect.close()


def insert_into_db(item,quantity, price):
    connect = sqlite3.connect("lite.db")
    cur = connect.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    connect.commit()
    connect.close()


def view_from_db():
    connect = sqlite3.connect("lite.db")
    cur = connect.cursor()
    cur.execute("SELECT * from store")
    result = cur.fetchall()
    return result


def delete_from_db(item):
    connect = sqlite3.connect("lite.db")
    cur = connect.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    connect.commit()
    connect.close()


def update_db(quantity,price,item):
    connect = sqlite3.connect("lite.db")
    cur = connect.cursor()
    cur.execute("UPDATE store SET quantity=?, price =? WHERE item=?",(quantity, price, item))
    connect.commit()
    connect.close()


insert_into_db("COFFEE MUG", 20, 10)
insert_into_db("CERAMIC MUG", 20, 2)
insert_into_db("CHAI MUG", 20, 5)

#delete_from_db("WINE GLASS")

#delete_from_db("COFFEE MUG")
#delete_from_db("CERAMIC MUG")
delete_from_db("CHAI MUG")

print(view_from_db())