#100DaysOfCode 034/100 - Databases
#
#  20200722 - 100DaysOfCode 034/100 - Databases and Python
#      sqlite3 - built in python library
#
################################################################################
#
import sqlite3

def create_table():
    # Connect to or create a new data base - created if it doesn't exist
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    conn.commit()
    conn.close()

#used for incserting data
#insert("Coffee Cup", 25, 7.50)

#delete("Wine Glass")



print(view())
