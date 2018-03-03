# Modul enthält alles rund um Kompassfunktionen

import mdhmc5883l

# Diese Funktion holt die Werte aus dem Kompass- und Neigungssensor und
# berechnet daraus den Winkel, den das Schiff zu Norden hat (Uhrzeigersinn)
# Wir erhalten eine Zahl zwischen 0 und 360.
def BoatToNorth():
    # Read Compass-Accelerometer raw value
    x = mdhmc588l.read_raw_data(0x03)
    z = mdhmc588l.read_raw_data(0x05)
    y = mdhmc588l.read_raw_data(0x07)
    
    
