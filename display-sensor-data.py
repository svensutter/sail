# Das Skript display-sensor-data.py gibt fortlaufend die (aufbereiteten) Messwerte
# aus, um die Sensoren zu ueberpruefen.

import time
import mdcompass

while true:
  print(mdcompass.BoatToNorth())
  time.sleep(1)
