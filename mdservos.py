# Das Modul mdservos beinhaltet die Funktionen, um die Servos (Ruder, Segel) anzusteuern.

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # Belegung GPIO-Ports definieren
GPIO.setwarnings(False) # Sonst kommt Warnung "Channel already in use"

# Initialisierung Ruder-Servo
GPIO.setup(17, GPIO.OUT)
RuderServo = GPIO.PWM(17, 50) # Pin 17 mit 50 Hz
RuderServo.start(2.5)

# Funktion RuderWinkel() nimmt Winkelwert zw. -45 und 45 entgegen und
# stellt das Ruder entsprechend ein. Die Minuswerte sind links.
def RuderWinkel(Winkel):

    if not (Winkel <= 45 and Winkel >= -45):
        print("Funktion RuderWinkel hat Wert ausserhalb des gueltigen Bereichs erhalten.")
        return False

    Pulsweite = 5 + ((5 / 90) * (Winkel + 45))

    RuderServo.ChangeDutyCycle(Pulsweite)

    return True