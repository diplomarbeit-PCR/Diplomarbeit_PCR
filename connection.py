import pymysql

# Verbindung zur Datenbank herstellen
connection = pymysql.connect(
    host='localhost',     # Hostname oder IP-Adresse deiner MariaDB-Instanz
    user='dein_benutzername',     # Benutzername für den Zugriff auf die Datenbank
    password='dein_passwort',    # Passwort für den Benutzer
    database='')    # Name der Datenbank, zu der du dich verbinden möchtest

try:
    # Cursor-Objekt erstellen
    cursor = connection.cursor()

    # Datenbank erstellen
    db_name = 'meine_datenbank'
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))
    print("Datenbank erstellt: {}".format(db_name))

    # Zur Datenbank wechseln
    cursor.execute("USE {}".format(db_name))

    # Tabelle erstellen
    create_table_query = """
    CREATE TABLE IF NOT EXISTS benutzer (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL UNIQUE
    )
    """
    cursor.execute(create_table_query)
    print("Tabelle 'benutzer' erstellt")

except pymysql.MySQLError as e:
    print("MySQL-Fehler: {}".format(str(e)))

finally:
    # Verbindung schließen
    connection.close()
