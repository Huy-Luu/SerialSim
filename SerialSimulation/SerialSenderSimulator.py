import serial
import numpy as np

class SerialSebderSimulator():
    def __init__(self, port, baudrate):
        self.sender = serial.Serial(port, baudrate)

    def sendSentence(self):
        #retrive from data file
        self.sender.send(data)