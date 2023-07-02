#Write a class named Pet, which should have the following data attributes:
#• _ _name (for the name of a pet)
#• _ _animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
#• _ _age (for the pet’s age)

#The Pet class should have an _ _init_ _ method that creates these attributes. It should also have the following methods:
#• set_name()
#This method assigns a value to the _ _name field.
#• set_animal_type()
#This method assigns a value to the _ _animal_type field.
#• set_age()
#This method assigns a value to the _ _age field.
#• get_name()
#This method returns the value of the _ _ name field.
#• get_animal_type()
#This method returns the value of the _ _animal_type field.
#• get_age()
#This method returns the value of the _ _age field.

#Imports necessary elements
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QInputDialog, QMessageBox
import sys
from PyQt5.QtWidgets import QApplication

#creates class for widgets
class Pet(QWidget):
    def __init__(self, x, y):
        super().__init__()
        self.positionx = x
        self.positiony = y
        self.__name = ""
        self.__animal_type = ""
        self.__age = ""

        
        self.initUI()

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

#creates function for GUI

    def initUI(self):
        #Creates the appropriate labels for each function
        name_label = QLabel("Name:")
        self.nameLabel = QLabel(str(self.get_name()))

        animal_type_label = QLabel("Animal Type:")
        self.animalType_label = QLabel(str(self.get_animal_type()))

        age_label = QLabel("Age:")
        self.age_value_label = QLabel(str(self.get_age()))
        
        #Creates buttons for each function
        change_name_button = QPushButton("Name")
        change_name_button.clicked.connect(self.change_name)

        #Determines the layout of the GUI
        vbox = QVBoxLayout()
        vbox.addWidget(name_label)
        vbox.addWidget(self.nameLabel)
        vbox.addWidget(animal_type_label)
        vbox.addWidget(self.animalType_label)
        vbox.addWidget(age_label)
        vbox.addWidget(self.age_value_label)

        vbox.addWidget(change_name_button)

        self.setLayout(vbox)
        self.setGeometry(self.positionx, self.positiony, 200, 200)
        self.setWindowTitle("Pet")
        self.show()

    def change_name(self):
        name, ok = QInputDialog.getText(self, "Change Name", "Enter Name:")
        if ok and name:
            self.set_name(name)
            self.nameLabel.setText(str(self.get_name()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = Pet( 100, 100)
    sys.exit(app.exec_())