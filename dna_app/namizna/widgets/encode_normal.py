import namizna.app, namizna.sequencing as sequencing, namizna.style as style
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton, QLabel, QTextEdit, QGridLayout

#---------------------------------- Encode - Text - Widgets ---------------------------------------

class encode_normal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(encode_normal, self).__init__(parent)
        grid_layout = QGridLayout(self, alignment=QtCore.Qt.AlignCenter)
        
        self.setAcceptDrops(True)

        self.btn_back = QPushButton('<--')
        self.btn_back.setObjectName('BtnBack')
        self.btn_back.setFixedWidth(40)
        self.btn_back.setFixedHeight(35)

        self.user_input_form = QTextEdit()
        self.user_input_form.setAlignment(QtCore.Qt.AlignCenter)
        self.user_input_form.setFixedWidth(700)
        self.user_input_form.setFixedHeight(150)
        self.user_input_form.setMaximumWidth(600)
        self.user_input_form.setMaximumHeight(150)
        self.user_input_form.setPlaceholderText('Podaj besedilo')
        
        self.btn_action = QPushButton('Kodiraj')
        self.btn_action.setObjectName('BtnStatic1')
        self.btn_action.setFixedWidth(200)
        self.btn_action.setFixedHeight(45)
        self.btn_action.clicked.connect(self.normal_encoding_line_edit)

        self.btn_save_img = QPushButton('Dekodiraj')
        self.btn_save_img.setObjectName('BtnStatic2')
        self.btn_save_img.setFixedWidth(200)
        self.btn_save_img.setFixedHeight(45)
        self.btn_save_img.clicked.connect(self.normal_decoding_line_edit)

        self.user_result_form = QTextEdit()
        self.user_result_form.setAlignment(QtCore.Qt.AlignCenter)
        self.user_result_form.setFixedWidth(700)
        self.user_result_form.setFixedHeight(150)
        self.user_result_form.setMaximumWidth(600)
        self.user_result_form.setMaximumHeight(150)
        self.user_result_form.setPlaceholderText('Rezultat sekvenca DNK')

        self.btn_back.setStyleSheet(style.user_interface_btn_back_style)
        self.btn_action.setStyleSheet(style.user_interface_btn1_style)
        self.btn_save_img.setStyleSheet(style.user_interface_btn2_style)
        self.user_input_form.setStyleSheet(style.user_interface_te2_style)
        self.user_result_form.setStyleSheet(style.user_interface_te2_style)

        grid_layout.addWidget(self.btn_back, 0, 3)

        #rowSpan columnSpan
        grid_layout.addWidget(self.user_input_form, 1, 0, 1, 4)
        grid_layout.addWidget(self.btn_action, 2, 0)
        grid_layout.addWidget(self.btn_save_img, 2, 3)
        grid_layout.addWidget(self.user_result_form, 3, 0, 1, 4)
        
        self.setLayout(grid_layout)

#---------------------------------- Encoding - Decoding - Functions -----------------------------------------

    def normal_encoding_line_edit(self):
        user_text_input = self.user_input_form.toPlainText()
        dna_sequencing = sequencing.fromTextToDna(user_text_input)
        self.user_result_form.setText(dna_sequencing)

    def normal_decoding_line_edit(self):
        user_text_input = self.user_input_form.toPlainText()
        dna_sequencing = sequencing.DnaSequenceToText(user_text_input)
        self.user_result_form.setText(dna_sequencing)

    #def huffman_encoding_line_edit(self):
        #user_text_input = self.user_input_form.text()
        #dna_sequencing = sequencing.fromTextToDna(user_text_input)
        #self.user_result_form.setText(dna_sequencing)

    #def huffman_decoding_line_edit(self):
        #user_text_input = self.user_input_form.text()
        #dna_sequencing = sequencing.fromTextToDna(user_text_input)
        #self.user_result_form.setText(dna_sequencing)