from CarClass import Car
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    car = Car("1990 ","5th Edition", 100, 100)
    sys.exit(app.exec_())
