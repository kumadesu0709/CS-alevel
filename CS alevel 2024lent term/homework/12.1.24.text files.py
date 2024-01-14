import PyQt6.QtWidgets as qtw
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor")

        vlayout = qtw.QVBoxLayout()
        hlayout = qtw.QHBoxLayout()

        self.main_text = qtw.QTextEdit()
        text = self.main_text.toPlainText()
        self.main_text.setPlainText(text)
        vlayout.addWidget(self.main_text)

        self.open = qtw.QPushButton("Open")
        self.open.clicked.connect(self.open_clicked)
        self.save = qtw.QPushButton("Save")
        self.save.clicked.connect(self.save_clicked)
        self.quit = qtw.QPushButton("Quit")
        self.quit.clicked.connect(self.quit_clicked)
        hlayout.addWidget(self.open)
        hlayout.addWidget(self.save)
        hlayout.addWidget(self.quit)
        
        vlayout.addLayout(hlayout)


        widget = qtw.QWidget()
        widget.setLayout(vlayout)
        
        self.setCentralWidget(widget)
    
    def open_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt *.html)")
        print(filename)

    def save_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html)")
        print(filename)

    def quit_clicked(self):
        button = QMessageBox.warning(self,"Hold up", "Are you sure you want to quit", QMessageBox.StandardButton.Ok| QMessageBox.StandardButton.Cancel)
        if button == QMessageBox.OK:
            self.close()

app = qtw.QApplication([])

window = MainWindow()
window.show()
app.exec()