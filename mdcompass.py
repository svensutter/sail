# Modul enthält alles rund um Kompassfunktionen

import mdhmc5883l
import mdmpu6050

# Diese Funktion holt die Werte aus dem Kompass- und Neigungssensor und
# berechnet daraus den Winkel, den das Schiff zu Norden hat (Uhrzeigersinn)
# Wir erhalten eine Zahl zwischen 0 und 360.
def BoatToNorth():
    # Read Compass-Accelerometer raw value
    x = mdhmc588l.read_raw_data(0x03)
    z = mdhmc588l.read_raw_data(0x05)
    y = mdhmc588l.read_raw_data(0x07)
    
    # Neigungswinkel einlesen
    tilt = mdmpu6050.GetTilt() # tilt wird zur Listenvariable: 0 = X, 1 = Y
    print(tilt)
    
BoatToNorth()
