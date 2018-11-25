
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 09:50:57 2018

@author: mimota
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
import mainPro

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        qbtn = QPushButton('ready', self)
        qbtn.clicked.connect(mainPro.mainLoop)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('superbin')
        self.show()
        
app = QApplication(sys.argv)
ex= Example()
sys.exit(app.exec_())