import sys
from PyQt4 import QtGui
from Client import Client

from MainWindow import Ui_MainWindow


class App(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.connect_button.clicked.connect(self.start)
        self.ui.send_button.clicked.connect(self.send_msg)

        self.client = None

    def start(self):
        server = self.ui.server_text.text()
        username = self.ui.user_text.text()


        self.client = Client(username, server)
        self.client.new_message.connect(self.print_msg)

        self.ui.chat_text.setEnabled(True)
        self.ui.message_text.setEnabled(True)
        self.ui.send_button.setEnabled(True)

    def send_msg(self):
        message = self.ui.message_text.text()
        self.ui.message_text.clear()
        self.client.send(message)

    def print_msg(self, message):
        self.ui.chat_text.append(message)

app = QtGui.QApplication(sys.argv)
gui = App()
gui.show()
sys.exit(app.exec_())
