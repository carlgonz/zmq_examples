import zmq

IP = "192.168.1.137"

print("Connecting to server... ")
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://{}:5555".format(IP))

for i in range(10):
    # Send a message to server
    message = "Helo {} ".format(i)
    socket.send(message.encode())

    #Get the reply
    message = socket.recv()
    print(message)

socket.send(b"end")
print("Client closed")
