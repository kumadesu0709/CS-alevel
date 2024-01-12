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
        ok_button = qtw.QPushButton("Ok")
        ok_button.clicked.connect(self.ok_btn_pushed)
        layout.addWidget(ok_button,2,1,1,2)
        self.line_edit = qtw.QLineEdit("0")
        layout.addWidget(self.line_edit,0,1,1,2)
        layout.addWidget(qtw.QLabel("Metres"),1,0,1,1)
        self.metre = qtw.QLabel("0")
        layout.addWidget(self.metre,1,1,1,2)




        widget = qtw.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def ok_btn_pushed(self):
        self.metre.setText(str(int(self.line_edit.text()) * 0.3048))
        dlg = QMessageBox.warning(self,"Quit?","Are you sure", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        if dlg == QMessageBox.ok:
            self.close

app = qtw.QApplication([])

window = MainWindow()
window.show()
app.exec()