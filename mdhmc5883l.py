# Modul aus dem Internet kopiert und angepasst.
# Funktionen fuer Hardwarezugriff auf Kompass, um Register auszulesen
# mit dem Ziel die Rohwerte der Achsen X Y Z zu bekommen, als Grundlage
# fuer die Berechnung des Kompasswinkels mit Beruecksichtigung der Neigung.

import smbus		#import SMBus module of I2C

#some MPU6050 Registers and their Address
Register_A     = 0              #Address of Configuration register A
Register_B     = 0x01           #Address of configuration register B
Register_mode  = 0x02           #Address of mode register


def Magnetometer_Init():
        #write to Configuration Register A
        bus.write_byte_data(Device_Address, Register_A, 0x70)

        #Write to Configuration Register B for gain
        bus.write_byte_data(Device_Address, Register_B, 0xa0)

        #Write to mode Register for selecting mode
        bus.write_byte_data(Device_Address, Register_mode, 0)
	
	

def read_raw_data(addr):
    
        #Read raw 16-bit value
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from module
        if(value > 32768):
            value = value - 65536
        return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x1e   # HMC5883L magnetometer device address

Magnetometer_Init()     # initialize HMC5883L magnetometer