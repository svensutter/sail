# Hier finden alle Funktionen zu GPS Platz. Dazu gehoeren Positionsbestimmung, Kompass, Winkel zum Ziel.

import math

# Diese Funktion berechnet aus den Koordinaten vom Boot und Ziel den Winkel im
# im Verhaeltnis zu Norden. Dabei erwartet die Funktion die Koordinaten in
# Dezimalform. Output ist der Winkel in Bezug zu Norden im Uhrzeigersinn,
# womit der Output zwischen 0 und 360 liegt.
def TargetAngleToNorth(Boat_Latitude, Boat_Longitude, Target_Latitude, Target_Longitude):

    Delta_Latitude = Target_Latitude - Boat_Latitude
    Delta_Longitude = Target_Longitude - Boat_Longitude

    # Positive Zahlen generieren
    Delta_Latitude_abs = abs(Delta_Latitude)
    Delta_Longitude_abs = abs(Delta_Longitude)

    # Winkel berechnen, unabhaengig von dem Quadranten (Nord-Ost, Ost-Sued, Sued-West, West-Nord)
    Angle = Delta_Longitude_abs / Delta_Latitude_abs # geht nur in python3!!
    Angle = math.atan(Angle)
    Angle = math.degrees(Angle)

    # Winkel anpassen an Quadrant, wenn nicht Nord-Ost
    if (Delta_Latitude < 0) and (Delta_Longitude > 0):
        Angle = 180 - Angle
    if (Delta_Latitude < 0) and (Delta_Longitude < 0):
        Angle = 180 + Angle
    if (Delta_Latitude > 0) and (Delta_Longitude < 0):
        Angle = 360 - Angle

    return(Angle)



# TEST
print(TargetAngleToNorth(50.237482364, 7.234872934, 53.23984729384, 8.234234324)) # Nord-Ost
print(TargetAngleToNorth(20, 30, 10, 50)) # Ost-Sued
print(TargetAngleToNorth(20, 40, 10, 15)) # Sued-West
print(TargetAngleToNorth(25, 20, 32, 10)) # West-Nord