import zmq

print("Connecting to server... ")
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print("Conected")

for i in range(10):
    # Send a message to server
    message = "Helo {} ".format(i)
    socket.send(message.encode())

    #Get the reply
    message = socket.recv()
    print(message)

socket.send(b"end")
print("Client closed")
