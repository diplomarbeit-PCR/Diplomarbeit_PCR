import smbus

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

value = int([{value_denat}, {value_aneal}, {value_elong}])

try:
    bus.write_byte(beweg_address, value)
except OSError as e:
    print(f"Error")
