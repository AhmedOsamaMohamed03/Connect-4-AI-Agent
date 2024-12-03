import sys
from PyQt5.QtWidgets import QApplication
from gui.GUI import ConnectFour

def main():
    app = QApplication(sys.argv)
    board = ConnectFour()
    board.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
   main()