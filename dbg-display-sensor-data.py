# Das Skript display-sensor-data.py gibt fortlaufend die (aufbereiteten) Messwerte
# aus, um die Sensoren zu ueberpruefen.

import time
import mdcompass
import mdmpu6050
import mdwind
import mdgps
import os
import mdirsensor

while True:
  os.system('clear')
  print("Neigungskorrigierter Winkel:",mdcompass.BoatToNorth())
  print("Neigung:",mdmpu6050.GetTilt())
  print("Position und Speed:",mdgps.GetGPSPosition())
  print("Windrichtung:",mdwind.GetApparentWind())
  print("Distanz vor Schiff:",mdirsensor.GetDistance())
  time.sleep(1)
