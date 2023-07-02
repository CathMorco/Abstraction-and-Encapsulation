#Imports necessary elements
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
import sys
from PyQt5.QtWidgets import QApplication

#creates class for widgets
class Car(QWidget):
    def __init__(self, yearModel, make, x, y):
        super().__init__()
        self.positionx = x
        self.positiony = y
        self.__speed = 0
        self.__year_model = yearModel
        self.__make = make

        self.initUI()

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

#creates function for GUI

    def initUI(self):
        #Creates the appropriate labels for each function
        speed_label = QLabel("Speed:")
        self.speed_value_label = QLabel(str(self.get_speed()))

        change_speed_button1 = QPushButton("Accelerate")
        change_speed_button1.clicked.connect(self.change_speed_accelerate)

        change_speed_button2 = QPushButton("Brake")
        change_speed_button2.clicked.connect(self.change_speed_brake)

        

        #Determines the layout of the GUI
        vbox = QVBoxLayout()
        vbox.addWidget(speed_label)
        vbox.addWidget(self.speed_value_label)
        vbox.addWidget(change_speed_button1)
        vbox.addWidget(change_speed_button2)

        self.setLayout(vbox)
        self.setGeometry(self.positionx, self.positiony, 800, 200)
        self.setWindowTitle(self.__year_model + self.__make)
        self.show()

    def change_speed_accelerate(self):
        self.accelerate()
        self.speed_value_label.setText(str(self.get_speed()))

    def change_speed_brake(self):
        self.brake()
        self.speed_value_label.setText(str(self.get_speed()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    car = Car("1990 ","5th Edition", 100, 100)
    sys.exit(app.exec_())

