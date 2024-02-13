import smbus
import time

# Verwenden von I2C Bus 7
bus = smbus.SMBus(7)

beweg_address = 0x28

value_denat = 10
value_aneal_gesamt = 30
value_elong_gesamt = 20

# Kommunikation mit Bewegmechanismus

def writeNumber(value):
    bus.write_byte(beweg_address, value)
    return -1

while True:
    inp =  [value_denat, value_aneal_gesamt, value_elong_gesamt]
    inp = int(inp)
    if not inp:
        continue

    writeNumber(inp)
    print ("Rock sends: ", inp)
    inp+1
    time.sleep(1)

   