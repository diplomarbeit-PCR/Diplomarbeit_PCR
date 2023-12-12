# i2c_module.py
import smbus

class I2CModule:
    def __init__(self, bus_number, device_address):
        self.bus = smbus.SMBus(bus_number)
        self.device_address = device_address

    def write_data(self, data):
        # Schreibe Daten an das I2C-Gerät
        self.bus.write_i2c_block_data(self.device_address, 0, data)

    def read_data(self, num_bytes):
        # Lese Daten vom I2C-Gerät
        return self.bus.read_i2c_block_data(self.device_address, 0, num_bytes)
