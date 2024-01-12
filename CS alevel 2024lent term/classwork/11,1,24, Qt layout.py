import PyQt6.QtWidgets as qtw
# import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg


# Subclass QMainWindow to customise your application's main window
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
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = qtw.QApplication([])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.