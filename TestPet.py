from PetClass import Pet
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = Pet( 100, 100)
    sys.exit(app.exec_())