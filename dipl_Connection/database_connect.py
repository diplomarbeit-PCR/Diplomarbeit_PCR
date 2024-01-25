import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(option_files = "connection.ini")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Name oder Password ist falsch")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Datenbank unbekannt")
        
    else: 
        print(err)

else: 
    cnx.close()