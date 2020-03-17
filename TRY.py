import sys
import sqlite3
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QPixmap, QFont, QIntValidator, QDoubleValidator
from PyQt5.QtCore import pyqtSlot, QSize

class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.title = "PHYSICS"
        self.x=540 
        self.y=300
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
        self.label.setGeometry(10,20,285,100)
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
                                                QPushButton:hover{background-color: black;
                                                                    color: rgb(203, 177, 242);
                                                                    border: 2px rgb(203, 177, 242)}
                                                QPushButton:pressed{background-color: black;
                                                color: rgb(203, 177, 242);
                                                border-style: inset}""")
        self.button.setToolTip("Click to Login!")
        self.button.clicked.connect(self.data)
        self.password.returnPressed.connect(self.button.click)
        
        self.register = QPushButton('Register',self)
        self.register.setFont(QtGui.QFont('Lucida Fax',11))
        self.register.setStyleSheet("""QPushButton{border: 2px solid gray;
                                                border-radius: 10px;
                                                border-width: 2px;
                                                border-style: outset;
                                                background: rgb(203, 177, 242);
                                                selection-background-color: darkgray;
                                                padding: 6px;
                                                }QPushButton:hover{background-color: black;
                                                                    color: rgb(203, 177, 242);
                                                                    border: 2px rgb(203, 177, 242)}
                                                QPushButton:pressed{background-color: black;
                                                color: rgb(203, 177, 242);
                                                border-style: inset}""")
        self.register.setToolTip("Click to Login!")
        self.register.clicked.connect(self.registerWin)
        self.layout.addWidget(self.register,3,1)
        self.layout.addWidget(self.textboxlbl,1,1)
        self.layout.addWidget(self.textbox,1,2)
        self.layout.addWidget(self.textboxlbl2,2,1)
        self.layout.addWidget(self.password,2,2)
        self.layout.addWidget(self.button,3,2)

    @pyqtSlot()
    def data(self):
        username = self.textbox.text()
        password = self.password.text()
        self.submitdata(username, password)
    
    def submitdata(self,username, password):
        submitting = QMessageBox.question(self, "Submitting Data", "Confirm?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if submitting == QMessageBox.Yes and username != "" and password != "":
            conn = sqlite3.connect('names.db')
            c = conn.cursor()
            def get_emps_by_name(username,password):
                c.execute("SELECT * FROM students WHERE username=:user AND password = :passw", {'user': username, 'passw':password})
                return c.fetchall()
            self.emp_1 = StudentLog(username, password)
            emps = get_emps_by_name(username,password)
            if emps == []:
                QMessageBox.warning(self, "Error","Input not found", QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, "Congratulations","Login successful", QMessageBox.Ok)
                self.Window2()
     
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and username == "" and password == "":
            pass
        elif submitting == QMessageBox.Yes or username == "" or password == "":
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)
        
    def registerWin(self):
        self.w = registerWin()
        self.w.show()
        self.hide()

    def Window2(self):                                             
        self.w = Window2()
        self.w.show()
        self.hide()

class Student:
    def __init__(self, first, last, user, passw):
        self.first = first
        self.last = last
        self.user = user
        self.passw = passw
        
class StudentLog:
    def __init__(self,user, passw):
        self.user = user
        self.passw = passw

class registerWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        self.title = "Registration"
        self.x=540
        self.y=300
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
                                                min-width: 5em;
                                                }QPushButton:hover{background-color: black;
                                                                    color: rgb(203, 177, 242);
                                                                    border: 2px rgb(203, 177, 242)}
                                                QPushButton:pressed{background-color: black;
                                                color: rgb(203, 177, 242);
                                                border-style: inset}""")
        self.button.clicked.connect(self.data) 
        self.textbox4.returnPressed.connect(self.button.click)

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
                                                }QPushButton:hover{background-color: black;
                                                                    color: rgb(203, 177, 242);
                                                                    border: 2px rgb(203, 177, 242)}
                                                QPushButton:pressed{background-color: black;
                                                color: rgb(203, 177, 242);
                                                border-style: inset}""")
        self.button2.clicked.connect(self.clear)

        self.back = QPushButton('Back',self)
        self.back.setFont(QtGui.QFont('Lucida Fax',11))
        self.back.setToolTip("Go Back")
        self.back.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 10px;
                                                padding: 6px;
                                                border-style: outset;
                                                background: rgb(203, 177, 242);
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
            conn = sqlite3.connect('names.db')
            c = conn.cursor()
            def get_emps_by_name(lastname,username):
                c.execute("SELECT * FROM students WHERE last=:last AND username = :user", {'last': lastname, 'user': username})
                return c.fetchall()
            def insert_emp(emp):
                with conn:
                    c.execute("INSERT INTO students VALUES (:first, :last, :user, :passw)", {'first': emp.first, 'last': emp.last, 'user': emp.user, 'passw':emp.passw})
            self.emp_1 = Student(fname, lastname, username, password)
            insert_emp(self.emp_1)
            emps = get_emps_by_name(lastname,username)
            print(emps)

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
        self.setGeometry(400,220,600,350)
        self.textboxlbl = QLabel("<h1>PHYSICS</h1>",self)
        self.textboxlbl.move(255, 30)
        self.textboxlbl.setFont(QtGui.QFont('Lucida Handwriting', 7))
        self.textboxlb2 = QLabel("<h2>Topics</h2>",self)
        self.textboxlb2.move(265, 55)
        self.textboxlb2.setFont(QtGui.QFont('Castellar', 7))
        self.button2 = QPushButton("NEWTON'S FIRST LAW OF MOTION", self)
        self.button2.setToolTip("View the first law of motion")
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
        self.button3.setToolTip("View the second law of motion")
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
        self.button4.setToolTip("View the third law of motion")
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
        self.button5.setToolTip("View the torque")
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
        self.w = Window6()
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
        self.setGeometry(400,220,600,350)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(5,5)
        self.buttonback.setFont(QtGui.QFont('Lucida Fax',11))
        self.buttonback.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.buttonback.resize(53,35)
        self.buttonback.clicked.connect(self.Window2)
        
        self.button1 = QPushButton("Formula",self)
        self.button1.setToolTip("View the formula")
        self.button1.setFont(QtGui.QFont('Lucida Fax',11))
        self.button1.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;}
                                                QPushButton:hover{border: 2px lightblue;
                                                                    background-color: green;
                                                                    color: lightblue;}
                                                QPushButton:pressed{background-color: green;
                                                color: lightblue;
                                                border-style: inset}""")
        self.button1.resize(80,35)
        self.button1.move(260,310)
        self.button1.clicked.connect(self.Formula1)
        
        self.textboxlbl = QLabel("READ!",self)
        self.textboxlbl.setFont(QtGui.QFont('Times New Roman', 18))
        self.textboxlbl.setStyleSheet("""QLabel  {color: white;
                                                border: 2px black;
                                                border-radius: 5px;
                                                padding: 2px;
                                                border-style: outset;
                                                background: black;
                                                selection-background-color: darkgray;}""")
        self.textboxlbl.move(250, 10)
        self.textboxlbl.setGeometry(250,5,90,40)
    
        self.desc1 = QPlainTextEdit("   An object at rest will remain at rest, and an object in \nmotion will remain in motion, at constant velocity and \nin a straight line, unless acted upon by a net force.\n\n    In the absence of external forces and when viewed \nfrom an inertial reference frame, an object at rest\nremains at rest and an object in motion continues in\nmotion with a constant velocity \n(that is, with a constant speed in a straight line).",self)
        self.desc1.setFont(QtGui.QFont('Lucida Fax',11))
        self.desc1.setReadOnly(True)
        self.desc1.setStyleSheet("""QPlainTextEdit{color: black;
                                                border: 3px black;
                                                border-radius: 30px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;}""")
        self.desc1.move(50, 60)
        self.desc1.setGeometry(80,50,450,230)

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
        self.setGeometry(400,220,600,350)
        self.setWindowTitle("NEWTON'S SECOND LAW")
        
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(5,5)
        self.buttonback.setFont(QtGui.QFont('Lucida Fax',11))
        self.buttonback.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.buttonback.resize(53,35)
        self.buttonback.clicked.connect(self.Window2)
        
        self.button1 = QPushButton("Formula",self)
        self.button1.setToolTip("View the formula")
        self.button1.setFont(QtGui.QFont('Lucida Fax',11))
        self.button1.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;}
                                                QPushButton:hover{border: 2px lightblue;
                                                                    background-color: green;
                                                                    color: lightblue;}
                                                QPushButton:pressed{background-color: green;
                                                color: lightblue;
                                                border-style: inset}""")
        self.button1.resize(80,35)
        self.button1.move(260,310)
        self.button1.clicked.connect(self.Formula2)
        
        self.textboxlbl = QLabel("<h1>READ!</h1>",self)
        self.textboxlbl.setFont(QtGui.QFont('Times New Roman', 12))
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
        self.setGeometry(400,220,600,350)
        self.setWindowTitle("NEWTON'S THIRD LAW")
        
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(5,5)
        self.buttonback.setFont(QtGui.QFont('Lucida Fax',11))
        self.buttonback.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.buttonback.resize(53,35)
        self.buttonback.clicked.connect(self.Window2)
        
        self.button1 = QPushButton("Formula",self)
        self.button1.setToolTip("View the formula")
        self.button1.setFont(QtGui.QFont('Lucida Fax',11))
        self.button1.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;}
                                                QPushButton:hover{border: 2px lightblue;
                                                                    background-color: green;
                                                                    color: lightblue;}
                                                QPushButton:pressed{background-color: green;
                                                color: lightblue;
                                                border-style: inset}""")
        self.button1.resize(80,35)
        self.button1.move(260,310)
        self.button1.clicked.connect(self.Formula3)
        
        self.textboxlbl = QLabel("<h1>READ!</h1>",self)
        self.textboxlbl.setFont(QtGui.QFont('Times New Roman', 12))
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
        self.setGeometry(400,220,600,350)
        self.setWindowTitle("TORQUE")
        
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(5,5)
        self.buttonback.setFont(QtGui.QFont('Lucida Fax',11))
        self.buttonback.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.buttonback.resize(53,35)
        self.buttonback.clicked.connect(self.Window2)
        
        self.button1 = QPushButton("Formula",self)
        self.button1.setToolTip("View the formula")
        self.button1.setFont(QtGui.QFont('Lucida Fax',11))
        self.button1.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;}
                                                QPushButton:hover{border: 2px lightblue;
                                                                    background-color: green;
                                                                    color: lightblue;}
                                                QPushButton:pressed{background-color: green;
                                                color: lightblue;
                                                border-style: inset}""")
        self.button1.resize(80,35)
        self.button1.move(260,310)
        self.button1.clicked.connect(self.Formula4)
        
        self.textboxlbl = QLabel("<h1>READ!</h1>",self)
        self.textboxlbl.setFont(QtGui.QFont('Times New Roman', 12))
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
        self.label.setGeometry(95,265,450,100)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(400,190,600,420)
        self.setWindowTitle("NEWTON'S FIRST LAW")

        self.image1 = QLabel(self)
        pic = QPixmap("image.png")
        self.image1.setPixmap(pic)
        self.image1.move(180,0)
        self.image1.resize(300,300)
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(5,5)
        self.buttonback.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.buttonback.resize(50,30)
        self.buttonback.clicked.connect(self.Window2)
        self.textboxlb3 = QLabel("Enter Mass:",self)
        self.textboxlb3.move(130,270)
        self.textboxlb3.setFont(QtGui.QFont('Lucida Fax',11))
        self.textboxlb4 = QLabel("Weight:",self)
        self.textboxlb4.move(150,300)
        self.textboxlb4.setFont(QtGui.QFont('Lucida Fax',11))

        self.textbox6 = QLineEdit(self)
        self.textbox6.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox6.setValidator(QDoubleValidator(self))
        self.textbox6.move(220, 270)
        self.textbox6.resize(200,30)
        self.textbox6.setText("0")
        self.textbox6.setToolTip("Enter Mass")
        self.textbox6.setFont(QtGui.QFont('Lucida Fax',11))

        self.textbox7 = QLineEdit(self)
        self.textbox7.setReadOnly(True)
        self.textbox7.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox7.move(220, 300)
        self.textbox7.resize(200,30)
        self.textbox7.setToolTip("Weight")
        self.textbox7.setFont(QtGui.QFont('Lucida Fax',11))

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button.resize(80,30)
        self.button.setToolTip("Submit your info")
        self.button.move(280,345) # button.move(x,y)
        self.button.clicked.connect(self.prof) 
        self.textbox6.returnPressed.connect(self.button.click)

    @pyqtSlot()
    def prof(self):
        num = float(self.textbox6.text())
        
        self.Submit(num)
    
    def Submit(self,num):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and num != "":
            grav= 9.8
            weight = num*grav
            weight2 = float("{0:.2f}".format(weight))
            self.textbox7.setText(f"{weight2}")
        
        
        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and num == "":
            QMessageBox.warning(self, "Error","Please Input Mass", QMessageBox.Ok, QMessageBox.Ok)
        else:
           QMessageBox.warning(self, "Error","Please Input an Integer", QMessageBox.Ok, QMessageBox.Ok)
        
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
        self.label.setGeometry(50,245,520,180)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)

        self.image1 = QLabel(self)
        self.image1.setGeometry(55,5,250,250)
        pic = QPixmap("image1.png")
        self.image1.setPixmap(pic)
        self.image1.setStyleSheet("""QLabel{border: 3px solid gray;
                                                border-radius: 5px;
                                                padding:0px}""")

        self.image2 = QLabel(self)
        self.image2.setGeometry(300,5,250,250)
        pic = QPixmap("Document 7_1.png")
        self.image2.setPixmap(pic)
        self.image2.setStyleSheet("""QLabel{border: 3px solid gray;
                                                border-radius: 5px;
                                                padding:0px}""")

        self.setGeometry(400,190,600,440)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(3,5)
        self.buttonback.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.buttonback.resize(50,30)
        self.buttonback.clicked.connect(self.Window2)
        self.textboxlb3 = QLabel("Enter Mass:",self)
        self.textboxlb3.move(55,250)
        self.textboxlb3.setStyleSheet("font-weight: bold;")
        self.textboxlb3.setFont(QtGui.QFont('Lucida Fax',11))

        self.textboxlb4 = QLabel("Acceleration(X):",self)
        self.textboxlb4.setGeometry(55,300,150,30)
        self.textboxlb4.setStyleSheet("font-weight: bold;")
        self.textboxlb4.setFont(QtGui.QFont('Lucida Fax',11))

        self.textboxlb5 = QLabel("Acceleration(Y):",self)
        self.textboxlb5.setGeometry(55,350,150,30)
        self.textboxlb5.move(55,350)
        self.textboxlb5.setStyleSheet("font-weight: bold;")
        self.textboxlb5.setFont(QtGui.QFont('Lucida Fax',11))

        self.textboxlb6 = QLabel("Fx:",self)
        self.textboxlb6.move(230,250)
        self.textboxlb6.setStyleSheet("font-weight: bold;")
        self.textboxlb6.setFont(QtGui.QFont('Lucida Fax',11))

        self.textboxlb7 = QLabel("Fy:",self)
        self.textboxlb7.move(230,300)
        self.textboxlb7.setStyleSheet("font-weight: bold;")
        self.textboxlb7.setFont(QtGui.QFont('Lucida Fax',11))

        self.textboxlb8 = QLabel("Fnet:",self)
        self.textboxlb8.move(230,350)
        self.textboxlb8.setStyleSheet("font-weight: bold;")
        self.textboxlb8.setFont(QtGui.QFont('Lucida Fax',11))

        self.textboxlb9 = QLabel("Direction:",self)
        self.textboxlb9.move(405,250)
        self.textboxlb9.setStyleSheet("font-weight: bold;")
        self.textboxlb9.setFont(QtGui.QFont('Lucida Fax',11))

        self.textbox6 = QLineEdit(self)
        self.textbox6.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox6.setValidator(QDoubleValidator(self))
        self.textbox6.move(55, 275)
        self.textbox6.resize(150,30)
        self.textbox6.setText("0")
        self.textbox6.setToolTip("Enter Mass")
        self.textbox6.setFont(QtGui.QFont('Lucida Fax',11))

        self.ax = QLineEdit(self)
        self.ax.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.ax.setValidator(QDoubleValidator(self))
        self.ax.move(55, 325)
        self.ax.resize(150,30)
        self.ax.setText("0")
        self.ax.setToolTip("Enter acceleration for x")
        self.ax.setFont(QtGui.QFont('Lucida Fax',11))
        
        self.ay = QLineEdit(self)
        self.ay.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.ay.setValidator(QDoubleValidator(self))
        self.ay.move(55, 375)
        self.ay.resize(150,30)
        self.ay.setText("0")
        self.ay.setToolTip("Enter acceleration for y")
        self.ay.setFont(QtGui.QFont('Lucida Fax',11))

        self.textbox7 = QLineEdit(self)
        self.textbox7.setReadOnly(True)
        self.textbox7.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox7.move(230, 275)
        self.textbox7.resize(150,30)
        self.textbox7.setToolTip("Fx")
        self.textbox7.setFont(QtGui.QFont('Lucida Fax',11))

        self.textbox8 = QLineEdit(self)
        self.textbox8.setReadOnly(True)
        self.textbox8.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox8.move(230, 325)
        self.textbox8.resize(150,30)
        self.textbox8.setToolTip("Fy")
        self.textbox8.setFont(QtGui.QFont('Lucida Fax',11))
        
        self.textbox9 = QLineEdit(self)
        self.textbox9.setReadOnly(True)
        self.textbox9.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox9.move(230, 375)
        self.textbox9.resize(150,30)
        self.textbox9.setToolTip("F Magnitude")
        self.textbox9.setFont(QtGui.QFont('Lucida Fax',11))

        self.textbox10 = QLineEdit(self)
        self.textbox10.setReadOnly(True)
        self.textbox10.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox10.move(405, 275)
        self.textbox10.resize(150,30)
        self.textbox10.setToolTip("Direction")
        self.textbox10.setFont(QtGui.QFont('Lucida Fax',11))

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button.resize(80,30)
        self.button.setToolTip("Submit your info")
        self.button.move(445,325) # button.move(x,y)
        self.button.clicked.connect(self.prof) 
        self.ax.returnPressed.connect(self.button.click)
        self.ay.returnPressed.connect(self.button.click)

    @pyqtSlot()
    def prof(self):
        mass = float(self.textbox6.text())
        acx = float(self.ax.text())
        acy = float(self.ay.text())
        
        self.Submit(mass,acx,acy)
    
    def Submit(self,mass,acx,acy):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and mass != "" and acx != "" and acy != "":
            fnetx = mass*acx
            fnetx2 = float("{0:.2f}".format(fnetx))
            fnety = mass*acy
            fnety2 = float("{0:.2f}".format(fnety))
            fnet = ((fnetx2)**2+(fnety2)**2)**0.5
            fnet2 = float("{0:.2f}".format(fnet))
            if acy == 0 or acx == 0:
                angle3 = 0
            else:
                angle = np.arctan(fnety2/fnetx2)
                pi = float("{0:.9f}".format(np.pi))
                angle2 = angle*(180/pi)
                angle3 = float("{0:.2f}".format(angle2))
            self.textbox7.setText(f"x({fnetx2})")
            self.textbox8.setText(f"y({fnety2})")
            self.textbox9.setText(f"{fnet2}")
            self.textbox10.setText(f"{angle3}")

        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and mass != "" and acx != "" and acy != "":
            QMessageBox.warning(self, "Error","Please Input Mass", QMessageBox.Ok, QMessageBox.Ok)
        else:
           QMessageBox.warning(self, "Error","Please Input an Integer", QMessageBox.Ok, QMessageBox.Ok)
        
        
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
        self.buttonback.move(5,5)
        self.buttonback.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.buttonback.resize(50,30)
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
        self.setGeometry(400,190,600,420)
        self.setWindowTitle("NEWTON'S FIRST LAW")
        self.image1 = QLabel(self)
        self.image1.setGeometry(180,15,250,250)
        pic = QPixmap("torque.jpg")
        self.image1.setPixmap(pic)
        self.image1.setStyleSheet("""QLabel{border: 3px solid gray;
                                                border-radius: 5px;
                                                padding:0px}""")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(5,5)
        self.buttonback.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.buttonback.resize(50,30)
        self.buttonback.clicked.connect(self.Window2)
        #self.textboxlb3 = QLabel("Enter Mass:",self)
        #self.textboxlb3.move(130,270)
        #self.textboxlb3.setFont(QtGui.QFont('Lucida Fax',11))
        #self.textboxlb4 = QLabel("Weight:",self)
        #self.textboxlb4.move(150,300)
        #self.textboxlb4.setFont(QtGui.QFont('Lucida Fax',11))

        self.force = QLineEdit(self)
        self.force.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.force.setValidator(QDoubleValidator(self))
        self.force.move(55, 275)
        self.force.resize(150,30)
        self.force.setText("0")
        self.force.setToolTip("Enter Force")
        self.force.setFont(QtGui.QFont('Lucida Fax',11))

        self.radius = QLineEdit(self)
        self.radius.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.radius.setValidator(QDoubleValidator(self))
        self.radius.move(55, 325)
        self.radius.resize(150,30)
        self.radius.setText("0")
        self.radius.setToolTip("Enter Radius")
        self.radius.setFont(QtGui.QFont('Lucida Fax',11))
    
        self.angx = QLineEdit(self)
        self.angx.setValidator(QDoubleValidator(self))
        self.angx.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.angx.move(230, 275)
        self.angx.resize(150,30)
        self.angx.setText("0")
        self.angx.setToolTip("Angle(cosine)")
        self.angx.setFont(QtGui.QFont('Lucida Fax',11))

        self.angy = QLineEdit(self)
        self.angy.setValidator(QDoubleValidator(self))
        self.angy.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.angy.move(230, 325)
        self.angy.resize(150,30)
        self.angy.setText("0")
        self.angy.setToolTip("Angle(sin)")
        self.angy.setFont(QtGui.QFont('Lucida Fax',11))

        self.textbox10 = QLineEdit(self)
        self.textbox10.setReadOnly(True)
        self.textbox10.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox10.move(405, 275)
        self.textbox10.resize(150,30)
        self.textbox10.setToolTip("Torque")
        self.textbox10.setFont(QtGui.QFont('Lucida Fax',11))

        self.button = QPushButton('Submit', self)
        self.button.setStyleSheet("""QPushButton  {color: green;
                                                border: 2px green;
                                                border-radius: 5px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;
                                                min-width: 1em;
                                                }QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button.resize(80,30)
        self.button.setToolTip("Submit your info")
        self.button.move(280,345) # button.move(x,y)
        self.button.clicked.connect(self.prof) 

    @pyqtSlot()
    def prof(self):
        force = float(self.force.text())
        dis = float(self.radius.text())
        ax = float(self.angx.text())
        ay = float(self.angy.text())
        self.Submit(force,dis,ax,ay)
    
    def Submit(self,force,dis,ax,ay):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and force != "" and dis != "":
            torque = force*dis
            torque2 = float("{0:.2f}".format(torque))
            self.textbox10.setText(f"{torque2}")
        
        
        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and num == "":
            QMessageBox.warning(self, "Error","Please Input Mass", QMessageBox.Ok, QMessageBox.Ok)
        else:
           QMessageBox.warning(self, "Error","Please Input an Integer", QMessageBox.Ok, QMessageBox.Ok)
        
    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
