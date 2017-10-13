# windrichtung und geschwindigkeit
import math


# funktion gibt wahrer Windwinkel zurueck
def RealWindAngle(ApparentWind, BoatSpeed, ApparentAngle):
 RealWindSpeed = math.sqrt(ApparentWind**2 + BoatSpeed**2 - 2*ApparentWind*BoatSpeed*math.cos(ApparentAngle))
 
 result_radiant = math.acos((ApparentWind*math.cos(ApparentAngle)-BoatSpeed)/RealWindSpeed)
 result = math.degrees(result_radiant)
 if (ApparentAngle > 180 and ApparentAngle < 360) or (ApparentAngle < 0 and ApparentAngle > -180):
  result = -result
  
 if result < 0:
  result = result + 360
 
 return result  
