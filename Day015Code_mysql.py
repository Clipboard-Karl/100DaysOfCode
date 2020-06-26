#-----------------------------------------------
#100DaysOfCode 015/100 - Interactive English Dictonry now with MySQL
#   2020-06-26
#
#  Connect to a remote MySQL database
#     Will need a libraary to work with MySQL
#        use the following command on the command line:
#              pip3 install mysql-connector-python
#
#  This is a very simple program with no error checking it could be improved on
#    I am going to move forward to more programming and return to this if needed
#
#
#  Note:  For the GitHub load I will be blocking out the credentials because
#         it doesn't seem right to connect to a database in a class that I paid
#         for.  :)
#
import mysql.connector
#
#  these are the credentials to connect to the remote database
con = mysql.connector.connect(
user = "**********",
password = "**************",
host = "***.***.***.***",
database = "******************"
)
#
#  a cursor object is needed to navigate throught the ardit700_pm1database
cursor = con.cursor()

word = input("Enter a word:  ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)

results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No word found!")
