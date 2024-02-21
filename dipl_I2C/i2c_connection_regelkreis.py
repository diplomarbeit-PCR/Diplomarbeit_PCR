import smbus
import time

from dipl_Phasenablauf.Phasenablauf_Vererbt_v1 import Frm_denat, Frm_aneal, Frm_elong

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Adresse des Arduino-Slave
temp_address = 0x26

def readFromTemp():
    frm_denat = Frm_denat()
    frm_aneal = Frm_aneal()
    frm_elong = Frm_elong()

    try:
        # Lesen der Daten als Block von 6 Bytes (2 Bytes pro Integer-Wert)
        data = bus.read_i2c_block_data(temp_address, 0, 6)

        # Interpretiere die empfangenen Daten als Integer-Werte
        frm_denat.temp_denat = int.from_bytes(data[0:2], byteorder='little', signed=True)
        frm_aneal.temp_aneal = int.from_bytes(data[2:4], byteorder='little', signed=True)
        frm_elong.temp_elong = int.from_bytes(data[4:6], byteorder='little', signed=True)

        print("Empfangener Denat-Wert:", frm_denat.temp_denat)
        print("Empfangener Aneal-Wert:", frm_aneal.temp_aneal)
        print("Empfangener Elong-Wert:", frm_elong.temp_elong)

        return frm_denat.temp_denat, frm_aneal.temp_aneal, frm_elong.temp_elong

    except OSError as e:
        print(f"Fehler beim Lesen vom I2C-Gerät: {e}")
        return None, None, None


