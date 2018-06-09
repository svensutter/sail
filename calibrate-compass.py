# Dieses Skript kann aufgerufen werden, um die Min/Max-Werte von X Y und Z des Kompass
# zu erhalten. Dazu muss der Kompass in alle Richtungen (3D) gedreht werden waehrend
# das Skript laeuft.

# Sobald Werte konstant bleiben, kann Skript abgebrochen werden, und die Werte in
# das CONFIG von mdcompass uebernommen werden.

import mdhmc5883l
import time
import os

x_max = 0
x_min = 0
y_max = 0
y_min = 0
z_max = 0
z_min = 0

while True:
    x = mdhmc5883l.read_raw_data(0x03)
    z = mdhmc5883l.read_raw_data(0x05)
    y = mdhmc5883l.read_raw_data(0x07)

    if x > x_max:
        x_max = x
    elif x < x_min:
        x_min = x

    if y > y_max:
        y_max = y
    elif y < y_min:
        y_min = y

    if z > z_max:
        z_max = z
    elif z < z_min:
        z_min = z

    os.system("clear")
    print("x-max:", x_max)
    print("x-min:", x_min)
    print("y-max:", y_max)
    print("y-min:", y_min)
    print("z-max:", z_max)
    print("z-min:", z_min)
    print("\n")
    print("x-Offset:", (x_min + x_max) / 2)
    print("y-Offset:", (y_min + y_max) / 2)
    print("z-Offset:", (z_min + z_max) / 2)

    time.sleep(0.01)