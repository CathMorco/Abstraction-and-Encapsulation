from FanClass import Fan
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Fan1 = Fan(3,10,"Yellow", 100, 100)
    Fan2 = Fan(2,5,"Blue", 500, 100)
    sys.exit(app.exec_())