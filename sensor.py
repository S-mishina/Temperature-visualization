import serial
import time
ser = serial.Serial('/dev/tty.usbmodem14101', 9600)
while (1):
    print(ser.readline())
    time.sleep(0.1)