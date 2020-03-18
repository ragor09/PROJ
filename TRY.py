import sys
import sqlite3
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QPixmap, QFont, QIntValidator, QDoubleValidator, QLinearGradient
from PyQt5.QtCore import pyqtSlot, QSize

class App(QMainWindow):
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
        self.register.setToolTip("Click to Register")
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
        elif submitting == QMessageBox.Yes and username == "" and password != "":
            QMessageBox.warning(self, "Error","Please input username", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and password == "" and username != "":
            QMessageBox.warning(self, "Error","Please input password", QMessageBox.Ok, QMessageBox.Ok)
        else:
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

class registerWin(QMainWindow):
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
        elif submitting == QMessageBox.Yes and fname == "" and lastname != "" and username != "" and password != "":
            QMessageBox.warning(self, "Error","Please enter your first name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and fname != "" and lastname == "" and username != "" and password != "":
            QMessageBox.warning(self, "Error","Please enter your last name", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and fname != "" and lastname != "" and username == "" and password != "":
            QMessageBox.warning(self, "Error","Please enter username", QMessageBox.Ok, QMessageBox.Ok)
        elif submitting == QMessageBox.Yes and fname != "" and lastname != "" and username != "" and password == "":
            QMessageBox.warning(self, "Error","Please enter password", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)

    def Window2(self):
        self.w = App()
        self.w.show()
        self.hide()
        
        
class Window2(QWidget):                         
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
        
        self.button4 = QPushButton("WORK, POWER AND ENERGY", self)
        self.button4.setToolTip("View work, power and energy")
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
        
        self.button5 = QPushButton("FLUID DYNAMICS", self)
        self.button5.setToolTip("View fluid dynamics")
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
        self.show()

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
        
        self.textboxlbl = QLabel("LAW OF INERTIA",self)
        self.textboxlbl.setFont(QtGui.QFont('Times New Roman', 18))
        self.textboxlbl.setStyleSheet("""QLabel  {color: black;
                                                border: 2px black;
                                                border-radius: 5px;
                                                padding: 2px;
                                                border-style: outset;
                                                background: rgb(203, 177, 242);
                                                selection-background-color: darkgray;}""")
        self.textboxlbl.move(250, 10)
        self.textboxlbl.setGeometry(195,5,210,40)
    
        self.desc1 = QPlainTextEdit("\n    An object at rest will remain at rest, and an object in \nmotion will remain in motion, at constant velocity and \nin a straight line, unless acted upon by a net force.\n\n    In the absence of external forces and when viewed \nfrom an inertial reference frame, an object at rest\nremains at rest and an object in motion continues in\nmotion with a constant velocity \n(that is, with a constant speed in a straight line).",self)
        self.desc1.setFont(QtGui.QFont('Lucida Fax',11))
        self.desc1.setReadOnly(True)
        self.desc1.setStyleSheet("""QPlainTextEdit{color: black;
                                                border: 3px black;
                                                border-radius: 30px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 darkGray, stop:1 rgba(98, 211, 162, 255));
                                                selection-background-color: green;}""")
        self.desc1.move(50, 60)
        self.desc1.setGeometry(80,50,450,235)

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
        self.button1.clicked.connect(self.Formula2)
        
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
    
        self.desc1 = QPlainTextEdit("LAW OF ACCELERATION\n    Newton's second law of motion answers the question of what happennds to an object that has one or more forces acting on it.\n    When viewed from an inertia; reference frame, the acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass.",self)
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
        self.setGeometry(400,190,600,420)
        self.setWindowTitle("WORK, POWER, ENERGY")
        self.image1 = QLabel(self)
        self.image1.setGeometry(305,15,250,250)
        image1 = QPixmap("density.png")
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
        self.buttonback.resize(80,30)
        
        self.button1 = QPushButton("WORK",self)
        self.button1.setToolTip("Go back to topics")
        self.button1.move(15,360)
        self.button1.setStyleSheet("""QPushButton  {color: green;
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
        self.button1.resize(150,30)
        
        self.button2 = QPushButton("POWER",self)
        self.button2.setToolTip("Go back to topics")
        self.button2.move(210,360)
        self.button2.setStyleSheet("""QPushButton  {color: green;
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
        self.button2.resize(150,30)
        
        self.button3 = QPushButton("ENERGY",self)
        self.button3.setToolTip("Go back to topics")
        self.button3.move(405,360)
        self.button3.setStyleSheet("""QPushButton  {color: green;
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
        self.button3.resize(150,30)
        
        self.desc1 = QPlainTextEdit("    WORK is the amount of energy transferred by a force acting through a distance.\n    The French mathematician Gaspard-Gustave Coriolis first coied the term work in 1826.\n    Work is zero, when F is perpendicular to delta r.\n    Work is positive, when F and delta r are in the same direction.\n    Work is negative, when F and delta r are in the opposite direction.",self)
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
        self.desc1.setGeometry(15,50,180,300)
        
        
        self.desc2 = QPlainTextEdit("    POWER measures the rate of work done.\n     It also rate at which energy expended.\n    Power is the amount of work done, divided by the time it takes to do it.\n    Where: P = W/t\n\t P = Power in Watt\n\t W = Work in Joules\n\t t = time in seconds\n\t    Since work performed equals energy expended, The watt is defined as the expenditure of 1 joule in 1 second.",self)
        self.desc2.setFont(QtGui.QFont('Lucida Fax',11))
        self.desc2.setReadOnly(True)
        self.desc2.setStyleSheet("""QPlainTextEdit{color: black;
                                                border: 3px black;
                                                border-radius: 30px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;}""")
        self.desc2.move(50, 60)
        self.desc2.setGeometry(210,50,180,300)
        
        self.desc3 = QPlainTextEdit("    ENERGY is the ability to do work. It is a combination of energy and matter make up the universe: Matter is substance, and energy is the mover of substance.\n    THE LAW OF CONSERVATION OF ENERGY\n    Energy cannot be created or destroyed; it may be transformed from one from into another, but the total amout of energy never changes.",self)
        self.desc3.setFont(QtGui.QFont('Lucida Fax',11))
        self.desc3.setReadOnly(True)
        self.desc3.setStyleSheet("""QPlainTextEdit{color: black;
                                                border: 3px black;
                                                border-radius: 30px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;}""")
        self.desc3.move(50, 60)
        self.desc3.setGeometry(405,50,180,300)
        
        self.buttonback.clicked.connect(self.Window2)
        self.button1.clicked.connect(self.Work)
        self.button2.clicked.connect(self.Power)
        self.button3.clicked.connect(self.Energy)
        
    def Window2(self):                                          
        self.w = Window2()
        self.w.show()
        self.hide()
        
    def Work(self):                                          
        self.w = Work()
        self.w.show()
        self.hide()

    def Power(self):                                          
        self.w = Power()
        self.w.show()
        self.hide()

    def Energy(self):                                          
        self.w = Energy()
        self.w.show()
        self.hide()



  
class Window6(QMainWindow):
    
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
  

        self.desc1 = QPlainTextEdit("    FLUID is a collection of molecules that are randomly arranged and held together by weak cohesive forces exerted by the walls of the container.\n\n    It is also a matter that flows under pressure, which includes liquids, gases, and even plasmas. Water, air, sun and even molasses are fluid.\n\n    FLUID DYNAMICS is the study of fluids in motion.",self)
        self.desc1.setFont(QtGui.QFont('Lucida Fax',11))
        self.desc1.setReadOnly(True)
        self.desc1.setStyleSheet("""QPlainTextEdit{color: black;
                                                border: 3px black;
                                                border-radius: 30px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: lightblue;
                                                selection-background-color: darkgray;}""")
        self.desc1.move(50, 5)
        self.desc1.setGeometry(80,5,450,200)
        
        self.button3 = QPushButton("D  E  N  S  I  T  Y", self)
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
        self.button3.move(150,240)
        self.button3.resize(300,30)
        
        
        self.button4 = QPushButton("P  R  E  S  S  U  R  E", self)
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
        self.button4.move(150,270)
        self.button4.resize(300,30)
        
        self.button5 = QPushButton("TORRICELLI'S PRINCIPLE", self)
        self.button5.setToolTip("View fluid dynamics")
        self.button5.setStyleSheet("""QPushButton{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 6px;
                                                border-style: outset;
                                                background: pink;
                                                selection-background-color: darkgray;}       
                                                QPushButton:hover{background-color: rgb(209, 200, 36)}
                                                QPushButton:pressed{background-color: rgb(0, 224, 157);
                                                border-style: inset}""")
        self.button5.move(150,300)
        self.button5.resize(300,30)
    
        self.button3.clicked.connect(self.Fdensity)
        self.button4.clicked.connect(self.Fpressure)
        self.button5.clicked.connect(self.Ftorri)
        self.buttonback.clicked.connect(self.Window2)

        self.show()

    def Fdensity(self):                                           
        self.w = Fdensity()
        self.w.show()
        self.hide()
        
    def Fpressure(self):                                       
        self.w = Fpressure()
        self.w.show()
        self.hide()
        
    def Ftorri(self):                                          
        self.w = Ftorri()
        self.w.show()
        self.hide()
        
    def Window2(self):                                          
        self.w = Window2()
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
        self.setWindowTitle("NEWTON'S SECOND LAW")
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
        
        
class Fdensity(QMainWindow):
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
        self.image1.setGeometry(305,15,250,250)
        image1 = QPixmap("density.png")
        self.image1.setStyleSheet("""QLabel{border: 3px solid gray;
                                                border-radius: 5px;
                                                padding:0px}""")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(405,365)
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
        self.buttonback.resize(80,30)
        self.buttonback.clicked.connect(self.Window6)

        self.desc1 = QPlainTextEdit("    DENSITY is a scalar quantity defined as the ratio of an object's mass to the volume it occupies, and is frequently given the symbol rho in physics.\n    It is also known as mass density.\n    NOTE: less dense fluids will float on top of more dense fluids, and less dense solids will float on top of more dense fluids(keeping in mind that the average density of the entire solid object must be considered.",self)
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
        self.desc1.setGeometry(80,15,250,250)

        self.mass = QLineEdit(self)
        self.mass.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.mass.setValidator(QDoubleValidator(self))
        self.mass.move(100, 275)
        self.mass.resize(150,30)
        self.mass.setText("0")
        self.mass.setToolTip("Enter Mass")
        self.mass.setFont(QtGui.QFont('Lucida Fax',11))

        self.vol = QLineEdit(self)
        self.vol.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.vol.setValidator(QDoubleValidator(self))
        self.vol.move(100, 325)
        self.vol.resize(150,30)
        self.vol.setText("0")
        self.vol.setToolTip("Enter Volume")
        self.vol.setFont(QtGui.QFont('Lucida Fax',11))
    
    

        self.textbox10 = QLineEdit(self)
        self.textbox10.setReadOnly(True)
        self.textbox10.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox10.move(365, 275)
        self.textbox10.resize(150,30)
        self.textbox10.setToolTip("Density")
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
        self.button.move(405,325) # button.move(x,y)
        self.button.clicked.connect(self.prof) 

    @pyqtSlot()
    def prof(self):
        mass = float(self.mass.text())
        vol = float(self.vol.text())
        self.Submit(mass,vol)
    
    def Submit(self,mass,vol):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and mass != "" and vol != "":
            density = mass/vol
            density2 = float("{0:.2f}".format(density))
            self.textbox10.setText(f"{density2}")
        
        
        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and num == "":
            QMessageBox.warning(self, "Error","Please Input Mass", QMessageBox.Ok, QMessageBox.Ok)
        else:
           QMessageBox.warning(self, "Error","Please Input an Integer", QMessageBox.Ok, QMessageBox.Ok)
        
    def Window6(self):
        self.w = Window6()
        self.w.show()
        self.hide()
        
        
        
class Fpressure(QMainWindow):
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
        self.setWindowTitle("PRESSURE")
        self.image1 = QLabel(self)
        self.image1.setGeometry(305,15,250,250)
        image1 = QPixmap("density.png")
        self.image1.setStyleSheet("""QLabel{border: 3px solid gray;
                                                border-radius: 5px;
                                                padding:0px}""")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(405,365)
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
        self.buttonback.resize(80,30)
        self.buttonback.clicked.connect(self.Window6)

        
        self.desc1 = QPlainTextEdit("    PRESSURE is the effect of a force acting upon a surface. It is a scalar quantity calculated as the force applied per unit area, where the force applied is always perpendicular to the surface.\nNOTE:\n101 325 Pa\n\t=1 atm\n\t=1.01325\n\t=14.70 psi\n\t= 760 mmHg",self)
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
        self.desc1.setGeometry(80,15,250,250)

        self.force = QLineEdit(self)
        self.force.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.force.setValidator(QDoubleValidator(self))
        self.force.move(100, 275)
        self.force.resize(150,30)
        self.force.setText("0")
        self.force.setToolTip("Enter Force")
        self.force.setFont(QtGui.QFont('Lucida Fax',11))

        self.area = QLineEdit(self)
        self.area.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.area.setValidator(QDoubleValidator(self))
        self.area.move(100, 325)
        self.area.resize(150,30)
        self.area.setText("0")
        self.area.setToolTip("Enter Area")
        self.area.setFont(QtGui.QFont('Lucida Fax',11))
    
    

        self.textbox10 = QLineEdit(self)
        self.textbox10.setReadOnly(True)
        self.textbox10.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox10.move(365, 275)
        self.textbox10.resize(150,30)
        self.textbox10.setToolTip("Density")
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
        self.button.move(405,325) # button.move(x,y)
        self.button.clicked.connect(self.prof) 

    @pyqtSlot()
    def prof(self):
        force = float(self.force.text())
        area = float(self.area.text())
        self.Submit(force,area)
    
    def Submit(self,force,area):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and force != "" and area != "":
            pressure = force/area
            pressure2 = float("{0:.2f}".format(pressure))
            self.textbox10.setText(f"{pressure2}")
        
        
        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and num == "":
            QMessageBox.warning(self, "Error","Please Input Mass", QMessageBox.Ok, QMessageBox.Ok)
        else:
           QMessageBox.warning(self, "Error","Please Input an Integer", QMessageBox.Ok, QMessageBox.Ok)
        
    def Window6(self):
        self.w = Window6()
        self.w.show()
        self.hide()
        
        
class Ftorri(QMainWindow):
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
        self.setWindowTitle("TORRICELLI'S PRINCIPLE")
        self.image1 = QLabel(self)
        self.image1.setGeometry(305,15,250,250)
        image1 = QPixmap("density.png")
        self.image1.setStyleSheet("""QLabel{border: 3px solid gray;
                                                border-radius: 5px;
                                                padding:0px}""")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(405,365)
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
        self.buttonback.resize(80,30)
        self.buttonback.clicked.connect(self.Window6)
        
        self.desc1 = QPlainTextEdit(" TORRICELLI'S PRINCIPLE\n     The speed of liquid leaving a hole a distance h(height) below the surface is equal to that acquired by an object falling freely through a vertical distance h.\n    statement that the speed, v, of a liquid flowing under the force of gravity out of an opening in a tank is proportional jointly to the square root of the vertical distance, h, between the liquid surface and the centre of the opening and to the square root of twice the acceleration caused by gravity, 2g, or simply v = (2gh)1/2. (The value of the acceleration caused by gravity at the Earth’s surface is about 32.2 feet per second per second, or 9.8 metres per second per second.) The theorem is named after Evangelista Torricelli, who discovered it in 1643.",self)
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
        self.desc1.setGeometry(80,15,250,250)

        self.height = QLineEdit(self)
        self.height.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.height.setValidator(QDoubleValidator(self))
        self.height.move(100, 275)
        self.height.resize(150,30)
        self.height.setText("0")
        self.height.setToolTip("Enter height")
        self.height.setFont(QtGui.QFont('Lucida Fax',11))

        self.grav = QLineEdit(self)
        self.grav.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")

        self.grav.move(100, 325)
        self.grav.resize(150,30)
        self.grav.setText("9.8")
        self.grav.setToolTip("Enter Volume")
        self.grav.setReadOnly(True)
    
    

        self.textbox10 = QLineEdit(self)
        self.textbox10.setReadOnly(True)
        self.textbox10.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox10.move(365, 275)
        self.textbox10.resize(150,30)
        self.textbox10.setToolTip("Density")
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
        self.button.move(405,325) # button.move(x,y)
        self.button.clicked.connect(self.prof) 

    @pyqtSlot()
    def prof(self):
        height = float(self.height.text())
        grav = 9.8
        self.Submit(height,grav)
    
    def Submit(self,height,grav):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and height != "":
            torri = (2*grav*height)**(.5)
            torri2 = float("{0:.2f}".format(torri))
            self.textbox10.setText(f"{torri2}")
        
        
        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and num == "":
            QMessageBox.warning(self, "Error","Please Input Mass", QMessageBox.Ok, QMessageBox.Ok)
        else:
           QMessageBox.warning(self, "Error","Please Input an Integer", QMessageBox.Ok, QMessageBox.Ok)
        
    def Window6(self):
        self.w = Window6()
        self.w.show()
        self.hide()
        
class Work(QMainWindow):
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
        self.setWindowTitle("WORK")
        self.image1 = QLabel(self)
        self.image1.setGeometry(305,15,250,250)
        image1 = QPixmap("density.png")
        self.image1.setStyleSheet("""QLabel{border: 3px solid gray;
                                                border-radius: 5px;
                                                padding:0px}""")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(405,365)
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
        self.buttonback.resize(80,30)
        self.buttonback.clicked.connect(self.Window5)
        
        self.desc1 = QPlainTextEdit(" TORRICELLI'S PRINCIPLE\n     The speed of liquid leaving a hole a distance h(height) below the surface is equal to that acquired by an object falling freely through a vertical distance h.\n    statement that the speed, v, of a liquid flowing under the force of gravity out of an opening in a tank is proportional jointly to the square root of the vertical distance, h, between the liquid surface and the centre of the opening and to the square root of twice the acceleration caused by gravity, 2g, or simply v = (2gh)1/2. (The value of the acceleration caused by gravity at the Earth’s surface is about 32.2 feet per second per second, or 9.8 metres per second per second.) The theorem is named after Evangelista Torricelli, who discovered it in 1643.",self)
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
        self.desc1.setGeometry(80,15,250,250)

        self.height = QLineEdit(self)
        self.height.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.height.setValidator(QDoubleValidator(self))
        self.height.move(100, 275)
        self.height.resize(150,30)
        self.height.setText("0")
        self.height.setToolTip("Enter height")
        self.height.setFont(QtGui.QFont('Lucida Fax',11))

        self.grav = QLineEdit(self)
        self.grav.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")

        self.grav.move(100, 325)
        self.grav.resize(150,30)
        self.grav.setText("9.8")
        self.grav.setToolTip("Enter Volume")
        self.grav.setReadOnly(True)
    
    

        self.textbox10 = QLineEdit(self)
        self.textbox10.setReadOnly(True)
        self.textbox10.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox10.move(365, 275)
        self.textbox10.resize(150,30)
        self.textbox10.setToolTip("Density")
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
        self.button.move(405,325) # button.move(x,y)
        self.button.clicked.connect(self.prof) 

    @pyqtSlot()
    def prof(self):
        height = float(self.height.text())
        grav = 9.8
        self.Submit(height,grav)
    
    def Submit(self,height,grav):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and height != "":
            torri = (2*grav*height)**(.5)
            torri2 = float("{0:.2f}".format(torri))
            self.textbox10.setText(f"{torri2}")
        
        
        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and num == "":
            QMessageBox.warning(self, "Error","Please Input Mass", QMessageBox.Ok, QMessageBox.Ok)
        else:
           QMessageBox.warning(self, "Error","Please Input an Integer", QMessageBox.Ok, QMessageBox.Ok)
        
    def Window5(self):
        self.w = Window5()
        self.w.show()
        self.hide()
        
class Power(QMainWindow):
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
        self.setWindowTitle("POWER")
        self.image1 = QLabel(self)
        self.image1.setGeometry(305,15,250,250)
        image1 = QPixmap("density.png")
        self.image1.setStyleSheet("""QLabel{border: 3px solid gray;
                                                border-radius: 5px;
                                                padding:0px}""")
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to topics")
        self.buttonback.move(405,365)
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
        self.buttonback.resize(80,30)
        self.buttonback.clicked.connect(self.Window5)
        
        self.desc1 = QPlainTextEdit(" TORRICELLI'S PRINCIPLE\n     The speed of liquid leaving a hole a distance h(height) below the surface is equal to that acquired by an object falling freely through a vertical distance h.\n    statement that the speed, v, of a liquid flowing under the force of gravity out of an opening in a tank is proportional jointly to the square root of the vertical distance, h, between the liquid surface and the centre of the opening and to the square root of twice the acceleration caused by gravity, 2g, or simply v = (2gh)1/2. (The value of the acceleration caused by gravity at the Earth’s surface is about 32.2 feet per second per second, or 9.8 metres per second per second.) The theorem is named after Evangelista Torricelli, who discovered it in 1643.",self)
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
        self.desc1.setGeometry(80,15,250,250)

        self.height = QLineEdit(self)
        self.height.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.height.setValidator(QDoubleValidator(self))
        self.height.move(100, 275)
        self.height.resize(150,30)
        self.height.setText("0")
        self.height.setToolTip("Enter height")
        self.height.setFont(QtGui.QFont('Lucida Fax',11))

        self.grav = QLineEdit(self)
        self.grav.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")

        self.grav.move(100, 325)
        self.grav.resize(150,30)
        self.grav.setText("9.8")
        self.grav.setToolTip("Enter Volume")
        self.grav.setReadOnly(True)
    
    

        self.textbox10 = QLineEdit(self)
        self.textbox10.setReadOnly(True)
        self.textbox10.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox10.move(365, 275)
        self.textbox10.resize(150,30)
        self.textbox10.setToolTip("Density")
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
        self.button.move(405,325) # button.move(x,y)
        self.button.clicked.connect(self.prof) 

    @pyqtSlot()
    def prof(self):
        height = float(self.height.text())
        grav = 9.8
        self.Submit(height,grav)
    
    def Submit(self,height,grav):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and height != "":
            torri = (2*grav*height)**(.5)
            torri2 = float("{0:.2f}".format(torri))
            self.textbox10.setText(f"{torri2}")
        
        
        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and num == "":
            QMessageBox.warning(self, "Error","Please Input Mass", QMessageBox.Ok, QMessageBox.Ok)
        else:
           QMessageBox.warning(self, "Error","Please Input an Integer", QMessageBox.Ok, QMessageBox.Ok)
        
    def Window5(self):
        self.w = Window5()
        self.w.show()
        self.hide()
        
class Energy(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("first.jpg")
        sImage = oImage.scaled(QSize(550,350))  
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,600,420)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("first.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(400,190,600,420)
        self.setWindowTitle("ENERGY")
        
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
        self.buttonback.resize(80,30)
        self.buttonback.clicked.connect(self.Window5)
        
        self.textboxlbl = QLabel("POTENTIAL ENERGY",self)
        self.textboxlbl.setFont(QtGui.QFont('Times New Roman', 14))
        self.textboxlbl.setStyleSheet("""QLabel  {color: black;
                                                border: 2px black;
                                                border-radius: 5px;
                                                padding: 2px;
                                                border-style: outset;
                                                background: rgb(203, 177, 242);
                                                selection-background-color: darkgray;}""")
        self.textboxlbl.setGeometry(50,50,200,45)
        
        self.textboxlb2 = QLabel("KINETIC ENERGY",self)
        self.textboxlb2.setFont(QtGui.QFont('Times New Roman', 14))
        self.textboxlb2.setStyleSheet("""QLabel  {color: black;
                                                border: 2px black;
                                                border-radius: 5px;
                                                padding: 2px;
                                                border-style: outset;
                                                background: rgb(203, 177, 242);
                                                selection-background-color: darkgray;}""")
        self.textboxlb2.setGeometry(350,50,170,45)
        
        self.desc1 = QPlainTextEdit("What is Potential Energy?\n   Energy that is stored and waiting to be used later.\nGRAVITATIONAL ENERGY\n   It is a potential energy due to an object's position.\n   It is also associated with an object at a given location above the surface of the Earth.\nWHERE:\n   U = gravitational potential energy in Joules\n   m = mass\n   g = gravity\n   y = distance above the Earth's surface",self)
        self.desc1.setFont(QtGui.QFont('Lucida Fax',11))
        self.desc1.setReadOnly(True)
        self.desc1.setStyleSheet("""QPlainTextEdit{color: black;
                                                border: 3px black;
                                                border-radius: 30px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 darkGray, stop:1 rgba(98, 211, 162, 255));
                                                selection-background-color: green;}""")
        self.desc1.move(50, 60)
        self.desc1.setGeometry(30,100,250,250)
        
        
        self.desc2 = QPlainTextEdit("What is Kinetic Energy?\n   Energy an object has due to its motion.\n   A change in Kinetic Energy is one possible result of doing Work in transfer energy into a system.\nNOTE:\n   The speed of the system increases if the work done on it is positive.\n   The speed of the system decreases if the net work is negative.\nWHERE:\n   K = 1/2mv^2\n   K = kinetic energy\n   m = mass of the particle in kg\n   v = speed of the particle",self)
        self.desc2.setFont(QtGui.QFont('Lucida Fax',11))
        self.desc2.setReadOnly(True)
        self.desc2.setStyleSheet("""QPlainTextEdit{color: black;
                                                border: 3px black;
                                                border-radius: 30px;
                                                padding: 8px;
                                                border-style: outset;
                                                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 darkGray, stop:1 rgba(98, 211, 162, 255));
                                                selection-background-color: green;}""")
        self.desc2.move(50, 60)
        self.desc2.setGeometry(310,100,250,250)

        
        self.button = QPushButton('POTENTIAL ENERGY\nFORMULA', self)
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
        self.button.resize(150,50)
        self.button.setToolTip("Potential Energy")
        self.button.move(80,360)
        self.button.clicked.connect(self.Potential)
        
        
        self.button2 = QPushButton('KINETIC ENERGY\nFORMULA', self)
        self.button2.setStyleSheet("""QPushButton  {color: green;
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
        self.button2.resize(150,50)
        self.button2.setToolTip("Kinetic Energy")
        self.button2.move(360,360)
        self.button2.clicked.connect(self.Kinetic)


    def Window5(self):
        self.w = Window5()
        self.w.show()
        self.hide()
        
    def Potential(self):
        self.w = Potential()
        self.w.show()
        self.hide()
        
    def Kinetic(self):
        self.w = Kinetic()
        self.w.show()
        self.hide()

class Potential(QMainWindow):
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
        self.setWindowTitle("POTENTIAL ENERGY")
        self.image1 = QLabel(self)
        self.image1.setGeometry(305,15,250,250)
        
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to energy")
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
        self.buttonback.resize(80,30)
        self.buttonback.clicked.connect(self.Energy)

        self.textboxlb = QLabel("Enter Mass:",self)
        self.textboxlb.move(100,245)
        self.textboxlb.setStyleSheet("font-weight: bold;")
        self.textboxlb.setFont(QtGui.QFont('Lucida Fax',12))
        self.mass = QLineEdit(self)
        self.mass.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.mass.setValidator(QDoubleValidator(self))
        self.mass.move(100, 275)
        self.mass.resize(150,30)
        self.mass.setText("0")
        self.mass.setToolTip("Enter Mass")
        self.mass.setFont(QtGui.QFont('Lucida Fax',11))
        
        
        self.textboxlb2 = QLabel("Enter Distance:",self)
        self.textboxlb2.move(100,310)
        self.textboxlb2.resize(150,20)
        self.textboxlb2.setStyleSheet("font-weight: bold;")
        self.textboxlb2.setFont(QtGui.QFont('Lucida Fax',12))
        self.dist = QLineEdit(self)
        self.dist.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.dist.setValidator(QDoubleValidator(self))
        self.dist.move(100, 335)
        self.dist.resize(150,30)
        self.dist.setText("0")
        self.dist.setToolTip("Enter Distance")
        self.dist.setFont(QtGui.QFont('Lucida Fax',11))
    
    
        self.textboxlb3 = QLabel("Potential Energy",self)
        self.textboxlb3.move(305,250)
        self.textboxlb3.resize(150,20)
        self.textboxlb3.setStyleSheet("font-weight: bold;")
        self.textboxlb3.setFont(QtGui.QFont('Lucida Fax',12))
        self.textbox10 = QLineEdit(self)
        self.textbox10.setReadOnly(True)
        self.textbox10.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox10.move(305, 275)
        self.textbox10.resize(150,30)
        self.textbox10.setToolTip("Potential Energy")
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
        self.button.move(335,325) # button.move(x,y)
        self.button.clicked.connect(self.prof) 

    @pyqtSlot()
    def prof(self):
        mass = float(self.mass.text())
        dist = float(self.dist.text())
        self.Submit(mass,dist)
    
    def Submit(self,mass,dist):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and mass != "" and dist != "":
            potential = mass*9.8*dist
            potential2 = float("{0:.2f}".format(potential))
            self.textbox10.setText(f"{potential2}")
        
        
        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and num == "":
            QMessageBox.warning(self, "Error","Please Input Mass", QMessageBox.Ok, QMessageBox.Ok)
        else:
           QMessageBox.warning(self, "Error","Please Input an Integer", QMessageBox.Ok, QMessageBox.Ok)
        
    def Energy(self):
        self.w = Energy()
        self.w.show()
        self.hide()
        
class Kinetic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('young-lion_97429.ico'))
        oImage = QImage("calculate.jpg")
        sImage = oImage.scaled(QSize(800,800))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage)) 
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.setGeometry(95,245,440,120)
        self.label.setGraphicsEffect(QGraphicsBlurEffect())
        self.label.setPixmap(QPixmap("calculate.jpg"))
        self.label.setScaledContents(True)
        self.setGeometry(400,190,600,420)
        self.setWindowTitle("KINETIC ENERGY")
        
        self.buttonback = QPushButton("Back",self)
        self.buttonback.setToolTip("Go back to energy")
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
        self.buttonback.resize(80,30)
        self.buttonback.clicked.connect(self.Energy)

        
        self.textboxlb = QLabel("Enter Mass:",self)
        self.textboxlb.move(100,245)
        self.textboxlb.setStyleSheet("font-weight: bold;")
        self.textboxlb.setFont(QtGui.QFont('Lucida Fax',12))
        self.mass = QLineEdit(self)
        self.mass.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.mass.setValidator(QDoubleValidator(self))
        self.mass.move(100, 275)
        self.mass.resize(150,30)
        self.mass.setText("0")
        self.mass.setToolTip("Enter Mass")
        self.mass.setFont(QtGui.QFont('Lucida Fax',11))


        self.textboxlb2 = QLabel("Enter Speed/Velocity:",self)
        self.textboxlb2.move(100,310)
        self.textboxlb2.resize(200,20)
        self.textboxlb2.setStyleSheet("font-weight: bold;")
        self.textboxlb2.setFont(QtGui.QFont('Lucida Fax',12))
        self.vel = QLineEdit(self)
        self.vel.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.vel.setValidator(QDoubleValidator(self))
        self.vel.move(100, 335)
        self.vel.resize(150,30)
        self.vel.setText("0")
        self.vel.setToolTip("Enter Velocity")
        self.vel.setFont(QtGui.QFont('Lucida Fax',11))
    
    
        self.textboxlb3 = QLabel("Kinetic Energy",self)
        self.textboxlb3.move(305,250)
        self.textboxlb3.resize(150,20)
        self.textboxlb3.setStyleSheet("font-weight: bold;")
        self.textboxlb3.setFont(QtGui.QFont('Lucida Fax',12))
        self.textbox10 = QLineEdit(self)
        self.textbox10.setReadOnly(True)
        self.textbox10.setStyleSheet("""QLineEdit{border: 2px solid gray;
                                                border-radius: 10px;
                                                padding: 0 8px;
                                                background: yellow;
                                                selection-background-color: darkgray;}""")
        self.textbox10.move(305, 275)
        self.textbox10.resize(150,30)
        self.textbox10.setToolTip("Kinetic Energy")
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
        self.button.move(335,325) # button.move(x,y)
        self.button.clicked.connect(self.prof) 

    @pyqtSlot()
    def prof(self):
        mass = float(self.mass.text())
        vel = float(self.vel.text())
        self.Submit(mass,vel)
    
    def Submit(self,mass,vel):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and mass != "" and vel != "":
            kinetic = (1/2*(mass*vel))
            kinetic2 = float("{0:.2f}".format(kinetic))
            self.textbox10.setText(f"{kinetic2}")
        
        
        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and num == "":
            QMessageBox.warning(self, "Error","Please Input Mass", QMessageBox.Ok, QMessageBox.Ok)
        else:
           QMessageBox.warning(self, "Error","Please Input an Integer", QMessageBox.Ok, QMessageBox.Ok)
        
    def Energy(self):
        self.w = Energy()
        self.w.show()
        self.hide()
        

        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Window2()
    sys.exit(app.exec_())
