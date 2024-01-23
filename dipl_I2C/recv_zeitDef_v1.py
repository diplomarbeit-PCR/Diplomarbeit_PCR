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
 
def writeNumber(address, value):
    bus.write_byte(address, value)
    return -1

while True:
    value_denat = input("Enter Denat value: ")
    value_denat = int(value_denat)
    writeNumber(beweg_address, value_denat)
    print("RPi sends Denat: ", value_denat)
    time.sleep(1)

    value_aneal = input("Enter Aneal value: ")
    value_aneal = int(value_aneal)
    writeNumber(beweg_address, value_aneal)
    print("RPi sends Aneal: ", value_aneal)
    time.sleep(1)

    value_elong = input("Enter Elong value: ")
    value_elong = int(value_elong)
    writeNumber(beweg_address, value_elong)
    print("RPi sends Elong: ", value_elong)
    time.sleep(1)


