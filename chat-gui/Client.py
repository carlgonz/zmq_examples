from PyQt4.QtCore import QObject, pyqtSignal
from threading import Thread
import zmq


class Client(QObject):

    new_message = pyqtSignal(str)

    def __init__(self, username, server="localhost", send_port="5557", recv_port="5556"):
        QObject.__init__(self)
        self.username = username
        self.context = zmq.Context()

        #Sender socket using PULL-PUSH pattern
        self.sender_socket = self.context.socket(zmq.PUSH)
        self.sender_socket.connect("tcp://{0}:{1}".format(server, send_port))

        #Receiver socket using SUB_PUB pattern
        self.receiver_socket = self.context.socket(zmq.SUB)
        self.receiver_socket.connect("tcp://{0}:{1}".format(server, recv_port))
        self.receiver_socket.setsockopt(zmq.SUBSCRIBE, b"")

        #Start receiver thread
        self.recv_thread = Thread(target=self.receive, daemon=True)
        self.recv_thread.start()

    def receive(self):
        while True:
            #Get the publisher's message
            message = self.receiver_socket.recv()
            self.new_message.emit(str(message))

    def send(self, message):
        message = "{0} says: {1}".format(self.username, message)
        self.sender_socket.send(message.encode())


