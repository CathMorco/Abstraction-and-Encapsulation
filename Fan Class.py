# Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
# A private int data field named speed that specifies the speed of the fan.
# A private bool data field named on that specifies whether the fan is on (the default is False).
# A private float data field named radius that specifies the radius of the fan.
# A private string data field named color that specifies the color of the fan.
# The accessor(getters)  and mutator(setters)  methods for all four data fields.
# A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).

#Imports necessary elements
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QInputDialog

#creates class for widgets
class Fan(QWidget):
    def __init__(self, x, y):
        super().__init__()
        self.positionx = x
        self.positiony = y
        self.__speed = 1
        self.__on = False
        self.__radius = 0
        self.__color = ""

        self.initUI()
# accessor(getters)  and mutator(setters) for a private int data field named speed 
    def getter_speed(self):
        return self.__speed

    def setter_speed(self, speed):
        self.__speed = speed
# accessor(getters)  and mutator(setters) for a private bool data field named on
    def getter_on(self):
        return self.__on

    def setter_on(self, on):
        self.__on = on

# accessor(getters)  and mutator(setters) for a private float data field named radius
    def getter_radius(self):
        return self.__radius

    def setter_radius(self, radius):
        self.__radius = radius

# accessor(getters)  and mutator(setters)  for a private string data field named color
    def getter_color(self):
        return self.__color

    def setter_color(self, color):
        self.__color = color

#creates function for GUI

    def initUI(self):
        speed_label = QLabel("Speed:")
        self.speed_value_label = QLabel(str(self.getter_speed()))
        on_label = QLabel("On:")
        self.on_value_label = QLabel(str(self.__on))
        radius_label = QLabel("Radius:")
        radius_value_label = QLabel(str(self.__radius))
        color_label = QLabel("Color:")
        color_value_label = QLabel(self.__color)

        change_speed_button = QPushButton("Change Speed")
        change_speed_button.clicked.connect(self.change_speed)

        change_on_button = QPushButton("Turn On/Off")
        change_on_button.clicked.connect(self.change_on)


        vbox = QVBoxLayout()
        vbox.addWidget(speed_label)
        vbox.addWidget(self.speed_value_label)
        vbox.addWidget(on_label)
        vbox.addWidget(self.on_value_label)
        vbox.addWidget(radius_label)
        vbox.addWidget(radius_value_label)
        vbox.addWidget(color_label)
        vbox.addWidget(color_value_label)
        vbox.addWidget(change_speed_button)
        vbox.addWidget(change_on_button)

        self.setLayout(vbox)
        self.setGeometry(self.positionx, self.positiony, 200, 200)
        self.setWindowTitle("Fan")
        self.show()

    def change_speed(self):
        speed, ok = QInputDialog.getInt(self, "Change Speed", "Enter Speed:", self.__speed)
        if ok:
            self.setter_speed(speed)
            self.speed_value_label.setText(str(self.getter_speed()))

    def change_on(self):
        self.setter_on(not self.__on)
        self.on_value_label.setText(str(self.__on))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Fan(100, 100)
    sys.exit(app.exec_())