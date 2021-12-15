
# CST 205 Multimedia Design & Programing 
# Group 808
# Date: December 2nd 2021
# Abstract:
# Authors: Yssa Traore, Shane Cromer, Ivan Martinez, and Tuan Nguyen 

from PyQt6 import QtCore, QtGui, QtWidgets
import pygame
from tkinter import *
from playsound import playsound


pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.mixer.init()




class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
       
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 10, 77, 146))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("Kick-01")
        self.pushButton_6.clicked.connect(self.B6)
        self.pushButton_6.setStyleSheet("QPushButton { background-color: yellow }"
                      "QPushButton:pressed { background-color: red }" )

        # self.pushButton_6.setStyleSheet("background-color : yellow")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("Kick-02")
        self.pushButton_7.clicked.connect(self.B7)
        self.pushButton_7.setStyleSheet("QPushButton { background-color: yellow }"
                      "QPushButton:pressed { background-color: red }" )
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("Kick-003")
        self.pushButton_8.setStyleSheet("QPushButton { background-color: yellow }"
                      "QPushButton:pressed { background-color: red }" )
        self.pushButton_8.clicked.connect(self.B8)
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName("Kick-004")
        self.pushButton_9.setStyleSheet("QPushButton { background-color: yellow }"
                      "QPushButton:pressed { background-color: red }" )
        self.pushButton_9.clicked.connect(self.B9)
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName("Kick-005")
        self.pushButton_10.setStyleSheet("QPushButton { background-color: yellow }"
                      "QPushButton:pressed { background-color: red }" )
        self.pushButton_10.clicked.connect(self.B10)
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(190, 10, 77, 146))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_11.setObjectName("Snare-01")
        self.pushButton_11.setStyleSheet("QPushButton { background-color: red }"
                      "QPushButton:pressed { background-color: gray }" )
        self.pushButton_11.clicked.connect(self.B11)
        self.verticalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_12.setObjectName("Snare-02")
        self.pushButton_12.setStyleSheet("QPushButton { background-color: red }"
                      "QPushButton:pressed { background-color: gray }" )
        self.verticalLayout_3.addWidget(self.pushButton_12)
        self.pushButton_12.clicked.connect(self.B12)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_13.setObjectName("Snare-03")
        self.pushButton_13.setStyleSheet("QPushButton { background-color: red }"
                      "QPushButton:pressed { background-color: gray }" )
        self.pushButton_13.setStyleSheet("background-color: red");
        self.pushButton_13.clicked.connect(self.B13)
        self.verticalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_14.setObjectName("Snare-04")
        self.pushButton_14.setStyleSheet("QPushButton { background-color: red }"
                      "QPushButton:pressed { background-color: gray }" )
        self.pushButton_14.clicked.connect(self.B14)
        self.verticalLayout_3.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_15.setObjectName("Snare-05")
        self.pushButton_15.setStyleSheet("QPushButton { background-color: red }"
                      "QPushButton:pressed { background-color: gray }" )
        self.pushButton_15.clicked.connect(self.B15)
        self.verticalLayout_3.addWidget(self.pushButton_15)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(280, 10, 77, 146))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_16.setObjectName("Cymbal-01")
        self.pushButton_16.setStyleSheet("QPushButton { background-color: blue }"
                      "QPushButton:pressed { background-color: green }" )
        self.pushButton_16.clicked.connect(self.B16)
        self.verticalLayout_4.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_17.setObjectName("Cymbal-02")
        self.pushButton_17.setStyleSheet("QPushButton { background-color: blue}"
                      "QPushButton:pressed { background-color: green }" )
        self.pushButton_17.clicked.connect(self.B17)
        self.verticalLayout_4.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_18.setObjectName("Cymbal-03")
        self.pushButton_18.setStyleSheet("QPushButton { background-color: blue }"
                      "QPushButton:pressed { background-color: green }" )
        self.verticalLayout_4.addWidget(self.pushButton_18)
        self.pushButton_18.clicked.connect(self.B18)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_19.setObjectName("Cymbal-04")
        self.pushButton_19.setStyleSheet("QPushButton { background-color: bleu }"
                      "QPushButton:pressed { background-color: green }" )
        self.verticalLayout_4.addWidget(self.pushButton_19)
        self.pushButton_19.clicked.connect(self.B19)
        self.pushButton_20 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_20.setObjectName("Cymbal-05")
        self.pushButton_20.setStyleSheet("QPushButton { background-color: bleu }"
                      "QPushButton:pressed { background-color: green }" )
        self.pushButton_20.clicked.connect(self.B20)
        self.verticalLayout_4.addWidget(self.pushButton_20)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 77, 146))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("DR110CHT.wav")
        self.pushButton.clicked.connect(self.B1)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("DR110KIK.wav")
        self.pushButton_4.clicked.connect(self.B4)
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("DR110OHT.wav")
        self.pushButton_5.clicked.connect(self.B5)
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("DR110CYM.wav")
        self.pushButton_3.clicked.connect(self.B3)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("DR110CLP.wav")
        self.pushButton_2.clicked.__setattr__
        self.pushButton_2.clicked.connect(self.B2)
        self.verticalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def B1(self):
        # playsound('sounds\Take_Me_On.mp3')
        pygame.mixer.music.load('DR110CHT.wav')
        pygame.mixer.music.play(loops=0)

    def B2(self):
        pygame.mixer.music.load('DR110CLP.wav')
        pygame.mixer.music.play(loops=0)

    def B3(self):
        pygame.mixer.music.load('DR110CYM.wav')
        pygame.mixer.music.play(loops=0)

    def B4(self):
        pygame.mixer.music.load('DR110KIK.wav')
        pygame.mixer.music.play(loops=0)

    def B5(self):
        pygame.mixer.music.load('DR110OHT.wav')
        pygame.mixer.music.play(loops=0)

    def B6(self):
        pygame.mixer.music.load('Kick-08.wav')
        pygame.mixer.music.play(loops=0)

    def B7(self):
        pygame.mixer.music.load('Kick-01.wav')
        pygame.mixer.music.play(loops=0)

    def B8(self):
        pygame.mixer.music.load('Kick-02.wav')
        pygame.mixer.music.play(loops=0)

    def B9(self):
        pygame.mixer.music.load('Kick-03.wav')
        pygame.mixer.music.play(loops=0)

    def B10(self):
        pygame.mixer.music.load('Kick-04.wav')
        pygame.mixer.music.play(loops=0)

    def B11(self):
        pygame.mixer.music.load('Snare-01.wav')
        pygame.mixer.music.play(loops=0)

    def B12(self):
        pygame.mixer.music.load('Snare-02.wav')
        pygame.mixer.music.play(loops=0)


    def B13(self):
        pygame.mixer.music.load('Snare-03.wav')
        pygame.mixer.music.play(loops=0)
    
    def B14(self):
        pygame.mixer.music.load('Snare-04.wav')
        pygame.mixer.music.play(loops=0)

    def B15(self):
        pygame.mixer.music.load('Snare-05.wav')
        pygame.mixer.music.play(loops=0)

    def B16(self):
        pygame.mixer.music.load('Cymbal-01.wav')
        pygame.mixer.music.play(loops=0)

    def B17(self):
        pygame.mixer.music.load('Cymbal-02.wav')
        pygame.mixer.music.play(loops=0)

    def B18(self):
        pygame.mixer.music.load('Cymbal-03.wav')
        pygame.mixer.music.play(loops=0)

    def B19(self):
        pygame.mixer.music.load('Cymbal-04.wav')
        pygame.mixer.music.play(loops=0)

    def B20(self):
        pygame.mixer.music.load('Cymbal-05.wav')
        pygame.mixer.music.play(loops=0)

    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "Kick-01"))
        self.pushButton_7.setText(_translate("MainWindow", "Kick-02"))
        self.pushButton_8.setText(_translate("MainWindow", "Kick-03"))
        self.pushButton_9.setText(_translate("MainWindow", "Kick-04"))
        self.pushButton_10.setText(_translate("MainWindow", "Kick-05"))
        self.pushButton_11.setText(_translate("MainWindow", "Snare-01"))
        self.pushButton_12.setText(_translate("MainWindow", "Snare-02"))
        self.pushButton_13.setText(_translate("MainWindow", "Snare-03"))
        self.pushButton_14.setText(_translate("MainWindow", "Snare-04"))
        self.pushButton_15.setText(_translate("MainWindow", "Snare-05"))
        self.pushButton_16.setText(_translate("MainWindow", "Cymbal-01"))
        self.pushButton_17.setText(_translate("MainWindow", "Cymbal-02"))
        self.pushButton_18.setText(_translate("MainWindow", "Cymbal-03"))
        self.pushButton_19.setText(_translate("MainWindow", "Cymbal-04"))
        self.pushButton_20.setText(_translate("MainWindow", "Cymbal-05"))
        self.pushButton.setText(_translate("MainWindow", "DR110CHT"))
        self.pushButton_4.setText(_translate("MainWindow", "DR110CLP"))
        self.pushButton_5.setText(_translate("MainWindow", "DR110CYM"))
        self.pushButton_3.setText(_translate("MainWindow", "DR110KIK"))
        self.pushButton_2.setText(_translate("MainWindow", "Clap"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
