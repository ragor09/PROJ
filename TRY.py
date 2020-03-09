import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtCore import pyqtSlot, QSize

class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        oImage = QImage("calculate.jpg")
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        sImage = oImage.scaled(QSize(550,350))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                        
        self.setPalette(palette)
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("1")
        self.textboxlbl = QLabel("1",self)
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightblue")
        self.buttonback.move(150,250)
        self.buttonback.clicked.connect(self.Window2)
        
    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()


class Window4(QMainWindow):
     def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(550,350))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                        
        self.setPalette(palette)
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("2")
        self.textboxlbl = QLabel("2",self)
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightblue")
        self.buttonback.move(150,250)
        self.buttonback.clicked.connect(self.Window2)
        
     def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()
    
class Window5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        self.setGeometry(200,200,600,350)
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(550,350))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                        
        self.setPalette(palette)
        self.setWindowTitle("3")
        self.textboxlbl = QLabel("3",self)
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightblue")
        self.buttonback.move(150,250)
        self.buttonback.clicked.connect(self.Window2)
        
    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()
    
    
class Window2(QMainWindow):                         
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PHYSICS(calculus-based)")
        self.setWindowIcon(QIcon('young-lion_97429.ico')) 
        oImage = QImage("first.jpg")
        sImage = oImage.scaled(QSize(550,350))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                        
        self.setPalette(palette)
        self.setStyleSheet
        self.setGeometry(200,200,600,350)
        self.textboxlbl = QLabel("<h1>PHYSICS</h1>",self)
        self.textboxlbl.move(255, 30)
        self.textboxlbl.setFont(QtGui.QFont('Lucida Handwriting', 7))
        self.textboxlb2 = QLabel("<h2>Topics</h2>",self)
        self.textboxlb2.move(265, 55)
        self.textboxlb2.setFont(QtGui.QFont('Castellar', 7))
        self.button2 = QPushButton("CALCULATE", self)
        self.button2.setToolTip("Calculate the formula")
        self.button2.setStyleSheet("background-color:pink")
        self.button2.move(150,90)
        self.button2.resize(300,30)
        self.button3 = QPushButton("CALCULATE 2", self)
        self.button3.setToolTip("Calculate the formula")
        self.button3.setStyleSheet("background-color:pink")
        self.button3.move(150,150)
        self.button3.resize(300,30)
        self.button4 = QPushButton("CALCULATE 3", self)
        self.button4.setToolTip("Calculate the formula")
        self.button4.setStyleSheet("background-color:pink")
        self.button4.move(150,210)
        self.button4.resize(300,30)
        

        self.button2.clicked.connect(self.Window3)
        self.button3.clicked.connect(self.Window4)
        self.button4.clicked.connect(self.Window5)


    def Window3(self):                                             # <===
        self.w = Window3()
        self.w.show()
        self.hide()
        
    def Window4(self):                                             # <===
        self.w = Window4()
        self.w.show()
        self.hide()
        
    def Window5(self):                                             # <===
        self.w = Window5()
        self.w.show()
        self.hide()
    
    
    

class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        
        self.title = "PHYSICS"
        self.x=200 
        self.y=200 
        self.width=600
        self.height=350
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('young-lion_97429.ico')) 
        oImage = QImage("explore.jpg")
        sImage = oImage.scaled(QSize(550,350))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.textboxlbl = QLabel("<h1>PHYSICS</h1>",self)
        self.textboxlbl.move(200, 70)
        self.textboxlbl.setFont(QtGui.QFont('Lucida Fax',18))
        self.textboxlb2= QLabel("<h2>Calculus-Based</h2>",self)
        self.textboxlb2.move(215, 130)
        self.textboxlb2.setFont(QtGui.QFont('Monotype Corsiva', 13))

        self.button = QPushButton('EXPLORE', self)
        self.button.setToolTip("Explore the wonderinfo")
        self.button.move(255,170)
        self.button.setStyleSheet("background-color:lightblue")
       
        self.button.clicked.connect(self.Window2)
    
        self.show()

    def Window2(self):                                             # <===
        self.w = Window2()
        self.w.show()
        self.hide()

        

        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())
