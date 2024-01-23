import smbus

bus = smbus.SMBus(7)

denat_address = 0x10
aneal_address = 0x11
elong_address = 0x12

value_denat = 35
value_aneal = 45 
value_elong = 40 


bus.write_byte(denat_address, {value_denat})
bus.write_byte(aneal_address, {value_aneal})
bus.write_byte(elong_address, {value_elong})