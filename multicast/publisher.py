import zmq
from time import sleep

# Socket to broadcast messages
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("epgm://eth0;172.17.1.1:5556")

# Broadcast N messages
for i in range(100):
    # Message construcction
    message = "ping-{}".format(i).encode("ascii")
    print("Sending:", message)
    
    # Broadcast message to all subscribers
    sleep(1)
    socket.send(message)
