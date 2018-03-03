# Modul enthält alles rund um Kompassfunktionen

import mdhmc5883l
import mdmpu6050
import math

# Diese Funktion holt die Werte aus dem Kompass- und Neigungssensor und
# berechnet daraus den Winkel, den das Schiff zu Norden hat (Uhrzeigersinn)
# Wir erhalten eine Zahl zwischen 0 und 360.
def BoatToNorth():
    # Read Compass-Accelerometer raw value
    x = mdhmc5883l.read_raw_data(0x03)
    z = mdhmc5883l.read_raw_data(0x05)
    y = mdhmc5883l.read_raw_data(0x07)
    
    # Neigungswinkel einlesen
    tilt = mdmpu6050.GetTilt() # tilt wird zur Listenvariable: 0 = X, 1 = Y
   
    # Tilt Compensation der Rohwerte aus dem Kompass
    xh = x * math.cos(tilt[0]) + z * math.sin(tilt[0])
    yh = x * math.sin(tilt[1]) * math.sin(tilt[0]) + y * math.cos(tilt[1]) - z * math.sin(tilt[1]) * math.cos(tilt[0])
    
    # aus korrigierten Rohwerten Heading berechnen
    HeadingRad = math.atan(yh / xh)
    Heading = math.degrees(HeadingRad)
    
    # da die Werte von -180 bis 180 gehen, Aenderung auf 0 bis 360 Grad
    if Heading < 0:
        Heading = Heading + 360
    
    Heading = abs(Heading) # um Fehlerquellen zu vermeiden, da bei Tests -0.0 ausgegeben wurde
    
    return Heading
