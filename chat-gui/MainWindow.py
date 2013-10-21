# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/MainWindow.ui'
#
# Created: Sun Oct 20 18:33:03 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(480, 431)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.message_text = QtGui.QLineEdit(self.centralwidget)
        self.message_text.setEnabled(False)
        self.message_text.setObjectName(_fromUtf8("message_text"))
        self.gridLayout.addWidget(self.message_text, 3, 1, 1, 1)
        self.send_button = QtGui.QPushButton(self.centralwidget)
        self.send_button.setEnabled(False)
        self.send_button.setObjectName(_fromUtf8("send_button"))
        self.gridLayout.addWidget(self.send_button, 3, 2, 1, 1)
        self.chat_text = QtGui.QTextEdit(self.centralwidget)
        self.chat_text.setEnabled(False)
        self.chat_text.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.chat_text.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.chat_text.setObjectName(_fromUtf8("chat_text"))
        self.gridLayout.addWidget(self.chat_text, 2, 1, 1, 2)
        self.connection_group = QtGui.QGroupBox(self.centralwidget)
        self.connection_group.setObjectName(_fromUtf8("connection_group"))
        self.gridLayout_2 = QtGui.QGridLayout(self.connection_group)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.server_text = QtGui.QLineEdit(self.connection_group)
        self.server_text.setObjectName(_fromUtf8("server_text"))
        self.gridLayout_2.addWidget(self.server_text, 0, 1, 1, 1)
        self.user_label = QtGui.QLabel(self.connection_group)
        self.user_label.setObjectName(_fromUtf8("user_label"))
        self.gridLayout_2.addWidget(self.user_label, 1, 0, 1, 1)
        self.user_text = QtGui.QLineEdit(self.connection_group)
        self.user_text.setObjectName(_fromUtf8("user_text"))
        self.gridLayout_2.addWidget(self.user_text, 1, 1, 1, 1)
        self.server_label = QtGui.QLabel(self.connection_group)
        self.server_label.setObjectName(_fromUtf8("server_label"))
        self.gridLayout_2.addWidget(self.server_label, 0, 0, 1, 1)
        self.connect_button = QtGui.QPushButton(self.connection_group)
        self.connect_button.setObjectName(_fromUtf8("connect_button"))
        self.gridLayout_2.addWidget(self.connect_button, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.connection_group, 1, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.menuFile.addAction(self.actionSalir)
        self.menubar.addAction(self.menuFile.menuAction())
        self.user_label.setBuddy(self.user_text)
        self.server_label.setBuddy(self.server_text)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.user_text, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.connect_button.click)
        QtCore.QObject.connect(self.server_text, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.connect_button.click)
        QtCore.QObject.connect(self.message_text, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.send_button.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.server_text, self.user_text)
        MainWindow.setTabOrder(self.user_text, self.connect_button)
        MainWindow.setTabOrder(self.connect_button, self.message_text)
        MainWindow.setTabOrder(self.message_text, self.send_button)
        MainWindow.setTabOrder(self.send_button, self.chat_text)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ZMQ - CHAT", None))
        self.send_button.setText(_translate("MainWindow", "Send", None))
        self.connection_group.setTitle(_translate("MainWindow", "Connection", None))
        self.server_text.setText(_translate("MainWindow", "localhost", None))
        self.user_label.setText(_translate("MainWindow", "Usuario", None))
        self.user_text.setText(_translate("MainWindow", "Usuario", None))
        self.server_label.setText(_translate("MainWindow", "Server", None))
        self.connect_button.setText(_translate("MainWindow", "Connect", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSalir.setText(_translate("MainWindow", "Exit", None))

