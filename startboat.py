# Skript, das aus Bootvorgang gestartet wird, von dem geht alles aus
# Standardsgeschwindigkeitsformat in kmh

import mdmail
import mdgps
import mdrouting

mdrouting.InitializeLakemaps() # Alle Seekarten werden in Instanzen ueberfuehrt

# TEST TEST TEST
target = mdmail.GetTargetFromMail()
if target == None:
  print("Keine Position per E-Mail erhalten")
else:
  print("Position erhalten: "+str(target))
  # in diesem Bsp ist das Boot im See am Buerkliplatz
  print("Winkel zum Ziel im Verhaeltnis zu Norden: "+str(mdgps.TargetAngleToNorth(47.3611303, 8.5401025, target[0], target[1])))