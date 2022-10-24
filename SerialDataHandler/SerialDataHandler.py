import serial
import numpy as np

class SerialDataHandler():
    def __init__(self, port, baudrate):
        self.handler = serial.Serial(port, baudrate)

    def handlePositionData(self, utm, shift):
        incoming = self.handler.readline()
        converted = str(incoming,'ascii').rstrip()
        data = np.fromstring(converted,dtype = float, sep = ',')
        x, y = utm.fromLatLon(data[0], data[1])
        x = x - shift.x
        y = y - shift.y
        yaw = data[2]
        v = data[3]
        return x, y, yaw, v

