from CarClass import Car
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    car = Car("2003 ","Chevrolet", 100, 100)
    sys.exit(app.exec_())
