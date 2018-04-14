# Das Skript display-sensor-data.py gibt fortlaufend die (aufbereiteten) Messwerte
# aus, um die Sensoren zu ueberpruefen.

import time
import mdcompass
import mdmpu6050
import mdwind
import mdgps
import os

while True:
  os.system('clear')
  print("Winkel:",mdcompass.BoatToNorth())
  print("Neigung:",mdmpu6050.GetTilt())
  print("Position und Speed:",mdgps.GetGPSPosition())
  print("Windrichtung:",mdwind.GetApparentWind())
  time.sleep(1)
