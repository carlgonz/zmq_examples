import zmq

#IP = "192.168.1.137"
IP = "localhost"

context = zmq.Context()

# Socket to send messages to
sender = context.socket(zmq.PUSH)
sender.connect("tcp://{}:5557".format(IP))

name = input("Enter name: ")

while True:
    message = input("Message: ")
    message = "{0} says: {1}".format(name, message)
    sender.send(message.encode())
