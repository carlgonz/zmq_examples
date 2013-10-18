import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    # Wait for next request from client
    message = b"Hi there!"
    socket.send(message)
    time.sleep(1)