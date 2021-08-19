import namizna.app, namizna.sequencing as sequencing, namizna.style as style
from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QLabel, QTextEdit, QGridLayout

#---------------------------------- Encode - Text - Widgets ---------------------------------------

class encode_normal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(encode_normal, self).__init__(parent)
        grid_layout = QGridLayout(self)
        
        self.user_input_label = QLabel()
        self.user_input_label.setText('Vhodni podatki')

        self.user_result_label = QLabel()
        self.user_result_label.setText('Rezultat')

        self.btn_back = QPushButton('Back')
        self.btn_back.setFixedWidth(50)
        self.btn_back.setFixedHeight(35)

        self.user_input_form = QTextEdit()
        self.user_input_form.setFixedWidth(200)
        self.user_input_form.setFixedHeight(200)

        self.user_result_form = QTextEdit()
        self.user_result_form.setFixedWidth(200)
        self.user_result_form.setFixedHeight(200)
        self.user_result_form.setReadOnly(True)

        self.setAcceptDrops(True)

        self.file_drop = QLabel()
        self.file_drop.setFixedWidth(200)
        self.file_drop.setFixedHeight(200)
        #self.file_drop.setPlaceholderText('Povleci sliko')
        self.file_drop.setStyleSheet('color: red')
        self.file_drop.setMaximumWidth(200)
        self.file_drop.setMaximumHeight(200)
        self.file_drop.setWordWrap(True)
        #https://www.codershubb.com/image-drag-and-drop-using-pyqt5/

        self.user_input_form.setStyleSheet(style.user_interface_le_style)
        self.user_result_form.setStyleSheet(style.user_interface_le_style)
        self.file_drop.setStyleSheet(style.user_interface_lb_style)

        grid_layout.addWidget(self.user_input_label, 1, 0)
        grid_layout.addWidget(self.user_result_label, 1, 2)
        grid_layout.addWidget(self.btn_back, 1, 3)

        grid_layout.addWidget(self.user_input_form, 2, 0)
        grid_layout.addWidget(self.user_result_form, 2, 1)

        self.file_drop_path = self.file_drop
        grid_layout.addWidget(self.file_drop_path, 2, 2)
        
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