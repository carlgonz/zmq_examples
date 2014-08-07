import zmq

#IP = "192.168.1.137"
IP = "localhost"

print("Connecting to publisher... ")
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("epgm://eth0;172.17.1.1:5556")
socket.setsockopt(zmq.SUBSCRIBE, b"")

while True:
    #Get the publisher's message
    message = socket.recv()
    print(message)
