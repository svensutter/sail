# Modul enthält alles rund um Kompassfunktionen

# CONFIG Offset-Bootausrichtung
offsetcomp_bootausrichtung = 0 # passte schon von Haus aus...

# IMPORT
import mdhmc5883l
import mdmpu6050
import math

# Diese Funktion holt die Werte aus dem Kompass- und Neigungssensor und
# berechnet daraus den Winkel, den das Schiff zu Norden hat (Uhrzeigersinn)
# Wir erhalten eine Zahl zwischen 0 und 359.99.
def BoatToNorth():
    # Read Compass-Accelerometer raw value
    x_raw = mdhmc5883l.read_raw_data(0x03)
    z_raw = mdhmc5883l.read_raw_data(0x05)
    y_raw = mdhmc5883l.read_raw_data(0x07)

    # Skalieren
    x = x_raw
    z = z_raw
    y = y_raw
    
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

    Heading = math.degrees(HeadingRad) + offsetcomp_bootausrichtung
    if Heading > 360:
        Heading -= 360
    elif Heading < 0:
        Heading += 360

    # Damit die Werte eindeutig sind, wird 360 auf 0 gesetzt
    if Heading == 360:
        Heading = 0

    return Heading
