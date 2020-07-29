#100DaysOfCode 035/100 - Databases
#
#  20200723 - 100DaysOfCode 035/100 - Databases and Python - continued
#             convert from sqlite3 to PostgreSQL
#
#    NOTE  -  This does not work - I had issues installing PostgreSQL.
#             I chose to skip because I want to focus on PHP with wordpress
#             after I finish this clas 
#
################################################################################
#  Libraries need to be installed:
#     PostgreSQL - https://www.postgresql.org/download/linux/ubuntu/
#
#  pip3 install psycopg2
#
import pyscopg2

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

#used for inserting data
#insert("Coffee Cup", 25, 7.50)

#used to delete data
#delete("Wine Glass")

#used to update data
update(11,6,"Water Glass")


print(view())
