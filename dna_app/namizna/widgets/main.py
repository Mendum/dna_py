import namizna.app, namizna.sequencing as sequencing, namizna.style as style
from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QLabel, QTextEdit, QGridLayout

#---------------------------------- Main - widgets -----------------------------------------

class main(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        grid_layout = QGridLayout(self)
        
        self.btn_normal_encoding = QPushButton('Navadno')
        self.btn_normal_encoding.setFixedWidth(200)
        self.btn_normal_encoding.setFixedHeight(35)

        self.btn_huffman_encoding = QPushButton('Zgosceno')
        self.btn_huffman_encoding.setFixedWidth(200)
        self.btn_huffman_encoding.setFixedHeight(35)
        
        self.btn_file_encoding = QPushButton('Slika')
        self.btn_file_encoding.setFixedWidth(200)
        self.btn_file_encoding.setFixedHeight(35)

        self.btn_normal_encoding.setStyleSheet(style.user_interface_btn_style)
        self.btn_huffman_encoding.setStyleSheet(style.user_interface_btn_style)
        self.btn_file_encoding.setStyleSheet(style.user_interface_btn_style)

        grid_layout.addWidget(self.btn_normal_encoding, 0, 0)
        grid_layout.addWidget(self.btn_huffman_encoding, 0, 1)
        #grid_layout.addWidget(self.btn_huffman_encoding, 0, 1, 2, 1)
        grid_layout.addWidget(self.btn_file_encoding, 0, 2)
        
        self.setLayout(grid_layout)
        #self.connect(self.btn_normal_encoding, QtCore.SIGNAL('clicked()'), self.normal_encoding_line_edit)
        #self.connect(self.btn_file_encoding, QtCore.SIGNAL('clicked()'), self.image_encoding_line_edit)