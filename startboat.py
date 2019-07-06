# Skript, das aus Bootvorgang gestartet wird, von dem geht alles aus
# Standardsgeschwindigkeitsformat in kmh

import mdmail
import mdgps
import mdrouting
import threading
import time
import mdwind
import mdcompass
import math

# Alle Seekarten werden in Instanzen ueberfuehrt
# Die Variable lake_instanzen enthaelt eine Liste aller Instanzen
# die erstellt wurden. Fuer jeden See eine.
# lake_instances = [""] # init
lake_instances = mdrouting.InitializeLakemaps()
print(lake_instances)


# Objekt ClsWindDirectionAverage ruft den Winkel der Windfahne ab, setzt diesen
# in Bezug zum Kompass und gibt einen gemittelten Wert (10s, 50Hz) in die
# Objektinstanz XYZ, in Attribut WindDirectionAverage aus (1Hz).
class ClsWindDirectionAverage(threading.Thread):

  def run(self):

    CntListenplatz = 0 # Position fuer spaetere Listeneintraege (0-499, weil 10*50 Werte)
    VarErste10s = True
    LstWindDirections = []

    while True:
      for i in range(0,50):

        # Winkel in Bezug auf Kompass setzen
        VarWindDirection = mdcompass.BoatToNorth() + mdwind.GetApparentWind()
        if VarWindDirection >= 360:
          VarWindDirection -= 360

        if VarErste10s:
          LstWindDirections.append(VarWindDirection)
        else:
          LstWindDirections[CntListenplatz] = VarWindDirection

        if CntListenplatz == 499:
          CntListenplatz = 0
          VarErste10s = False
        else:
          CntListenplatz += 1


        time.sleep(0.02) # entspricht den 50Hz


      # Mittelwert ueber Vektoren berechnen und in Objektinstanz XYZ schreiben

      LstVektorSumme = [0, 0] # Startpunkt Vektor

      for Winkel in LstWindDirections:

        VarPunktverschiebung = [0, 0] # init (x, y)
        WinkelRad = math.radians(Winkel) # fuer spaetere Sinus-/Cosinus-Berechnungen

        # Sollte Winkel genau 0, 90, 180 oder 270 sein, kann nicht ueber ein rechtwinkliges
        # Dreieck errechnet werden, aber dafuer direkt abgeleitet werden. 360 muss nicht definiert
        # werden, weil dies bereits in mdwind.GetApparentWind() bereits auf 0 gesetzt wird.
        if Winkel == 0:
          VarPunktverschiebung = [0, 1]
        elif Winkel == 90:
          VarPunktverschiebung = [1, 0]
        elif Winkel == 180:
          VarPunktverschiebung = [0, -1]
        elif Winkel == 270:
          VarPunktverschiebung = [-1, 0]

        # Alle weiteren Winkel werden je nach Quadrant anders weiterverabeitet
        if Winkel > 0 and Winkel < 90:
          VarDeltaX = math.sin(WinkelRad)
          VarDeltaY = math.cos(WinkelRad)
          VarPunktverschiebung = [VarDeltaX, VarDeltaY]
        elif Winkel > 90 and Winkel < 180:
          VarWinkelQ2Rad = math.radians(180 - Winkel) # Winkel im Dreieck fuer Quadrant 2
          VarDeltaX = math.sin(VarWinkelQ2Rad)
          VarDeltaY = -math.cos(VarWinkelQ2Rad)
          VarPunktverschiebung = [VarDeltaX, VarDeltaY]
        elif Winkel > 180 and Winkel < 270:
          VarWinkelQ3Rad = math.radians(Winkel - 180)
          VarDeltaX = -math.sin(VarWinkelQ3Rad)
          VarDeltaY = -math.cos(VarWinkelQ3Rad)
          VarPunktverschiebung = [VarDeltaX, VarDeltaY]
        elif Winkel > 270 and Winkel < 360:
          VarWinkelQ4Rad = math.radians(360 - Winkel)
          VarDeltaX = -math.sin(VarWinkelQ4Rad)
          VarDeltaY = math.cos(VarWinkelQ4Rad)
          VarPunktverschiebung = [VarDeltaX, VarDeltaY]

        # Punktverschiebung dem Gesamtvektor hinzufuegen
        LstVektorSumme[0] += VarDeltaX
        LstVektorSumme[1] += VarDeltaY


      # Gesamtwinkel aus Gesamtvektor errechnen + Anpassung je Quadrant
      # Und zunaechst Fall abgedeckt, wenn x und/oder y 0 sein sollte.
      if LstVektorSumme[0] == 0:
        if LstVektorSumme[1] >= 0:
          VarWinkelSumme = 0
        else:
          VarWinkelSumme = 180
      elif LstVektorSumme[1] == 0:
        if LstVektorSumme[0] > 0:
          VarWinkelSumme = 90
        else:
          VarWinkelSumme = 270
      else:
        VarWinkelSumme = math.degrees(math.atan(math.fabs(LstVektorSumme[0]) / math.fabs(LstVektorSumme[1])))
        if LstVektorSumme[0] > 0 and LstVektorSumme[1] < 0:
          VarWinkelSumme = 180 - VarWinkelSumme
        elif LstVektorSumme[0] < 0 and LstVektorSumme[1] < 0:
          VarWinkelSumme = 180 + VarWinkelSumme
        elif LstVektorSumme[0] < 0 and LstVektorSumme[1] > 0:
          VarWinkelSumme = 360 - VarWinkelSumme


      if VarWinkelSumme == 360: # damit eindeutige Werte, weil 360 und 0 dasselbe bedeutet
        VarWinkelSumme = 0

      print(VarWinkelSumme)
      print(VarWindDirection)


# Test
A = ClsWindDirectionAverage()
A.start()