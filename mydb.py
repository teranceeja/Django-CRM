import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'arteta11'
)


# prepare a cursor object

cursorObject = dataBase.cursor()

# create a Database

cursorObject.execute("CREATE DATABASE crm")

print('ALL DONE')