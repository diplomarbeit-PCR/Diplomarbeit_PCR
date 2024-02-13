import smbus

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)

beweg_address = 0x028

value_denat = 10
value_aneal_gesamt = 30
value_elong_gesamt = 20

# Kommunikation mit Bewegmechanismus
    
def readFromBeweg():
    try:
        b = bus.read_byte(beweg_address)

        values = [value_denat, value_aneal_gesamt, value_elong_gesamt]
        # fragt ab, ob in 0-Posi
        if b == 1:
            beweg_null = bus.read_byte(beweg_address)

            for i in range (2,4):
                value = values[i]
                bus.write_byte(beweg_address,i+1)
                bus.write_byte(beweg_address, value)

# vermerkt in sipl_Haupt_Verebt_v1.py
        # btn_Weiter gedrückt
        bus.write_byte(beweg_address, 5)
        # btn_Kontroll gedrückt
        bus.write_byte(beweg_address, 6)
        # btn_Fortführen gedrückt
        bus.write_byte(beweg_address, 5)
#
        
        # falls Notaus gedrückt -> Stop everything
        if b == 9:
            notaus = bus.read_byte(beweg_address)

        else:
            print(f"No valid input")

        return notaus, beweg_null
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None
