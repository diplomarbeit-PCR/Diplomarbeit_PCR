# master_code.py
import os
from i2c_module import I2CModule
from dipl_Haupt_v1 import Frm_zeitDef

# Das aktuelle Arbeitsverzeichnis speichern
current_directory = os.getcwd()

# Zum Root-Verzeichnis wechseln
root_directory = "/"
os.chdir(root_directory)

# Hier importieren Sie das I2C-Modul und verwenden es im Master-Code
i2c_module = I2CModule(bus_number=1, device_address=0x42)

# Instanz von Frm_zeitDef erstellen
frm_zeitDef_instanz = Frm_zeitDef()

# Werte, die übertragen werden sollen
value_denat_to_send = frm_zeitDef_instanz.wasserDauer_denat
value_aneal_to_send = frm_zeitDef_instanz.wasserDauer_aneal
value_elong_to_send = frm_zeitDef_instanz.wasserDauer_elong

# Daten in eine Liste konvertieren, um sie an das I2C-Modul zu senden
data_to_send = [value_denat_to_send, value_aneal_to_send, value_elong_to_send]

# Daten an das I2C-Modul senden
i2c_module.write_data(data_to_send)

# Zum ursprünglichen Verzeichnis zurückkehren (optional)
os.chdir(current_directory)
