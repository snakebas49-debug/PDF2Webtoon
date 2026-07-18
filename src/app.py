
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
import sys
def run():
    app=QApplication(sys.argv)
    w=MainWindow()
    w.show()
    sys.exit(app.exec())
