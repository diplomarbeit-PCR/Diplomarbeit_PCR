import pymysql

Servername = 'localhost'
Benutzer = 'root'
Passwort = 'Rock4C+'

# Verbindung mit der Datenbank
con = pymysql.connect(
    host = Servername,
    user = Benutzer,
    Password = Passwort
)
cursor = con.cursor()
cursor.execute("CREATE DATABASE EDUPCR")
cursor.execute("SHOW DATABASES")
dataLbaseist = cursor.fetchall()

for database in databaseList:
    print(database)

con.close()