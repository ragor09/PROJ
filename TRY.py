import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QPixmap, QFont, QIntValidator, QDoubleValidator
from PyQt5.QtCore import pyqtSlot, QSize
from sqlitedict import *

class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.title = "Antipuesto"
        self.x=200 
        self.y=200 
        self.width=300
        self.height=200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("explore.jpg")
        sImage = oImage.scaled(QSize(200,200))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.createGridLayout()
        self.setLayout(self.layout) 
        self.show()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(3, 1)
        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(3, 0)

        self.label = QLabel(self)
        self.label.setGeometry(32,20,250,100)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)

        self.textboxlbl = QLabel("Username: ",self)
        self.textboxlbl.setFont(QtGui.QFont('Lucida Fax',15))
        self.textbox = QLineEdit(self)
        self.textbox.setFont(QtGui.QFont('Lucida Fax',11))
        self.textbox.setStyleSheet("""QLineEdit {border: 1.5px solid gray;
                                                border-radius: 4px;
                                                padding: 0 3px;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                }""")
        self.textboxlbl2 = QLabel("Password: ",self)
        self.textboxlbl2.setFont(QtGui.QFont('Lucida Fax',15))
        self.password = QLineEdit(self)
        self.password.setFont(QtGui.QFont('Lucida Fax',11))
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("""QLineEdit{border: 1.5px solid gray;
                                                border-radius: 4px;
                                                padding: 0 3px;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                }""")
        self.button = QPushButton('Login',self)
        self.button.setFont(QtGui.QFont('Lucida Fax',11))
        self.button.setStyleSheet("""QPushButton{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 6px;
                                                border-style: outset;
                                                background: rgb(203, 177, 242);
                                                selection-background-color: darkgray;}       
                                                QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button.setToolTip("Click to Login!")
        self.button.clicked.connect(self.Window2)
        self.register = QPushButton('Register',self)
        self.register.setFont(QtGui.QFont('Lucida Fax',11))
        self.register.setStyleSheet("""QPushButton{border: 2px solid gray;
                                                border-radius: 10px;
                                                border-width: 2px;
                                                border-style: outset;
                                                background: rgb(203, 177, 242);
                                                selection-background-color: darkgray;
                                                padding: 6px;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.register.setToolTip("Click to Login!")
        self.register.clicked.connect(self.registerWin)
        self.layout.addWidget(self.register,3,1)
        self.layout.addWidget(self.textboxlbl,1,1)
        self.layout.addWidget(self.textbox,1,2)
        self.layout.addWidget(self.textboxlbl2,2,1)
        self.layout.addWidget(self.password,2,2)
        self.layout.addWidget(self.button,3,2)
        
    def registerWin(self):
        self.w = registerWin()
        self.w.show()
        self.hide()

    def Window2(self):                                             
        self.w = Window2()
        self.w.show()
        self.hide()

class registerWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        self.title = "Registration"
        self.x=200
        self.y=200
        self.width=300
        self.height=200
        oImage = QImage("explore.jpg")
        sImage = oImage.scaled(QSize(200,200))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(20,45,270,150)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(3, 1)
        grid.setRowStretch(0, 0)
        grid.setRowStretch(3, 0)

        self.textboxlbl = QLabel("First Name:", self)
        self.textboxlbl.setFont(QtGui.QFont('Lucida Fax',11))
        self.textbox1 = QLineEdit(self)
        self.textbox1.setFont(QtGui.QFont('Lucida Fax',11))
        self.textbox1.setToolTip("Enter your First Name here")
        self.textbox1.setStyleSheet("""QLineEdit {border: 1.5px solid gray;
                                                border-radius: 4px;
                                                padding: 0 3px;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                }""")
       
        self.textboxlbl2 = QLabel("Last Name:", self)
        self.textboxlbl2.setFont(QtGui.QFont('Lucida Fax',11))
        self.textbox2 = QLineEdit(self)
        self.textbox2.setFont(QtGui.QFont('Lucida Fax',11))
        self.textbox2.setToolTip("Enter your Last Name here")
        self.textbox2.setStyleSheet("""QLineEdit {border: 1.5px solid gray;
                                                border-radius: 4px;
                                                padding: 0 3px;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                }""")
    
        self.textboxlbl3 = QLabel("Username:", self)
        self.textboxlbl3.setFont(QtGui.QFont('Lucida Fax',11))
        self.textbox3 = QLineEdit(self)
        self.textbox3.setFont(QtGui.QFont('Lucida Fax',11))
        self.textbox3.setToolTip("Enter Username here")
        self.textbox3.setStyleSheet("""QLineEdit {border: 1.5px solid gray;
                                                border-radius: 4px;
                                                padding: 0 3px;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                }""")
   
        self.textboxlbl4 = QLabel("Password:", self)
        self.textboxlbl4.setFont(QtGui.QFont('Lucida Fax',11))
        self.textbox4 = QLineEdit(self)
        self.textbox4.setFont(QtGui.QFont('Lucida Fax',11))
        self.textbox4.setToolTip("Enter Password here")
        self.textbox4.setEchoMode(QLineEdit.Password)
        self.textbox4.setStyleSheet("""QLineEdit {border: 1.5px solid gray;
                                                border-radius: 4px;
                                                padding: 0 3px;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                }""")
  
        self.button = QPushButton('Submit', self)
        self.button.setFont(QtGui.QFont('Lucida Fax',11))
        self.button.setToolTip("Submit your information")
        self.button.setStyleSheet("""QPushButton  {border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 6px;
                                                border-style: outset;
                                                background: rgb(203, 177, 242);
                                                selection-background-color: darkgray;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button.clicked.connect(self.data) 

        self.button2 = QPushButton('Clear',self)
        self.button2.setFont(QtGui.QFont('Lucida Fax',11))
        self.button2.setToolTip("Clear all")
        self.button2.setStyleSheet("""QPushButton  {border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 6px;
                                                border-style: outset;
                                                background: rgb(203, 177, 242);
                                                selection-background-color: darkgray;
                                                min-width: 5em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button2.clicked.connect(self.clear)

        self.back = QPushButton('Back',self)
        self.back.setFont(QtGui.QFont('Lucida Fax',11))
        self.back.setToolTip("Go Back")
        self.back.setStyleSheet("""QPushButton  {border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 6px;
                                                border-style: outset;
                                                background: red;
                                                selection-background-color: darkgray;
                                                min-width: 5em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.back.clicked.connect(self.Window2)

        grid.addWidget(self.back,0,1)
        grid.addWidget(self.textboxlbl,1,1)
        grid.addWidget(self.textboxlbl2,2,1)
        grid.addWidget(self.textboxlbl3,3,1)
        grid.addWidget(self.textboxlbl4,4,1)
        grid.addWidget(self.button2,5,1)
        grid.addWidget(self.textbox1,1,2)
        grid.addWidget(self.textbox2,2,2)
        grid.addWidget(self.textbox3,3,2)
        grid.addWidget(self.textbox4,4,2)
        grid.addWidget(self.button,5,2)
        self.setGeometry(self.x,self.y,self.width,self.height)
    @pyqtSlot()
    def clear(self):
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")

    def data(self):
        fname = self.textbox1.text()
        lastname = self.textbox2.text()
        username = self.textbox3.text()
        password = self.textbox4.text()
        self.submitdata(fname, lastname, username, password)
        
    def submitdata(self, fname, lastname, username, password):
        submitting = QMessageBox.question(self, "Submitting Data", "Confirm?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if submitting == QMessageBox.Yes and fname != "" and lastname != "" and username != "" and password != "":
            dataDB = SqliteDict("Ddd.db", autocommit=True)
            reglist = dataDB.get('reg',[])
            listdict = {"fname":fname,"lastname":lastname,"username":username, "password":password}
            reglist.append(listdict)
            dataDB['reg'] = reglist
            print(dataDB['reg'])

            QMessageBox.information(self, "Evaluation", "Registration Complete", QMessageBox.Ok, QMessageBox.Ok)
        
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and fname == "" and lastname == "" and username == "" and password == "":
            pass
        elif submitting == QMessageBox.No and fname == "" or lastname == "" or username == "" or password == "":
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)
    def Window2(self):
        self.w = App()
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
        self.label = QLabel(self)
        self.label.setGeometry(0,0,600,350)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("first.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(200,200,600,350)
        self.textboxlbl = QLabel("<h1>PHYSICS</h1>",self)
        self.textboxlbl.move(255, 30)
        self.textboxlbl.setFont(QtGui.QFont('Lucida Handwriting', 7))
        self.textboxlb2 = QLabel("<h2>Topics</h2>",self)
        self.textboxlb2.move(265, 55)
        self.textboxlb2.setFont(QtGui.QFont('Castellar', 7))
        self.button2 = QPushButton("NEWTON'S FIRST LAW OF MOTION", self)
        self.button2.setToolTip("Calculate the formula")
        self.button2.setStyleSheet("""QPushButton{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 6px;
                                                border-style: outset;
                                                background: pink;
                                                selection-background-color: darkgray;}       
                                                QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button2.move(150,90)
        self.button2.resize(300,30)
        
        self.button3 = QPushButton("NEWTON'S SECOND LAW OF MOTION", self)
        self.button3.setToolTip("Calculate the formula")
        self.button3.setStyleSheet("""QPushButton{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 6px;
                                                border-style: outset;
                                                background: pink;
                                                selection-background-color: darkgray;}       
                                                QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button3.move(150,150)
        self.button3.resize(300,30)
        
        self.button4 = QPushButton("NEWTON'S THIRD LAW OF MOTION", self)
        self.button4.setToolTip("Calculate the formula")
        self.button4.setStyleSheet("""QPushButton{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 6px;
                                                border-style: outset;
                                                background: pink;
                                                selection-background-color: darkgray;}       
                                                QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button4.move(150,210)
        self.button4.resize(300,30)
        
        self.button5 = QPushButton("TORQUE", self)
        self.button5.setToolTip("Calculate the formula")
        self.button5.setStyleSheet("""QPushButton{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 6px;
                                                border-style: outset;
                                                background: pink;
                                                selection-background-color: darkgray;}       
                                                QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button5.move(150,270)
        self.button5.resize(300,30)
        

        self.button2.clicked.connect(self.Window3)
        self.button3.clicked.connect(self.Window4)
        self.button4.clicked.connect(self.Window5)
        self.button5.clicked.connect(self.Window6)

    def Window3(self):                                           
        self.w = Window3()
        self.w.show()
        self.hide()
        
    def Window4(self):                                       
        self.w = Window4()
        self.w.show()
        self.hide()
        
    def Window5(self):                                          
        self.w = Window5()
        self.w.show()
        self.hide()
        
    def Window6(self):                                          
        self.w = Window5()
        self.w.show()
        self.hide()      
        

class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(800,800))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,800)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightpink")
        self.buttonback.move(350,315)
        self.buttonback.clicked.connect(self.Window2)
        
        self.button1 = QPushButton("Formula",self)
        self.button1.setToolTip("View the formula")
        self.button1.setStyleSheet("background-color:lightpink")
        self.button1.move(150,315)
        self.button1.clicked.connect(self.Formula1)
        
        self.textboxlbl = QLabel("<h1>READ!</h1>",self)
        self.textboxlbl.setFont(QtGui.QFont('Times New Roman', 12))
        #self.textboxlbl.setGraphicsEffect(QGraphicsBlurEffect())
        self.textboxlbl.move(250, 10)
        
        self.desc1 = QLabel("<h3>“An object at rest will remain at rest, and an object in </h3>",self)
        self.desc1.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc1.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc1.move(100, 60)
        self.desc1.resize(440,30)
        
        self.desc2 = QLabel("<h3>motion will remain in motion, at constant velocity </h3>",self)
        self.desc2.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc2.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc2.move(100, 90)
        self.desc2.resize(440,30)
        
        self.desc3 = QLabel("<h3>and in a straight line, unless acted upon by a net force.”</h3>",self)
        self.desc3.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc3.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc3.move(100, 120)
        self.desc3.resize(440,30)
        
        self.desc4 = QLabel("<h3>“In the absence of external forces and when viewed </h3>",self)
        self.desc4.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc4.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc4.move(100, 150)
        self.desc4.resize(440,30)
        
        self.desc5 = QLabel("<h3>from an inertial reference frame, an object at rest  </h3>",self)
        self.desc5.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc5.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc5.move(100, 180)
        self.desc5.resize(440,30)
        
        self.desc6 = QLabel("<h3>remains at rest and an object in motion continues in  </h3>",self)
        self.desc6.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc6.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc6.move(100, 210)
        self.desc6.resize(440,30)
        
        self.desc7 = QLabel("<h3>motion with a constant velocity (that is, with a constant  </h3>",self)
        self.desc7.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc7.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc7.move(100, 240)
        self.desc7.resize(440,30)
        
        self.desc7 = QLabel("<h3>speed in a straight line).” </h3>",self)
        self.desc7.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc7.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc7.move(100, 270)
        self.desc7.resize(440,30)
    
    

    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()
    
    def Formula1(self):
        self.w = Formula1()
        self.w.show()
        self.hide()


class Window4(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(800,800))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,800)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightpink")
        self.buttonback.move(350,315)
        self.buttonback.clicked.connect(self.Window2)
        
        self.button1 = QPushButton("Formula",self)
        self.button1.setToolTip("View the formula")
        self.button1.setStyleSheet("background-color:lightpink")
        self.button1.move(150,315)
        self.button1.clicked.connect(self.Formula2)
        
        self.textboxlbl = QLabel("<h1>READ!</h1>",self)
        self.textboxlbl.setFont(QtGui.QFont('Times New Roman', 12))
        #self.textboxlbl.setGraphicsEffect(QGraphicsBlurEffect())
        self.textboxlbl.move(250, 10)
        
        self.desc1 = QLabel("<h3>“Newton’s second law answers the question of </h3> ",self)
        self.desc1.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc1.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc1.move(100, 60)
        self.desc1.resize(440,30)
        
        self.desc2 = QLabel("<h3>forces acting on it.”  </h3>",self)
        self.desc2.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc2.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc2.move(100, 90)
        self.desc2.resize(440,30)
        
        self.desc3 = QLabel("<h3>“When viewed from an inertial reference frame, </h3>",self)
        self.desc3.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc3.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc3.move(100, 120)
        self.desc3.resize(440,30)
        
        self.desc4 = QLabel("<h3>the acceleration of an object is directly proportional</h3>",self)
        self.desc4.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc4.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc4.move(100, 150)
        self.desc4.resize(440,30)
        
        self.desc5 = QLabel("<h3>to the net force acting on it and inversely  </h3>",self)
        self.desc5.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc5.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc5.move(100, 180)
        self.desc5.resize(440,30)
        
        self.desc6 = QLabel("<h3>proportional to its mass.” </h3>",self)
        self.desc6.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc6.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc6.move(100, 210)
        self.desc6.resize(440,30)
    
    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()
        
    def Formula2(self):
        self.w = Formula2()
        self.w.show()
        self.hide()
    
class Window5(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(800,800))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,800)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightpink")
        self.buttonback.move(350,315)
        self.buttonback.clicked.connect(self.Window2)
        
        self.button1 = QPushButton("Formula",self)
        self.button1.setToolTip("View the formula")
        self.button1.setStyleSheet("background-color:lightpink")
        self.button1.move(150,315)
        self.button1.clicked.connect(self.Formula3)
        
        self.textboxlbl = QLabel("<h1>READ!</h1>",self)
        self.textboxlbl.setFont(QtGui.QFont('Times New Roman', 12))
        #self.textboxlbl.setGraphicsEffect(QGraphicsBlurEffect())
        self.textboxlbl.move(250, 10)
        
        self.desc1 = QLabel("<h3>“If two objects interact, the force exerted by object 1 </h3>",self)
        self.desc1.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc1.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc1.move(100, 60)
        self.desc1.resize(440,30)
        
        self.desc2 = QLabel("<h3>on object 2 is equal in magnitude and opposite  </h3>",self)
        self.desc2.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc2.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc2.move(100, 90)
        self.desc2.resize(440,30)
        
        self.desc3 = QLabel("<h3>in direction to the force exerted by object 2 on object 1.”</h3>",self)
        self.desc3.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc3.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc3.move(100, 120)
        self.desc3.resize(440,30)
        
        self.desc4 = QLabel("<h3>“The force that object 1 exerts on object 2 is popularly  </h3>",self)
        self.desc4.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc4.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc4.move(100, 150)
        self.desc4.resize(440,30)
        
        self.desc5 = QLabel("<h3> called the action force, and the force of object 2 on </h3>",self)
        self.desc5.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc5.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc5.move(100, 180)
        self.desc5.resize(440,30)
        
        self.desc6 = QLabel("<h3>object 1 is called the reaction force. “</h3>",self)
        self.desc6.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc6.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc6.move(100, 210)
        self.desc6.resize(440,30)

    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()
    
    def Formula3(self):
        self.w = Formula3()
        self.w.show()
        self.hide()
    
class Window6(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(800,800))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,800)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightpink")
        self.buttonback.move(350,315)
        self.buttonback.clicked.connect(self.Window2)
        
        self.button1 = QPushButton("Formula",self)
        self.button1.setToolTip("View the formula")
        self.button1.setStyleSheet("background-color:lightpink")
        self.button1.move(150,315)
        self.button1.clicked.connect(self.Formula4)
        
        self.textboxlbl = QLabel("<h1>READ!</h1>",self)
        self.textboxlbl.setFont(QtGui.QFont('Times New Roman', 12))
        #self.textboxlbl.setGraphicsEffect(QGraphicsBlurEffect())
        self.textboxlbl.move(250, 10)
        
        self.desc1 = QLabel("<h3>“Torque is the tendency of a force to rotate an object </h3>",self)
        self.desc1.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc1.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc1.move(100, 60)
        self.desc1.resize(440,30)
        
        self.desc2 = QLabel("<h3>about an axis, fulcrum, or pivot. Just as a force is a</h3>",self)
        self.desc2.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc2.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc2.move(100, 90)
        self.desc2.resize(440,30)
        
        self.desc3 = QLabel("<h3>push or a pull, a torque can be thought of as a twist.”</h3>",self)
        self.desc3.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc3.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc3.move(100, 120)
        self.desc3.resize(440,30)
        
        self.desc4 = QLabel("<h3>“It is a measure of the turning force on an object such </h3>",self)
        self.desc4.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc4.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc4.move(100, 150)
        self.desc4.resize(440,30)
        
        self.desc5 = QLabel("<h3>as a bolt or a flywheel. It is an influence which tends  </h3>",self)
        self.desc5.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc5.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc5.move(100, 180)
        self.desc5.resize(440,30)
        
        self.desc6 = QLabel("<h3>to change the rotational motion of an object.“</h3>",self)
        self.desc6.setFont(QtGui.QFont('Bradley Hand ITC', 10))
        self.desc6.setStyleSheet("""QLabel{ background: lightblue;}""")
        self.desc6.move(100, 210)
        self.desc6.resize(440,30)

    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()
    
    def Formula4(self):
        self.w = Formula4()
        self.w.show()
        self.hide()
       
class Formula1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(800,800))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,800)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightblue")
        self.buttonback.move(350,300)
        self.buttonback.clicked.connect(self.Window2)
        
    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()
    
class Formula2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(800,800))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,800)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightblue")
        self.buttonback.move(350,300)
        self.buttonback.clicked.connect(self.Window2)
        
    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()
        
class Formula3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(800,800))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,800)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightblue")
        self.buttonback.move(350,300)
        self.buttonback.clicked.connect(self.Window2)
        
    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()        
        
        
class Formula4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(800,800))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,800)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(200,200,600,350)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.setStyleSheet("background-color:lightblue")
        self.buttonback.move(350,300)
        self.buttonback.clicked.connect(self.Window2)
        
    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
