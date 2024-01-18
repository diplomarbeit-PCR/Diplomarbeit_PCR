import smbus
import time

bus_number = 1  # Du kannst auch Bus 0 ausprobieren
slave_address = 0x27

bus = smbus.SMBus(bus_number)

def readFromSlave():
    try:
        value = bus.read_byte(slave_address)
        return value
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

while True:
    # Hier könntest du andere Aktionen durchführen, bevor du den Wert anforderst
    time.sleep(1)

    # Den Wert vom Slave anfordern
    value = readFromSlave()

    if value is not None:
        print(f"Received value from Arduino: {value}")
    else:
        # Handle error, for example, you may choose to break the loop or take corrective action.
        break
