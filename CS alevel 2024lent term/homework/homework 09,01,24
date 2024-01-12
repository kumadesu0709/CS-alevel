import PyQt6.QtWidgets as qtw
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")

        layout = qtw.QVBoxLayout()
        self.label = qtw.QLabel("WidgetDemo")
        layout.addWidget(self.label)

        combo = qtw.QComboBox()
        combo.addItems(["One","Two","Three","Four"])
        layout.addWidget(combo)

        self.checkbox1 = qtw.QCheckBox("Choose this")
        layout.addWidget(self.checkbox1)
        self.checkbox2 = qtw.QCheckBox("and this?")
        layout.addWidget(self.checkbox2)

        self.line_edit = qtw.QLineEdit("Type Here")
        layout.addWidget(self.line_edit)

        self.radio_button1 = qtw.QRadioButton("This one?")
        self.radio_button2 = qtw.QRadioButton("Or this one?")
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)

        self.slider= qtw.QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(self.slider)

        self.button1 = qtw.QPushButton("Ok")
        self.button2 = qtw.QPushButton("Cancel")
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        ok_button = qtw.QPushButton("ok")
        ok_button.clicked.connect(self.do_stuff)
        layout.addWidget(ok_button)

        open_btn = qtw.QPushButton("Open")
        open_btn.clicked.connect(self.open_btn_click)
        layout.addWidget(open_btn)

        save_btn = qtw.QPushButton("Save")
        save_btn.clicked.connect(self.save_btn_click)
        layout.addWidget(save_btn)


        widget = qtw.QWidget()
        widget.setLayout(layout)
        

        self.setCentralWidget(widget)

    def do_stuff(self):
        print("stuff")
        thing = QMessageBox.warning(self,"Hold up", "You did stuff", QMessageBox.StandardButton.Ok| QMessageBox.StandardButton.Cancel)
        print(thing)
    
    def open_btn_click(self):
        filename,_ = QFileDialog.getOpenFileName(self,"Open File", ".", "Text Files (*.txt *.html)")
        print(filename)

    def save_btn_click(self):
        filename,_ = QFileDialog.getSaveFileName(self,"Save File", ".", "Text Files (*.txt *.html)")
        print(filename)


app = qtw.QApplication([])

window = MainWindow()
window.show()
app.exec()