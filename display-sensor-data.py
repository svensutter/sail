# Das Skript display-sensor-data.py gibt fortlaufend die (aufbereiteten) Messwerte
# aus, um die Sensoren zu ueberpruefen.

import time
import mdcompass
import mdmpu6050

while True:
  print("Winkel:",mdcompass.BoatToNorth())
  print("Neigung:",mdmpu6050.GetTilt())
  time.sleep(1)
