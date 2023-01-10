#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agv_interface2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
import time
import rospy
import rospkg
from rviz import bindings as rviz
from PyQt5 import uic, QtGui, QtCore,QtWidgets
from PyQt5.QtCore import Qt
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseWithCovarianceStamped
import asyncio
from quamash import QEventLoop
import kavurlar_logo_rc
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import threading


class Ui_MainWindow(object):
   
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1469, 799)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/kavurlar_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.positionZ = QtWidgets.QLineEdit(self.centralwidget)
        self.positionZ.setObjectName("positionZ")
        self.gridLayout_4.addWidget(self.positionZ, 3, 3, 1, 1)
        self.slopeZ = QtWidgets.QLineEdit(self.centralwidget)
        self.slopeZ.setObjectName("slopeZ")
        self.gridLayout_4.addWidget(self.slopeZ, 4, 3, 1, 1)
        self.positionX = QtWidgets.QLineEdit(self.centralwidget)
        self.positionX.setText("")
        self.positionX.setObjectName("positionX")
        self.gridLayout_4.addWidget(self.positionX, 3, 1, 1, 1)
        self.positionY = QtWidgets.QLineEdit(self.centralwidget)
        self.positionY.setText("")
        self.positionY.setObjectName("positionY")
        self.gridLayout_4.addWidget(self.positionY, 3, 2, 1, 1)
        self.slopeLabel = QtWidgets.QLabel(self.centralwidget)
        self.slopeLabel.setObjectName("slopeLabel")
        self.gridLayout_4.addWidget(self.slopeLabel, 4, 0, 1, 1)
        self.slopeY = QtWidgets.QLineEdit(self.centralwidget)
        self.slopeY.setObjectName("slopeY")
        self.gridLayout_4.addWidget(self.slopeY, 4, 2, 1, 1)
        self.statusBattery = QtWidgets.QLineEdit(self.centralwidget)
        self.statusBattery.setObjectName("statusBattery")
        self.gridLayout_4.addWidget(self.statusBattery, 2, 1, 1, 1)
        self.instantaneousVelocityLabel = QtWidgets.QLabel(self.centralwidget)
        self.instantaneousVelocityLabel.setObjectName("instantaneousVelocityLabel")
        self.gridLayout_4.addWidget(self.instantaneousVelocityLabel, 1, 0, 1, 1)
        self.instantaneousVelocityY = QtWidgets.QLineEdit(self.centralwidget)
        self.instantaneousVelocityY.setObjectName("instantaneousVelocityY")
        self.gridLayout_4.addWidget(self.instantaneousVelocityY, 1, 2, 1, 1)
        self.position = QtWidgets.QLabel(self.centralwidget)
        self.position.setObjectName("position")
        self.gridLayout_4.addWidget(self.position, 3, 0, 1, 1)
        self.statusBatteryLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusBatteryLabel.setObjectName("statusBatteryLabel")
        self.gridLayout_4.addWidget(self.statusBatteryLabel, 2, 0, 1, 1)
        self.slopeX = QtWidgets.QLineEdit(self.centralwidget)
        self.slopeX.setObjectName("slopeX")
        self.gridLayout_4.addWidget(self.slopeX, 4, 1, 1, 1)
        self.instantaneousVelocityX = QtWidgets.QLineEdit(self.centralwidget)
        self.instantaneousVelocityX.setObjectName("instantaneousVelocityX")
        self.gridLayout_4.addWidget(self.instantaneousVelocityX, 1, 1, 1, 1)
        self.frame = rviz.VisualizationFrame()
        self.frame.setSplashPath( "" )
        self.frame.initialize()
        reader = rviz.YamlConfigReader()
        config = rviz.Config()		
        reader.readFile( config, "/home/kavurlar/catkin_ws/src/diff_om_drive/rviz_config/config.rviz" )
        self.frame.load( config )	

        self.frame.setMenuBar( None )
        self.frame.setStatusBar( None )
        self.frame.setHideButtonVisibility( True )
        self.manager = self.frame.getManager()
        self.gridLayout_4.addWidget(self.frame, 0, 4, 7, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.startMappingButton = QtWidgets.QPushButton(self.centralwidget)
        self.startMappingButton.setMinimumSize(QtCore.QSize(0, 40))
        self.startMappingButton.setBaseSize(QtCore.QSize(30, 100))
        self.startMappingButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.startMappingButton.setObjectName("startMappingButton")
        self.gridLayout.addWidget(self.startMappingButton, 0, 0, 1, 1)
        self.startRouteButton = QtWidgets.QPushButton(self.centralwidget)
        self.startRouteButton.setMinimumSize(QtCore.QSize(0, 40))
        self.startRouteButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.startRouteButton.setObjectName("startRouteButton")
        self.gridLayout.addWidget(self.startRouteButton, 0, 1, 1, 1)
        self.startAutonomousButton = QtWidgets.QPushButton(self.centralwidget)
        self.startAutonomousButton.setMinimumSize(QtCore.QSize(0, 40))
        self.startAutonomousButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.startAutonomousButton.setObjectName("startAutonomousButton")
        self.gridLayout.addWidget(self.startAutonomousButton, 0, 2, 1, 1)
        self.stopMappingButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopMappingButton.setMinimumSize(QtCore.QSize(0, 40))
        self.stopMappingButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.stopMappingButton.setObjectName("stopMappingButton")
        self.gridLayout.addWidget(self.stopMappingButton, 1, 0, 1, 1)
        self.stopRouteButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopRouteButton.setMinimumSize(QtCore.QSize(0, 40))
        self.stopRouteButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.stopRouteButton.setObjectName("stopRouteButton")
        self.gridLayout.addWidget(self.stopRouteButton, 1, 1, 1, 1)
        self.StopAutonomoustButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopAutonomoustButton.setMinimumSize(QtCore.QSize(0, 40))
        self.StopAutonomoustButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.StopAutonomoustButton.setObjectName("StopAutonomoustButton")
        self.gridLayout.addWidget(self.StopAutonomoustButton, 1, 2, 1, 1)
        self.saveMappingButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveMappingButton.setMinimumSize(QtCore.QSize(0, 40))
        self.saveMappingButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.saveMappingButton.setObjectName("saveMappingButton")
        self.gridLayout.addWidget(self.saveMappingButton, 2, 0, 1, 1)
        self.routeCoordinateButton = QtWidgets.QPushButton(self.centralwidget)
        self.routeCoordinateButton.setMinimumSize(QtCore.QSize(0, 40))
        self.routeCoordinateButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.routeCoordinateButton.setObjectName("routeCoordinateButton")
        self.gridLayout.addWidget(self.routeCoordinateButton, 2, 1, 1, 1)
        self.autonomousSettingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.autonomousSettingsButton.setMinimumSize(QtCore.QSize(0, 40))
        self.autonomousSettingsButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.autonomousSettingsButton.setObjectName("autonomousSettingsButton")
        self.gridLayout.addWidget(self.autonomousSettingsButton, 2, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.linearVelocityUp = QtWidgets.QPushButton(self.centralwidget)
        self.linearVelocityUp.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.linearVelocityUp.setObjectName("linearVelocityUp")
        self.gridLayout_3.addWidget(self.linearVelocityUp, 0, 0, 1, 1)
        self.linearVelocityDown = QtWidgets.QPushButton(self.centralwidget)
        self.linearVelocityDown.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.linearVelocityDown.setObjectName("linearVelocityDown")
        self.gridLayout_3.addWidget(self.linearVelocityDown, 0, 1, 1, 1)
        self.AngularVelocityUp = QtWidgets.QPushButton(self.centralwidget)
        self.AngularVelocityUp.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.AngularVelocityUp.setObjectName("AngularVelocityUp")
        self.gridLayout_3.addWidget(self.AngularVelocityUp, 1, 0, 1, 1)
        self.angularVelocityDown = QtWidgets.QPushButton(self.centralwidget)
        self.angularVelocityDown.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.angularVelocityDown.setObjectName("angularVelocityDown")
        self.gridLayout_3.addWidget(self.angularVelocityDown, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.leftForwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftForwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.leftForwardButton.setObjectName("leftForwardButton")
        self.gridLayout_2.addWidget(self.leftForwardButton, 0, 0, 1, 1)
        self.forwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.forwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.forwardButton.setObjectName("forwardButton")
        self.gridLayout_2.addWidget(self.forwardButton, 0, 1, 1, 1)
        self.rightForwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightForwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.rightForwardButton.setObjectName("rightForwardButton")
        self.gridLayout_2.addWidget(self.rightForwardButton, 0, 2, 1, 1)
        self.leftButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.leftButton.setObjectName("leftButton")
        self.gridLayout_2.addWidget(self.leftButton, 1, 0, 1, 1)
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.StopButton.setObjectName("StopButton")
        self.gridLayout_2.addWidget(self.StopButton, 1, 1, 1, 1)
        self.rightButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.rightButton.setObjectName("rightButton")
        self.gridLayout_2.addWidget(self.rightButton, 1, 2, 1, 1)
        self.leftBackwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftBackwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.leftBackwardButton.setObjectName("leftBackwardButton")
        self.gridLayout_2.addWidget(self.leftBackwardButton, 2, 0, 1, 1)
        self.backwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.backwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.backwardButton.setObjectName("backwardButton")
        self.gridLayout_2.addWidget(self.backwardButton, 2, 1, 1, 1)
        self.rightBackwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightBackwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.rightBackwardButton.setObjectName("rightBackwardButton")
        self.gridLayout_2.addWidget(self.rightBackwardButton, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 5, 0, 1, 4)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 6, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1469, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kavurlar-Agv"))
        self.slopeLabel.setText(_translate("MainWindow", "Eğim:"))
        self.instantaneousVelocityLabel.setText(_translate("MainWindow", "Anlık Hız:"))
        self.position.setText(_translate("MainWindow", "Konum:"))
        self.statusBatteryLabel.setText(_translate("MainWindow", "Batarya Durumu:"))
        self.startMappingButton.setText(_translate("MainWindow", "Harita Başlat"))
        self.startRouteButton.setText(_translate("MainWindow", "Rota Başlat"))
        self.startAutonomousButton.setText(_translate("MainWindow", "Otonom Başlat"))
        self.stopMappingButton.setText(_translate("MainWindow", "Harita Durdur"))
        self.stopRouteButton.setText(_translate("MainWindow", "Rota Durdur"))
        self.StopAutonomoustButton.setText(_translate("MainWindow", "Otonom Durdur"))
        self.saveMappingButton.setText(_translate("MainWindow", "Harita Kaydet"))
        self.routeCoordinateButton.setText(_translate("MainWindow", "Rota Koordinat"))
        self.autonomousSettingsButton.setText(_translate("MainWindow", "Otonom Ayarlar"))
        self.linearVelocityUp.setText(_translate("MainWindow", "Doğrusal Hız Artır"))
        self.linearVelocityDown.setText(_translate("MainWindow", "Doğrusal Hız Azalt"))
        self.AngularVelocityUp.setText(_translate("MainWindow", "Açısal Hız Artır"))
        self.angularVelocityDown.setText(_translate("MainWindow", "Açısal Hız Azalt"))
        self.leftForwardButton.setText(_translate("MainWindow", "SOL İLERİ"))
        self.forwardButton.setText(_translate("MainWindow", "İLERİ"))
        self.rightForwardButton.setText(_translate("MainWindow", "SAĞ İLERİ"))
        self.leftButton.setText(_translate("MainWindow", "SOL"))
        self.StopButton.setText(_translate("MainWindow", "DUR"))
        self.rightButton.setText(_translate("MainWindow", "SAĞ"))
        self.leftBackwardButton.setText(_translate("MainWindow", "SOL GERİ"))
        self.backwardButton.setText(_translate("MainWindow", "GERİ"))
        self.rightBackwardButton.setText(_translate("MainWindow", "SAĞ GERİ"))
        self.forwardButton.pressed.connect(self.forwardButtonPressed)
        self.forwardButton.released.connect(self.forwardButtonReleased) 
    
        
    

    def forwardButtonPressed(self):
        self.worker.setX(1000) 
        print("butona basıldı.")
                                
                
    def forwardButtonReleased(self):
        self.worker.setX(100000) 
        print("butondan çekildi.")
                
       
    send_key_signal = pyqtSignal(int)


class Worker(QObject):
    progress = pyqtSignal(int)

    xxx = 0
    def setX(self, nmb):
        print('aaa')
        self.xxx = nmb

    def run(self):
        self.xxx = 0
        while(True):
            self.xxx += 1
            print(str(self.xxx))
            QtCore.QThread.sleep(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

    
    
