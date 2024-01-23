import smbus

bus = smbus.SMBus(7)
temp_address = 0x26
detect_address = 0x27
beweg_address = 0x028

def writeNumber(value):
    bus.write_byte(beweg_address, value)
    return -1

def readFromDetekt():
    try:
        value = bus.read_byte(detect_address)
        return value
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None

while True:
    beweg_signal = 1
    beweg_signal = int(beweg_signal)
    if not beweg_signal:
        continue

    writeNumber(beweg_signal)

    value = readFromDetekt()

    if value is not None:
        print(f"Received value from Arduino: {value}")
    else:
        # Handle error, for example, you may choose to break the loop or take corrective action.
        break
