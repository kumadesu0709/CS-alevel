import PyQt6.QtWidgets as qtw
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QToolBar
import PyQt6.QtGui as qtg
import sys

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor")

        save_action = qtg.QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_clicked)

        open_action = qtg.QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_clicked)

        quit_action = qtg.QAction('\0Quit', self)
        quit_action.setShortcut('Ctrl+Q')
        quit_action.triggered.connect(self.quit_clicked)


        character_count = qtg.QAction('Character count', self)
        character_count.setShortcut('Ctrl+C')
        character_count.triggered.connect(self.count_character)


        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(character_count)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

        
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
        if filename:
            with open(filename, 'r') as text_file:
                text = text_file.read()
                self.main_text.setPlainText(text)

    def save_clicked(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html)")
        text = self.main_text.toPlainText()
        if filename:
            with open(filename, 'w') as text_file:
                text_file.write(text)

    def quit_clicked(self):
        button = QMessageBox.warning(self,"Hold up", "Are you sure you want to quit", QMessageBox.StandardButton.Ok| QMessageBox.StandardButton.Cancel)
        if button == QMessageBox.StandardButton.Ok:
            self.close()
    
    def count_character(self):
        text = self.main_text.toPlainText()
        length = len(text)
        QMessageBox.information(self, "CHaracter Length", f"The length of your text is: {length}", QMessageBox.StandardButton.Ok)





app = qtw.QApplication([])

window = MainWindow()
window.show()
app.exec()