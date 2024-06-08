import sys
from PySide6.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)
myWindow = QWidget()
myWindow.show()
n=app.exec()
sys.exit(n)