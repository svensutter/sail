# coding=utf-8
# Das Modul mdservos beinhaltet die Funktionen, um die Servos (Ruder, Segel) anzusteuern.

import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BCM) # Belegung GPIO-Ports definieren
GPIO.setwarnings(False) # Sonst kommt Warnung "Channel already in use"

# Initialisierung Ruder-Servo
GPIO.setup(17, GPIO.OUT)
RuderServo = GPIO.PWM(17, 50) # Pin 17 mit 50 Hz
RuderServo.start(7.5) # gerades Ruder

# Initialisierung Segel-Servo
GPIO.setup(18, GPIO.OUT)
SegelServo = GPIO.PWM(18, 50) # Pin 18 mit 50 Hz
SegelServo.start(5) # Segel angelegt

# Funktion RuderWinkel() nimmt Winkelwert zw. -45 und 45 entgegen und
# stellt das Ruder entsprechend ein. Die Minuswerte sind links.
def RuderWinkel(Winkel):

    if not (Winkel <= 45 and Winkel >= -45):
        print("Funktion RuderWinkel hat Wert ausserhalb des gueltigen Bereichs erhalten.")
        return False

    Pulsweite = 5 + ((5 / 90) * (Winkel + 45))

    RuderServo.ChangeDutyCycle(Pulsweite)

    return True


# Funktion SegelWinkel() nimmt Winkelwert zw. 0 und 90 Grad entgegen und
# stellt das Segel entsprechend ein. Das Segel wird im Umfang des
# eingestellten Winkels von der Mitte abweichen; in welche Richtung
# entscheidet der Wind.
def SegelWinkel(Winkel):

    if not (Winkel <= 90 and Winkel >= 0):
        print("Funktion SegelWinkel hat Wert ausserhalb des gueltigen Bereichs erhalten.")
        return False

    if Winkel == 0:
        SegelServo.ChangeDutyCycle(5)
        return True

    Winkel_rad = math.radians(Winkel)

    Seillaenge = math.sqrt(281**2 + 310**2 + 110**2 - 2 * 281 * 310 * math.cos(Winkel_rad)) # in mm

    # umrechnen in Pulsweite (5% = 100mm / 8.4% = 436mm) ! 436mm waeren knapp ueber 90 Grad
    Pulsweite = 5 + (3.4 / (436 - 100)) * (Seillaenge - 100)

    SegelServo.ChangeDutyCycle(Pulsweite)

    return True


# test test, noch lassen fuer Christine
while True:
    InputWinkel = float(input("Winkel des Hauptsegels:"))
    SegelWinkel(InputWinkel)