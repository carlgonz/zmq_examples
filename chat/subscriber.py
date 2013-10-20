import zmq

#IP = "192.168.1.137"
IP = "localhost"

print("Connecting to publisher... ")
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://{}:5556".format(IP))
socket.setsockopt(zmq.SUBSCRIBE, b"")

while True:
    #Get the publisher's message
    message = socket.recv()
    print(message)
