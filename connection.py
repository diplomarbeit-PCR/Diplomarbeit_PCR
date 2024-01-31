import pymysql

temp_denat = 95
temp_aneal = 60
temp_elong = 70
value_denat = 10
value_aneal = 30
value_elong = 20

DL_counter = 10
value_light = 24.90

# Verbindung zur Datenbank herstellen
connection = pymysql.connect(
    host='localhost',     # Hostname oder IP-Adresse deiner MariaDB-Instanz
    user='root',     # Benutzername für den Zugriff auf die Datenbank
    password='Rock4C+',    # Passwort für den Benutzer
    database='eduPCR'    # Name der Datenbank, zu der du dich verbinden möchtest
)

try:
    # Cursor-Objekt erstellen
    with connection.cursor() as cursor:

        # Tabelle 'PhasenWerte' erstellen
        create_table_phasen = """
        CREATE TABLE IF NOT EXISTS PhasenWerte (
            Kategorien VARCHAR(50),
            Denaturierung DECIMAL(5,2),
            Annealing DECIMAL(5,2),
            Elongation DECIMAL(5,2),
            Einheit VARCHAR(50)
        )
        """
        cursor.execute(create_table_phasen)
        print("Tabelle 'PhasenWerte' erstellt")

        # Tabelle 'Messwerte' erstellen
        create_table_messwert = """
        CREATE TABLE IF NOT EXISTS Messwerte (
            Kategorien VARCHAR(50),
            Werte DECIMAL(5,2),
            Einheit VARCHAR(50)
        )
        """
        cursor.execute(create_table_messwert)
        print("Tabelle 'Messwerte' erstellt")

        # Daten in Tabelle 'PhasenWerte' einfügen
        insert_table_phasen = """
        INSERT INTO PhasenWerte
        VALUES
        ("Temperatur", %s, %s, %s, "°C"),
        ("Dauer", %s, %s, %s, "sek")
        """
        cursor.execute(insert_table_phasen, (temp_denat, temp_aneal, temp_elong, value_denat, value_aneal, value_elong))
        print("In Tabelle 'PhasenWerte' eingefügt")

        # Daten in Tabelle 'Messwerte' einfügen
        insert_table_messwert = """
        INSERT INTO Messwerte
        VALUES
        ("Durchläufe", %s, ""),
        ("Lichtstärke", %s, "lum")
        """
        cursor.execute(insert_table_messwert, (DL_counter, value_light))
        print("In Tabelle 'Messwerte' eingefügt")

        # Daten aus Tabelle 'PhasenWerte' abrufen und ausgeben
        dae = "SELECT * FROM PhasenWerte"
        cursor.execute(dae)
        result = cursor.fetchall()
        for row in result:
            print(row)

        # Daten aus Tabelle 'Messwerte' abrufen und ausgeben
        mw = "SELECT * FROM Messwerte"
        cursor.execute(mw)
        result = cursor.fetchall()
        for row in result:
            print(row)

except pymysql.MySQLError as e:
    print("MySQL-Fehler: {}".format(str(e)))

finally:
    # Verbindung schließen
    connection.close()
