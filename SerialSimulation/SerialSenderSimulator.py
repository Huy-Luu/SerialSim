import serial
import numpy as np

class SerialSenderSimulator():
    def __init__(self, port, baudrate):
        self.sender = serial.Serial(port, baudrate)

    def sendSentence(self, sentence):
        self.sender.write(sentence.encode())

    def readFromText(self, fileDir):
        file = open(fileDir, 'r')
        lines = file.readlines()
        return lines