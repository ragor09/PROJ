import sys
from sqlitedict import *
from PyQt5.QtWidgets import QWidget,QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Registration"
        self.x=200
        self.y=200
        self.width=700
        self.height=500
        self.initUI()
        self.show
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        
        self.textbox1 = QLineEdit(self)
        self.textboxlbl = QLabel("First Name:", self)
        self.textboxlbl.move(190,79)
        self.textbox1.setText("Enter your First Name")
        self.textbox1.move(250,70)
        self.textbox1.resize(280,30)
        
        self.textbox2 = QLineEdit(self)
        self.textboxlbl2 = QLabel("Last Name:", self)
        self.textboxlbl2.move(190,119)
        self.textbox2.setText("Enter your Last Name")
        self.textbox2.move(250,110)
        self.textbox2.resize(280,30)
        
        self.textbox3 = QLineEdit(self)
        self.textboxlbl3 = QLabel("Username:", self)
        self.textboxlbl3.move(191,159)
        self.textbox3.setText("Enter your Username")
        self.textbox3.move(250,150)
        self.textbox3.resize(280,30)

        self.textbox4 = QLineEdit(self)
        self.textboxlbl4 = QLabel("Password:", self)
        self.textboxlbl4.move(193,199)
        self.textbox4.setText("Enter your Password")
        self.textbox4.move(250,190)
        self.textbox4.resize(280,30)

        self.textbox5 = QLineEdit(self)
        self.textboxlbl5 = QLabel("Email Address:", self)
        self.textboxlbl5.move(172,239)
        self.textbox5.setText("Enter your Email")
        self.textbox5.move(250,230)
        self.textbox5.resize(280,30)
        
        self.textbox6 = QLineEdit(self)
        self.textboxlbl6 = QLabel("Contact Number:", self)
        self.textboxlbl6.move(161,279)
        self.textbox6.setText("Enter your Contact Number")
        self.textbox6.move(250,270)
        self.textbox6.resize(280,30)

        self.button = QPushButton('Submit', self)
        self.button.setToolTip("Submit your information to the Account Registration")
        self.button.move(149,310)
        self.button.clicked.connect(self.data) 
        self.button2 = QPushButton('Clear',self)
        self.button2.setToolTip("Clearing all your information from the ACCOUNT Registration ")
        self.button2.move(305,310)
        self.button2.clicked.connect(self.clear)
        self.button3 = QPushButton('Exit', self)
        self.button3.setToolTip("Exit to the Account Registration")
        self.button3.move(461,310)
        self.button3.clicked.connect(QApplication.instance().quit)
        
        self.show()

    @pyqtSlot()

    def submitBox(self):
        buttonReply = QMessageBox.question(self,"Submitting Data", "Do you want to submit the information ? ", 
                                                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            QMessageBox.warning(self,"Evalutaion", "Registration Complete", QMessageBox.Ok,QMessageBox.Ok)

        else:
           pass

    def clear(self):
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")

    def data(self):
        fname = self.textbox1.text()
        lastname = self.textbox2.text()
        username = self.textbox3.text()
        password = self.textbox4.text()
        emailAdd = self.textbox5.text()
        contact = self.textbox6.text()
        
        self.submitdata(fname, lastname, username, password, emailAdd, contact)
        
    def submitdata(self, fname, lastname, username, password, emailAdd, contact):
        submitting = QMessageBox.question(self, "Submitting Data", "Confirm?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if submitting == QMessageBox.Yes and fname != "" and lastname != "" and username != "" and password != "" and emailAdd != "" and contact != "":
            dataDB = SqliteDict("Ddd.db", autocommit=True)
            reglist = dataDB.get('reg',[])
            listdict = {"fname":fname,"lastname":lastname,"username":username, "password":password, "emailAdd":emailAdd, "contact":contact}
            reglist.append(listdict)
            dataDB['reg'] = reglist
            print(dataDB['reg'])

            QMessageBox.information(self, "Evaluation", "Registration Complete", QMessageBox.Ok, QMessageBox.Ok)
        
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and fname == "" and lastname == "" and username == "" and password == "" and emailAdd == "" and contact == "":
            pass
        elif submitting == QMessageBox.No and fname == "" or lastname == "" or username == "" or password == "" or emailAdd == "" or contact == "":
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)


    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Confirmation',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec())

    