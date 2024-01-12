import PyQt6.QtWidgets as qtw
# import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg


# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template Window")

        layout = qtw.QVBoxLayout()
        self.label = qtw.QLabel("Demo")
        layout.addWidget(self.label)
        
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