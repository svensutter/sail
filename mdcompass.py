# Modul enthält alles rund um Kompassfunktionen

import mdhmc5883l

# Diese Funktion holt die Werte aus dem Kompass- und Neigungssensor und
# berechnet daraus den Winkel, den das Schiff zu Norden hat (Uhrzeigersinn)
# Wir erhalten eine Zahl zwischen 0 und 360.
def BoatToNorth():
    # Read Compass-Accelerometer raw value
    X_axis_H = 0x03  # Address of X-axis MSB data register (HMC5883l)
    Z_axis_H = 0x05  # Address of Z-axis MSB data register (HMC5883l)
    Y_axis_H = 0x07  # Address of Y-axis MSB data register (HMC5883l)
    x = mdhmc588l.read_raw_data(X_axis_H)
    z = mdhmc588l.read_raw_data(Z_axis_H)
    y = mdhmc588l.read_raw_data(Y_axis_H)