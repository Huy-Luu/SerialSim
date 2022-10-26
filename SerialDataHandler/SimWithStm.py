from SerialDataHandler import SerialDataHandler
import time

serialHandler = SerialDataHandler('COM3', 115200)
count = 0

while True:
    serialHandler.send("m")
    x, y =serialHandler.receiveTwoInputs()
    print(x, y, count)
    time.sleep(0.05)
    count += 1