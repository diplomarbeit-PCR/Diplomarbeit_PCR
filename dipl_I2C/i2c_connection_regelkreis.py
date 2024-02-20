import smbus
import time


# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adressen der Slaves
temp_address = 0x26

# Kommunikation mit Regelkreis
def readFromTemp():

    try:
        t = bus.read_byte(temp_address)
        if t_alt == 1:
            temp_denat = t
            t_alt = 0

        if t_alt == 2:
            temp_aneal = t
            t_alt = 0

        if t_alt == 3:
            temp_elong = t
            t_alt = 0
        else:
            print(f"No valid input")

        t_alt = t

        print(temp_denat) 
        print(temp_aneal) 
        print(temp_elong) 
        return temp_denat, temp_aneal, temp_elong
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None