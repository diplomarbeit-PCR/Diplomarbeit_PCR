import smbus
import time

bus = smbus.SMBus(7)

beweg_address = 0x28
#denat_address = 0x10
#aneal_address = 0x11
#elong_address = 0x12

value_denat = 35
value_aneal = 45 
value_elong = 40 

value_denat = int(value_denat)
value_aneal = int(value_aneal)
value_elong = int(value_elong)
 
def writeNumber(value):
    bus.write_byte(beweg_address, value)
    return -1

while True:
    inp1 = input(value_denat)
    inp1 = int(inp1)
    if not inp1:
        continue

    writeNumber(inp1)
    print ("RPi sends: ", inp1)
    time.sleep(1)

    inp2 = input(value_aneal)
    inp2 = int(inp2)
    if not inp2:
        continue

    writeNumber(inp2)
    print ("RPi sends: ", inp2)
    time.sleep(1)

    inp3 = input(value_elong)
    inp3 = int(inp3)
    if not inp3:
        continue

    writeNumber(inp3)
    print ("RPi sends: ", inp3)
    time.sleep(1)

