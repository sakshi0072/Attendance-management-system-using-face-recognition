# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'att_p.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_att(object):
    def python(self):
        from python import python
        self.window = QtWidgets.QMainWindow()
        self.ui = python()
        self.ui.setupUi(self.window)
        self.window.show()

    def maths(self):
        from maths import maths
        self.window = QtWidgets.QMainWindow()
        self.ui = maths()
        self.ui.setupUi(self.window)
        self.window.show()

    def automata(self):
        from at import automata
        self.window = QtWidgets.QMainWindow()
        self.ui = automata()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 802)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(3, 127, 236);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 50, 600, 120))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 157,100);\n"
"border-radius:20px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 230, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("background-color: rgb(2, 77, 205);\n"
"border-radius:20px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 360, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("background-color: rgb(2, 77, 205);\n"
"border-radius:20px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 490, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("background-color: rgb(2, 77, 205);\n"
"border-radius:20px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 620, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("background-color: rgb(2, 77, 205);\n"
"border-radius:20px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 360, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0,120);\n"
"border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.python)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 490, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0,120);\n"
"border-radius:20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.maths)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 620, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 0, 0,120);\n"
"border-radius:20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.automata)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ATTENDANCE TRACKER"))
        self.label_2.setText(_translate("MainWindow", "SUBJETS"))
        self.label_3.setText(_translate("MainWindow", "Python"))
        self.label_4.setText(_translate("MainWindow", "Maths "))
        self.label_5.setText(_translate("MainWindow", "Automata Theory"))
        self.pushButton.setText(_translate("MainWindow", "FACE TRACK"))
        self.pushButton_2.setText(_translate("MainWindow", "FACE TRACK"))
        self.pushButton_3.setText(_translate("MainWindow", "FACE TRACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_att()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
