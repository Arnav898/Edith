import webbrowser
from EdithUi import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer,QTime,QDate
from PyQt5.uic import loadUiType
import Edith
import os
import sys


class Mainthread(QThread):
    def _init_(self):
        super(Mainthread,self).__init__()
    def run(self):
        Edith.Task_Gui()

class Gui_Start(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.gui=Ui_MainWindow()
        self.Gui.setupUi(self)

        
    
    def chrome_app(self):
        Main.Speak("Opening Chrome....")
        os.startfile("chrome app")

    def yt_app(self):
        webbrowser.open("https://www.youtube.com/")

    def whats_app(self):
        webbrowser.open("https://www.web.whatsapp.com/")



GuiApp=QApplication(sys.argv)
edith_ui=Gui_Start()
edith_ui.show()
exit(Gui_App.exec_())
    


