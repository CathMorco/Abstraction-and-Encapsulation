#Write a class named Car that has the following data attributes:
#• _ _year_model (for the car’s year model)
#• _ _make (for the make of the car)
#• _ _speed (for the car’s current speed)

#The Car class should have an _ _init_ _ method that accepts the car’s year model and make as arguments. These values should be assigned to the object’s _ _year_model and _ _make data attributes. It should also assign 0 to the _ _speed data attribute.

#The class should also have the following methods:
#• accelerate()
#The accelerate method should add 5 to the speed data attribute each time it is called.
#• brake()
#The brake method should subtract 5 from the speed data attribute each time it is called.
#• get_speed()
#The get_speed method should return the current speed.

#Imports necessary elements
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QInputDialog, QMessageBox

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
        self.speed_value_label = QLabel(str(self.getter_speed()))
        on_label = QLabel("On:")
        self.on_value_label = QLabel(str(self.__on))
        radius_label = QLabel("Radius:")
        self.radius_value_label = QLabel(str(self.getter_radius()))
        color_label = QLabel("Color:")
        self.color_value_label = QLabel(self.getter_color())
        
        #Creates buttons for each function
        change_on_button = QPushButton("Power")
        change_on_button.clicked.connect(self.change_on)

        change_speed_button = QPushButton("Change Speed")
        change_speed_button.clicked.connect(self.change_speed)

        change_radius_button = QPushButton("Change Radius")
        change_radius_button.clicked.connect(self.change_radius)

        change_color_button = QPushButton("Change Color")
        change_color_button.clicked.connect(self.change_color)

        #Determines the layout of the GUI
        vbox = QVBoxLayout()
        vbox.addWidget(speed_label)
        vbox.addWidget(self.speed_value_label)
        vbox.addWidget(on_label)
        vbox.addWidget(self.on_value_label)
        vbox.addWidget(radius_label)
        vbox.addWidget(self.radius_value_label)
        vbox.addWidget(color_label)
        vbox.addWidget(self.color_value_label)
        vbox.addWidget(change_on_button)
        vbox.addWidget(change_speed_button)
        vbox.addWidget(change_radius_button)
        vbox.addWidget(change_color_button)

        self.setLayout(vbox)
        self.setGeometry(self.positionx, self.positiony, 200, 200)
        self.setWindowTitle("Fan")
        self.show()

    #The function that is connected to the change speed button, it utilizes the setters and getters of the program
    def change_speed(self):
        speed, ok = QInputDialog.getInt(self, "Change Speed", "Enter Speed(1-3):", self.__speed, 1, 3)
        if ok:
            speed_labels = {1: "slow", 2: "medium", 3: "fast"}
            if speed in speed_labels:
                self.setter_speed(speed)
                self.speed_value_label.setText(str(self.getter_speed()) + " (" + speed_labels[speed] + ")")

    #The function that is connected to the Power Button it utilizes the setters and getters of the program
    def change_on(self):
        self.setter_on(not self.__on)
        self.on_value_label.setText(str(self.getter_on()))

    #The function that is connected to the change radius button, it utilizes the setters and getters of the program
    def change_radius(self):
        radius, ok = QInputDialog.getInt(self, "Change Radius", "Enter Radius. Your Radius Should not be Negative in Value:", self.__radius)
        if ok:
            if radius >= 0:
                self.setter_radius(radius)
                self.radius_value_label.setText(str(self.getter_radius()))
            else:
                QMessageBox.warning(self, "Invalid Radius", "I'm sorry, your radius can not be negative in value, please choose a positive integer")

    #The function that is connected to the change colors button, it utilizes the setters and getters of the program
    def change_color(self):
        colors = ["Red", "Green", "Blue", "Pink", "White", "Orange", "Yellow", "Purple","Lilac","Lavender","Indigo"]
        color, ok = QInputDialog.getItem(self, "Change Color", "Select Color:", colors, 0, False)
        if ok and color:
            self.setter_color(color)
            self.color_value_label.setText(str(self.getter_color()))

