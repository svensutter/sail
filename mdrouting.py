# Das Modul mdrouting beinhaltet Funktionen zur Berechnung der Route/Navigation. Das heisst, hier werden
# die Seekarten verarbeitet und anhand der aktuellen Position des Schiffes mögliche Wege generiert.

import os
import re

# Klasse lakemap wird bei der Initialisierung der Seekarten genutzt. Das heisst, dass
# beim Starten des Hauptskriptes (startboat.py) eine Funktion aufgerufen wird, die alle
# Seekarten einliest und fuer jeden See ein Objekt erstellt anhand dieser Klasse.
class lakemap:
    def __init__(self, lake_name, navigable, excludes, exclude_names, buoys, buoy_names):
        self.lake_name = lake_name # Bezeichnung des Sees

        # navigable ist 2-fach verschachtelte Liste: Punktepaare des fahrb. Bereiches > Punkte
        self.navigable = navigable

        # excludes ist 3-fach verschachtelte Liste: Nicht fahrb. Polygone > Punktpaare > Punkte
        self.excludes = excludes

        # Bezeichnungen der einzelnen nichtfahrb. Bereichen in Reihenfolge von self.excludes
        self.exclude_names = exclude_names

        # Bei den Bojen gilt derselbe Aufbau wie bei den excludes
        self.buoys = buoys
        self.buoy_names = buoy_names

# Diese Funktion liest alle Textfiles in /lakemaps aus und eroeffnet fuer jeden See eine Instanz
# von der Klasse lakemap. Dort werden alle Punkte und Bezeichnungen abgelegt. Funktionen und so
# weiter arbeiten dann nur noch mit den Instanzen und nicht mit den Textfiles.
# Return-Wert: Liste mit erstellten Instanzen.
# Diese Funktion wird einmalig bei Skriptstart (startboat.py) ausgefuert.
def InitializeLakemaps():

    file_path = os.path.abspath(__file__)  # Gibt absoluten Pfad dieser Datei (mdrouting.py) an, mit Filename.
    file_dir = re.sub(str(__file__), '', file_path)  # Filename wird geloescht, sodass nur Pfad bleibt
    filenames = os.listdir(file_dir + "lakemaps") # ergibt Liste mit allen Dateinamen

    # Aus jeder Datei wird nun eine Instanz von lakemap erstellt
    x = 0 # einfacher Zaehler
    lakemaps = [""] # init
    for i in filenames:
        lake_name = re.sub("\.txt", '', i)


        file_content = open(file_dir + "lakemaps/" + i, "r") # Datei auslesen

        # Zeile fuer Zeile bearbeiten
        current_dataset = ""
        navigable_list = [[0, 0]]
        exclude_list = [[[0, 0]]] # Nur hier ist 3-fach-Verschachtelung notwendig:
                                  # Polygon > Koordinaten > Punkte
        buoy_list = [[0, 0]]
        exclude_names = [""]
        buoy_names = [""]
        number_of_excludes = 0
        buoy_counter = 0
        for line in file_content:
            if re.search("Navigable", line) != None:
                current_dataset = "navigable"
                navigable_counter = 0
            elif re.search("Exclude", line) != None:
                current_dataset = "exclude"
                exclude_counter = 0

                exclude_name = re.sub("Exclude ", '', line)
                exclude_name = re.sub(":", '', exclude_name)
                exclude_name = re.sub(r"\n", '', exclude_name)

                if number_of_excludes == 0:
                    exclude_names[0] = exclude_name
                else:
                    exclude_names.append(exclude_name)
                    exclude_list.append([[0, 0]])

                number_of_excludes += 1

            elif re.search("Buoy", line) != None:
                current_dataset = "buoy"

                buoy_name = re.sub("Buoy ", '', line)
                buoy_name = re.sub(":", '', buoy_name)
                buoy_name = re.sub(r"\n", '', buoy_name)

                if buoy_counter == 0:
                    buoy_names[0] = buoy_name
                else:
                    buoy_names.append(buoy_name)


            else:
                coordinates = re.split(",", line)
                coordinates[0] = float(coordinates[0])  # floaten
                coordinates[1] = re.sub(" ", '', coordinates[1])  # saeubern
                coordinates[1] = float(re.sub(r"\n", '', coordinates[1]))  # weiter saeubern + floaten

            if current_dataset == "navigable" and re.search("Navigable", line) == None:

                if navigable_counter == 0:
                    navigable_list[0] = coordinates
                else:
                    navigable_list.append(coordinates)

                navigable_counter += 1

            if current_dataset == "exclude" and re.search("Exclude", line) == None:

                if exclude_counter == 0:
                    exclude_list[number_of_excludes - 1][0] = coordinates
                else:
                    exclude_list[number_of_excludes - 1].append(coordinates)

                exclude_counter += 1

            if current_dataset == "buoy" and re.search("Buoy", line) == None:

                if buoy_counter == 0:
                    buoy_list[0] = coordinates
                else:
                    buoy_list.append(coordinates)

                buoy_counter += 1



        if number_of_excludes == 0:
            exclude_list = None
            exclude_names = None

        if buoy_counter == 0:
            buoy_list = None
            buoy_names = None



        file_content.close()  # Dateistream schliessen


        globals()[lake_name] = lakemap(lake_name, navigable_list, exclude_list, exclude_names, buoy_list, buoy_names) # Die Instanz wird nach dem See benannt

        if x == 0:
            lakemaps[x] = lake_name # Instanzname wird in Liste eingetragen
        else:
            lakemaps.append(lake_name)

        x += 1

    return lakemaps



# TEST TEST TEST kann spaeter geloescht werden
InitializeLakemaps() # test
print(opfikersee)
print(opfikersee.lake_name)
print(opfikersee.navigable)
print(opfikersee.excludes)
print(opfikersee.exclude_names)
print(opfikersee.buoys)
print(opfikersee.buoy_names)

