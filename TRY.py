import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import pyqtSlot, QSize
from sqlitedict import *

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
        oImage = QImage("123.jpg")
        sImage = oImage.scaled(QSize(550,350))   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                        
        self.setPalette(palette)
        
        self.textboxlbl = QLabel("     PHYSICS\n"
        "Calculus-Based",self)
        self.textboxlbl.move(255, 130)

        self.button = QPushButton('EXPLORE', self)
        self.button.setToolTip("Explore the wonderinfo")
        self.button.move(255,190) # button.move(x,y)
       
        self.button.clicked.connect(self.prof)
    
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
    









