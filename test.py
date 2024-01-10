import smbus
import time

# Festlegen des I2C-Bus (normalerweise 1 für Raspberry Pi)
i2c_bus = 1

# Festlegen der I2C-Adresse des Slaves
i2c_address = 0x04

# Erstellen einer I2C-Verbindung
bus = smbus.SMBus(i2c_bus)

try:
    while True:
        # Hier können Sie Daten an den Slave senden
        data_to_send = [0x01, 0x02, 0x03]
        bus.write_i2c_block_data(i2c_address, 0x00, data_to_send)

        # Warten Sie einen Moment (optional)
        time.sleep(1)

        # Daten vom Slave lesen (nehmen Sie die Anzahl der Bytes, die Sie erwarten)
        data_received = bus.read_i2c_block_data(i2c_address, 0x00, 3)
        print("Received data:", data_received)

        # Warten Sie einen Moment (optional)
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    # Schließen Sie die I2C-Verbindung, wenn das Programm beendet wird
    bus.close()
