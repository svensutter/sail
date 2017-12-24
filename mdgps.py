# Hier finden alle Funktionen zu GPS Platz. Dazu gehoeren Positionsbestimmung, Kompass, Winkel zum Ziel.

import math
import urllib.request
import re


# Funktion GetGooglePosition. Ausgehend von URL, die in Mail steckt, wenn man eine
# Position teilt, werden die Koordinaten dieses Punktes zurueckgegeben.
def GetGooglePosition(url):
    content = urllib.request.urlopen(url)

    html = content.read()
    html = html.decode()

    hits = re.findall(r"\-{0,1}\d{1,2}[\°]\d\d[\']\d\d[\.]\d", html)

    for i in range(0, 1):
        split1[i] = re.split(r"[\°]", hits[i])
        split2[i] = re.split(r"[\']", hits[i])
        
        coordinates[i] = (((split2[i][1] / 60) + split2[i][0]) / 60) + split1[i][0]
        
    print(cordinates[0])
    print(cordinates[1])
       
        
GetGooglePosition("https://goo.gl/maps/LHnc9P1YEvN2")
        
    
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
