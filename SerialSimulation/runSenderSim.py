from SerialSenderSimulator import SerialSenderSimulator
import time

senderSim = SerialSenderSimulator('COM1', 115200)
bigData = senderSim.readFromText('data2.txt')

for data in bigData:
    senderSim.sendSentence(data)
    time.sleep(0.2)

print(data)