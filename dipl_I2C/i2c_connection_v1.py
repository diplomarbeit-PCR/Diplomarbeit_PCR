import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)
# Deklarieren der Adressen der Slaves
temp_address = 0x26
detect_address = 0x27
beweg_address = 0x028

temp_denat = 94
temp_aneal = 65
temp_elong = 67
value_denat = 10
value_aneal_gesamt = 30
value_elong_gesamt = 20
value_spg = 40.1
value_light = 17.39

# Kommunikation mit Detektor

def readFromDetekt():
    try:
        d = bus.read_byte(detect_address)
        # fragt ab, ob <detektor in Nullposition ist und die Probe eingeführt ist
        if d == 1:
            detect_null = bus.read_byte(detect_address)

        # fragt nach Spg
        if d == 2:
            value_spg = bus.read_byte(detect_address)

        # fragt nach Lichtintensität    
        if d == 3:
            value_light = bus.read_byte(detect_address)

        else:
            print(f"Noch nicht bereit")
            print(f"Bitte kontrollieren Sie, ob die Probe beim Detektor ist")
            print(f"Bitte kontrollieren Sie, ob der Detektor in Nullposition steht.")

        return value_spg, value_light, detect_null
 
    except OSError as e:
        print(f"Error reading from I2C device: {e}")
        return None



# Kommunikation mit Regelkreis

# Während Denaturierung soll t = 1 sein
# Wert 1 an Arduino senden, um in Auswahl-Anweisung mit Temperatur von Denaturierung zu kommen
def writeTempD(t):
    t = 1
    bus.write_byte(temp_address, t)
    temp_denat = bus.read_byte(temp_address)
    return temp_denat

# Während Annealing soll t = 2 sein
# Wert 2 an Arduino senden, um in Auswahl-Anweisung mit Temperatur von Annealing zu kommen
def writeTempA(t):
    t = 2
    bus.write_byte(temp_address, t)
    temp_aneal = bus.read_byte(temp_address)
    return temp_aneal

# Während Elongation soll t = 3 sein
# Wert 3 an Arduino senden, um in Auswahl-Anweisung mit Temperatur von Elongation zu kommen
def writeTempE(t):
    t = 3
    bus.write_byte(temp_address, t)
    temp_elong = bus.read_byte(temp_address)
    return temp_elong

#def readFromTemp():
 #   try:
  #      t = bus.read_byte(temp_address)
   #     if t == 1:
    #        temp_denat = bus.read_byte(temp_address)
#
 #       if t == 2:
  #          temp_aneal = bus.read_byte(temp_address)
   # 
    #    if t == 3:
     #       temp_elong = bus.read_byte(temp_address)

      #  else:
       #     print(f"No valid input")

        #return temp_denat, temp_aneal, temp_elong
 
    #except OSError as e:
     #   print(f"Error reading from I2C device: {e}")
      #  return None

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
