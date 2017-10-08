# windrichtung und geschwindigkeit
import math


# funktion gibt wahre Windgeschwindigkeit zurueck
def RealWindSpeed(ApparentWind, BoatSpeed, ApparentAngle):
 result = -99
 result = math.sqrt(ApparentWind**2 + BoatSpeed**2 - 2*ApparentWind*BoatSpeed*math.cos(ApparentAngle))
 return result      
test
