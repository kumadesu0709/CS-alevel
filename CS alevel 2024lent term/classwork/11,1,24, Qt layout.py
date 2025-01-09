import PyQt6.QtWidgets as qtw
# import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Demo")
        layout = qtw.QGridLayout()
        form_layout = qtw.QFormLayout()
        form_layout.addRow("Name:",qtw.QLineEdit("Name"))
        form_layout.addRow("Location:",qtw.QLineEdit("Location"))
        layout.addLayout(form_layout,0,0,1,3)

        combo = qtw.QComboBox()
        combo.addItems(["One","Two","Three","Four"])
        layout.addWidget(combo,1,0,1,2) #Row comes first
        
        layout.addWidget(qtw.QCheckBox("On or off"),1,2,1,1)

        ok_btn = qtw.QPushButton("Ok")
        cancel_btn = qtw.QPushButton("Cancel")
        layout.addWidget(ok_btn,2,1,1,1)
        layout.addWidget(cancel_btn,2,2,1,1)

        widget = qtw.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = qtw.QApplication([])

window = MainWindow()
window.show()

app.exec()