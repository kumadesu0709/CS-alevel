import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Signals and Slots")

        layout = QVBoxLayout()

        # Create a button
        ok_btn = QPushButton("Ok")
        ok_btn.clicked.connect(self.button_click)
        layout.addWidget(ok_btn)

        # Create another button
        reset_btn = QPushButton("Reset")
        reset_btn.clicked.connect(self.reset_button_click)
        layout.addWidget(reset_btn)

        # A text edit box
        self.edit_box = QLineEdit("Type here")
        self.edit_box.textChanged.connect(self.on_text_change)
        layout.addWidget(self.edit_box)

        # Create the windows central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def button_click(self):
        """The slot that gets called when the ok button is clicked"""
        edit_contents = self.edit_box.text()
        print(f"Ok: {edit_contents}")

    def reset_button_click(self):
        """The slot that gets called when the reset button is clicked"""
        self.edit_box.setText("Type here:")

    def on_text_change(self, new_text):
        """
        This slot gets called when the text in the edit box changes.
        QLineEdit.textChanged includes a string, the new text.
        """
        print(new_text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()