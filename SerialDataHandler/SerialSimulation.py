from SerialDataHandler import SerialDataHandler
from Point import Point
from MQTTclient import MQTTclient

client = MQTTclient("broker.hivemq.com", 1883, "SimulationCart")
client.init("control/auto")
point_to_send = Point(0, 0)
serialHandler = SerialDataHandler('COM1', 115200)

while True:
    x, y, yaw, v = serialHandler.receiveFourInputs()
    point_to_send.set(x, y)
    message = str(point_to_send.getY()) + "," + str(point_to_send.getX()) + "," + "0" + "," + "0" + "," + "0" + "," + str(v) + "," + str(yaw)
    client.publish(message, "data/position")

    print(x, y, yaw, v)