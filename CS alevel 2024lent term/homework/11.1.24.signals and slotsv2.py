import PyQt6.QtWidgets as qtw
# import PyQt6.QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6.QtWidgets import QMessageBox

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversion Tool.")

        layout = qtw.QGridLayout()
        layout.addWidget(qtw.QLabel("Feet"),0,0,1,1)
        self.line_edit = qtw.QLineEdit("")
        self.line_edit.textChanged.connect(self.text_changed)
        layout.addWidget(self.line_edit,0,1,1,2)
        layout.addWidget(qtw.QLabel("Metres"),1,0,1,1)
        self.metre = qtw.QLabel("")
        layout.addWidget(self.metre,1,1,1,2)



        widget = qtw.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def text_changed(self):
        self.metre.setText(str(int(self.line_edit.text()) * 0.3048))

app = qtw.QApplication([])

window = MainWindow()
window.show()
app.exec()