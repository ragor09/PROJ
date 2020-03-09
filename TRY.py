import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import pyqtSlot, QSize

class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("1")
        self.textboxlbl = QLabel("1",self)

class Window4(QMainWindow):
     def __init__(self):
        super().__init__()
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("2")
        self.textboxlbl = QLabel("2",self)
    
class Window5(QMainWindow):
    def __init__(self):
        self.setGeometry(200,200,600,350)
        super().__init__()
        self.setWindowTitle("3")
        self.textboxlbl = QLabel("3",self)
    
    
class Window2(QMainWindow):                         
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHYSICS(calculus-based)")
        self.setWindowIcon(QIcon('young-lion_97429.ico')) 

        self.setGeometry(200,200,600,350)
        self.textboxlbl = QLabel("<h1>PHYSICS</h1>",self)
        self.textboxlbl.move(245, 10)
        self.textboxlb2 = QLabel("<h2>Topics</h2>",self)
        self.textboxlb2.move(265, 35)
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
        self.textboxlbl.move(245, 130)
        self.textboxlb2= QLabel("<h2>Calculus-Based</h2>",self)
        self.textboxlb2.move(225, 160)

        self.button = QPushButton('EXPLORE', self)
        self.button.setToolTip("Explore the wonderinfo")
        self.button.move(255,190)
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
