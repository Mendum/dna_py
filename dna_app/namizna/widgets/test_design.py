import namizna.app, namizna.sequencing as sequencing, namizna.style as style
import tkinter as tk
from tkinter import filedialog
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton, QLabel, QTextEdit, QGridLayout
#---------------------------------- File - Drop - Widgets ---------------------------------------

class test_design(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(test_design, self).__init__(parent)
        grid_layout = QGridLayout(self, alignment=QtCore.Qt.AlignCenter)
        
        self.setAcceptDrops(True)

        self.btn_00 = QPushButton('0Menu0')
        self.btn_00.setObjectName('BtnBack')
        self.btn_00.setFixedWidth(69)
        self.btn_00.setFixedHeight(35)
        self.btn_00.setStyleSheet(style.user_interface_btn_back_style)


        grid_layout.addWidget(self.btn_00, 0, 0)

        #rowSpan columnSpan
        #grid_layout.addWidget(self.file_drop, 1, 0, 1, 4)
        #grid_layout.addWidget(self.btn_encode, 2, 0)
        #grid_layout.addWidget(self.btn_decode, 2, 1)
        #grid_layout.addWidget(self.btn_save, 2, 3)
        #grid_layout.addWidget(self.file_drop_result, 3, 0, 1, 4)
        
        self.setLayout(grid_layout)

        #self.connect(self.btn_action, QtCore.SIGNAL('clicked()'), self.image_encoding())

#---------------------------------- Encoding - Decoding - Functions -----------------------------------------
    def image_encoding(self):
        file_path = self.file_drop.toPlainText()
        dna_sequencing = sequencing.fromImageToDna(file_path)
        self.file_drop_result.setText(dna_sequencing)
        
    def image_decoding(self):
        dna_sequence = self.file_drop.toPlainText()
        sequencing.DnaSequenceToImage(dna_sequence)
        #image_base_64 = sequencing.DnaSequenceToImage(dna_sequence)
        #print(image_base_64)
        #self.user_result_form.setText(image_base_64)
    
    def save_file(self):
        file_data = self.file_drop_result.toPlainText()
        if file_data is None:
            return

        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.asksaveasfilename(initialfile = 'sequence_dna_image.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file_path is None:
            return

        with open(file_path, 'w') as f:
            f.write(file_data)

#---------------------------------- Drag - Drop - Functions -----------------------------------------

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(QtCore.Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_file_path(file_path)

            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(QtCore.Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_file_path(file_path)

            event.accept()
        else:
            event.ignore()

    def set_file_path(self, file_path):
        self.file_drop.setText(file_path)