# Modul mdirsensor.py enthaelt Funktionen zur Verbindung und Auswertung des IR-Sensors,
# welcher fuer die Kollisionsvermeidung eingesetzt wird.

import gpiozero
import time # loeschen

def GetDistance():
 IR_Sensor_Objekt = gpiozero.MCP3008(channel = 1) # Objekt mit Wert aus AD-Wandler Kanal 1
 IR_Sensor_Wert = IR_Sensor_Objekt.value

 IR_Sensor_Wert_handlich = int(IR_Sensor_Wert * 100) # ergibt return-Wert zw. 0 und 100
 # !! Achtung. Diese Werte sind aber nicht linear, sondern werden bei uns nur fuer den Vergleich
 # mit einem Cutoff verwendet und nicht zur Distanzbestimmung in Meter oder so ...

 return IR_Sensor_Wert_handlich