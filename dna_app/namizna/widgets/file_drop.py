import namizna.app, namizna.sequencing as sequencing, namizna.style as style
import tkinter as tk
from tkinter import filedialog
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton, QLabel, QTextEdit, QGridLayout
#---------------------------------- File - Drop - Widgets ---------------------------------------

class file_drop(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(file_drop, self).__init__(parent)
        grid_layout = QGridLayout(self, alignment=QtCore.Qt.AlignCenter)
        
        self.setAcceptDrops(True)

        self.btn_back = QPushButton('Meni')
        self.btn_back.setObjectName('BtnBack')
        self.btn_back.setFixedWidth(200)
        self.btn_back.setFixedHeight(35)

        self.file_drop = QTextEdit()
        self.file_drop.setAlignment(QtCore.Qt.AlignCenter)
        self.file_drop.setFixedWidth(700)
        self.file_drop.setFixedHeight(150)
        self.file_drop.setMaximumWidth(600)
        self.file_drop.setMaximumHeight(150)
        self.file_drop.setPlaceholderText('Povleci datoteko')
        
        self.btn_encode = QPushButton('Kodiraj')
        self.btn_encode.setObjectName('BtnStatic1')
        self.btn_encode.setFixedWidth(200)
        self.btn_encode.setFixedHeight(45)
        self.btn_encode.clicked.connect(self.image_encoding)

        self.btn_decode = QPushButton('Dekodiraj')
        self.btn_decode.setObjectName('BtnStatic2')
        self.btn_decode.setFixedWidth(200)
        self.btn_decode.setFixedHeight(45)
        self.btn_decode.clicked.connect(self.image_decoding)

        self.btn_save = QPushButton('Shrani')
        self.btn_save.setObjectName('BtnSave')
        self.btn_save.setFixedWidth(200)
        self.btn_save.setFixedHeight(45)
        self.btn_save.clicked.connect(self.save_file)

        self.file_drop_result = QTextEdit()
        self.file_drop_result.setAlignment(QtCore.Qt.AlignCenter)
        self.file_drop_result.setFixedWidth(700)
        self.file_drop_result.setFixedHeight(150)
        self.file_drop_result.setMaximumWidth(600)
        self.file_drop_result.setMaximumHeight(150)
        self.file_drop_result.setPlaceholderText('Rezultat sekvenca DNK')

        self.btn_back.setStyleSheet(style.user_interface_btn_back_style)
        self.btn_encode.setStyleSheet(style.user_interface_btn1_style)
        self.btn_decode.setStyleSheet(style.user_interface_btn2_style)
        self.btn_save.setStyleSheet(style.user_interface_btn3_style)
        self.file_drop.setStyleSheet(style.user_interface_te1_style)
        self.file_drop_result.setStyleSheet(style.user_interface_te2_style)

        grid_layout.addWidget(self.btn_back, 0, 3)

        #rowSpan columnSpan
        grid_layout.addWidget(self.file_drop, 1, 0, 1, 4)
        grid_layout.addWidget(self.btn_encode, 2, 0)
        grid_layout.addWidget(self.btn_decode, 2, 1)
        grid_layout.addWidget(self.btn_save, 2, 3)
        grid_layout.addWidget(self.file_drop_result, 3, 0, 1, 4)
        
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

        file_path = filedialog.asksaveasfilename(initialfile = 'sekvenca_dnk_slika.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
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