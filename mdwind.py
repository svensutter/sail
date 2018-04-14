# Dieses Modul beinhaltet alle Funktionen zur Windanalyse. Dazu gehört die Bestimmung der subjektiven Windrichtung,
# wie auch die Verbindung zur Hardware.
import math
import gpiozero


# Mit dieser Funktion kann die tatsaechliche Windrichtung (unabhaengig von Fahrtwind) berechnet werden.
## !! Diese Funktion werden wir voraussichtlich gar nicht benoetigen, da wir whs. nur mit der subj. Windrichtung
##    arbeiten werden. Kann also evtl. spaeter geloescht werden.
def RealWindAngle(ApparentWind, BoatSpeed, ApparentAngle):
 RealWindSpeed = math.sqrt(ApparentWind**2 + BoatSpeed**2 - 2*ApparentWind*BoatSpeed*math.cos(ApparentAngle))
 
 result_radiant = math.acos((ApparentWind*math.cos(ApparentAngle)-BoatSpeed)/RealWindSpeed)
 result = math.degrees(result_radiant)
 if (ApparentAngle > 180 and ApparentAngle < 360) or (ApparentAngle < 0 and ApparentAngle > -180):
  result = -result
  
 if result < 0:
  result = result + 360
 
 return result  


# Mit dieser Funktion wird die gemessene Windrichtung ausgegeben, zwischen 0 und 360 Grad. 0 ist, wenn
# der Wind direkt von vorne kommt (relativ zum Boot) und dann geht es im Uhrzeigersinn herum.
def GetApparentWind():
 Winkelaufnehmer_Objekt = gpiozero.MCP3008(channel = 0) # Objekt mit Wert aus AD-Wandler Kanal 0
 Winkelaufnehmer_Wert = Winkelaufnehmer_Objekt.value
 return Winkelaufnehmer_Wert # test
