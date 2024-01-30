import mysql.connector # neue Bibliothek

Servername = 'localhost'
Benutzer = 'root'
Passwort = 'Rock4C+'
Datenbank = 'eduPCR'

# Verbindung mit der Datenbank
con = mysql.connector.connect(
    host = Servername,
    user = Benutzer,
    Password = Passwort
)
con.database = Datenbank

