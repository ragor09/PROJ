import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import pyqtSlot, QSize
from sqlitedict import *

class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        
        self.title = "Antipuesto"
        self.x=200 
        self.y=200 
        self.width=600
        self.height=350
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('young-lion_97429.ico')) 
        oImage = QImage("123.jpg")
        sImage = oImage.scaled(QSize(550,350))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.textboxlbl = QLabel("ACCOUNT REGISTRATTION SYSTEM",self)
        self.textboxlbl.move(215,20)
        self.textboxlb2 = QLabel("First Name:",self)
        self.textboxlb2.move(120,60)
        self.textboxlb3 = QLabel("Last Name:",self)
        self.textboxlb3.move(120,100)
        self.textboxlb4 = QLabel("Username:",self)
        self.textboxlb4.move(122,140)
        self.textboxlb5 = QLabel("Password:",self)
        self.textboxlb5.move(122,180)
        self.textboxlb6 = QLabel("E-mail:",self)
        self.textboxlb6.move(141,220)
        self.textboxlb7 = QLabel("Contact No.:",self)
        self.textboxlb7.move(112,260)

        self.textbox = QLineEdit(self)
        self.textbox.move(175, 50)
        self.textbox.resize(280,30)
        self.textbox.setToolTip("Enter your First Name")
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(175, 90)
        self.textbox2.resize(280,30)
        self.textbox2.setToolTip("Enter your Last Name")
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(175, 130)
        self.textbox3.resize(280,30)
        self.textbox3.setToolTip("Enter Username")
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(175, 170)
        self.textbox4.resize(280,30)
        self.textbox4.setToolTip("Enter Password")
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(175, 210)
        self.textbox5.resize(280,30)
        self.textbox5.setToolTip("Enter your email")
        self.textbox6 = QLineEdit(self)
        self.textbox6.move(175, 250)
        self.textbox6.resize(280,30)
        self.textbox6.setToolTip("Enter your Contact Number")

        self.button = QPushButton('Submit', self)
        self.button.setToolTip("Submit your info")
        self.button.move(175,290) # button.move(x,y)
        self.button2 = QPushButton('Clear',self)
        self.button2.setToolTip("Clears everything")
        self.button2.move(380,290) # button.move(x,y)
        self.button.clicked.connect(self.prof)
        self.button2.clicked.connect(self.on_click)
        
        
        self.show()

    @pyqtSlot()
    def prof(self):
        fName = self.textbox.text()
        lName = self.textbox2.text()
        userN = self.textbox3.text()
        passw = self.textbox4.text()
        email = self.textbox5.text()
        num = self.textbox6.text()
        
        self.Submit(fName, lName, userN, passw, email, num)

    def Submit(self,fName, lName, userN, passw, email, num):
        button = QMessageBox.question(self,"Submit Data", "Are you sure?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
        if button == QMessageBox.Yes and fName != "" and lName != "" and userN != "" and passw != "" and email != "" and num != "":
            dataDB = SqliteDict("some.db", autocommit=True)
            reglist = dataDB.get('reg',[])
            listdict = {"fname":fName,"lastname":lName,"username":userN, "password":passw, "emailAdd":email, "contact":num}
            reglist.append(listdict)
            dataDB['reg'] = reglist
            print(dataDB['reg'])

            QMessageBox.information(self, "Evaluation", "Registration Complete", QMessageBox.Ok, QMessageBox.Ok)
            self.textbox.setText("")
            self.textbox2.setText("")
            self.textbox3.setText("")
            self.textbox4.setText("")
            self.textbox5.setText("")
            self.textbox6.setText("")
        
        elif button == QMessageBox.No:
            pass
        
        elif button == QMessageBox.Yes and fName == "" and lName == "" and userN == "" and passw == "" and email == "" and num == "":
            QMessageBox.warning(self, "Error","Required input on every field", QMessageBox.Ok, QMessageBox.Ok)
        elif button == QMessageBox.Yes and fName == "":
            QMessageBox.warning(self, "Error","Please Input your First Name", QMessageBox.Ok, QMessageBox.Ok)
        elif button == QMessageBox.Yes and lName == "":
            QMessageBox.warning(self, "Error","Please Input your Last Name", QMessageBox.Ok, QMessageBox.Ok)
        elif button == QMessageBox.Yes and userN == "":
            QMessageBox.warning(self, "Error","Please Input Username", QMessageBox.Ok, QMessageBox.Ok)
        elif button == QMessageBox.Yes and passw == "":
            QMessageBox.warning(self, "Error","Please Input Password", QMessageBox.Ok, QMessageBox.Ok)
        elif button == QMessageBox.Yes and email == "":
            QMessageBox.warning(self, "Error","Please Input your Email", QMessageBox.Ok, QMessageBox.Ok)
        elif button == QMessageBox.Yes and num == "":
            QMessageBox.warning(self, "Error","Please Input your Contact Number", QMessageBox.Ok, QMessageBox.Ok)
        else:
           pass
        
    def on_click(self):
        self.textbox.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")
        self.textbox6.setText("")
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())
    









