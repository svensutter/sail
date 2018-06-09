# Modul enthält alles rund um Kompassfunktionen

# CONFIG (manuell uebertragen aus ausgefuetrtem Script calibrate-compass.py)
x_offset = 4.0
y_offset = -79.0
z_offset = 60

# IMPORT
import mdhmc5883l
import mdmpu6050
import math

# Diese Funktion holt die Werte aus dem Kompass- und Neigungssensor und
# berechnet daraus den Winkel, den das Schiff zu Norden hat (Uhrzeigersinn)
# Wir erhalten eine Zahl zwischen 0 und 360.
def BoatToNorth():
    # Read Compass-Accelerometer raw value
    x_raw = mdhmc5883l.read_raw_data(0x03)
    z_raw = mdhmc5883l.read_raw_data(0x05)
    y_raw = mdhmc5883l.read_raw_data(0x07)

    # Skalieren
    x = x_raw - x_offset
    z = z_raw - z_offset
    y = y_raw - y_offset
    
    # Neigungswinkel einlesen
    tilt = mdmpu6050.GetTilt() # tilt wird zur Listenvariable: 0 = X, 1 = Y
   
    # Tilt Compensation der Rohwerte aus dem Kompass
    xh = x * math.cos(tilt[0]) + z * math.sin(tilt[0])
    yh = x * math.sin(-tilt[1]) * math.sin(tilt[0]) + y * math.cos(-tilt[1]) - z * math.sin(-tilt[1]) * math.cos(tilt[0])
    
    # aus korrigierten Rohwerten Heading berechnen
    HeadingRad = math.atan2(yh, xh)
    if HeadingRad < 0:
        HeadingRad += 2 * math.pi
    if HeadingRad > (2 * math.pi):
        HeadingRad -= 2 * math.pi

    Heading = math.degrees(HeadingRad)
    
    return Heading
