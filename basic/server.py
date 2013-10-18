import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Wait for next request from client
    message = socket.recv()
    print(message)

    if message == b"end":
        print("Shutdown")
        break

    #Process message or do some 'work'
    time.sleep(1)

    #Send reply back to clent
    socket.send(b"World")