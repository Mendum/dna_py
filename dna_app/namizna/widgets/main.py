import namizna.app, namizna.sequencing as sequencing, namizna.style as style
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QPushButton, QLabel, QTextEdit, QGridLayout, QToolBar, QToolButton

#---------------------------------- Main - widgets -----------------------------------------

class main(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        grid_layout = QGridLayout(self, alignment=QtCore.Qt.AlignCenter)
        
        self.btn_normal_encoding = QPushButton('Navadno')
        self.btn_normal_encoding.setFixedWidth(200)
        self.btn_normal_encoding.setFixedHeight(35)

        self.btn_huffman_encoding = QPushButton('Zgosceno')
        self.btn_huffman_encoding.setFixedWidth(200)
        self.btn_huffman_encoding.setFixedHeight(35)
        
        self.btn_file_encoding = QPushButton('Slika')
        self.btn_file_encoding.setFixedWidth(200)
        self.btn_file_encoding.setFixedHeight(35)

        self.lb_hello = QLabel('Dobrodosli', self)
        self.lb_hello.setFixedWidth(700)
        self.lb_hello.setFixedHeight(300)
        self.lb_hello.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_hello.setStyleSheet(style.user_interface_lb_welcome)

        self.btn_normal_encoding.setStyleSheet(style.user_interface_btn_style)
        self.btn_huffman_encoding.setStyleSheet(style.user_interface_btn_style)
        self.btn_file_encoding.setStyleSheet(style.user_interface_btn_style)

        grid_layout.addWidget(self.btn_normal_encoding, 0, 0)
        grid_layout.addWidget(self.btn_huffman_encoding, 0, 1)
        #grid_layout.addWidget(self.btn_huffman_encoding, 0, 1, 2, 1)
        grid_layout.addWidget(self.btn_file_encoding, 0, 2)
        grid_layout.addWidget(self.lb_hello, 1, 0, 3, 3)

        #tool_bar.addWidget(tool_bar_button_encode)
        #tool_bar.addWidget(tool_bar_button_compressed)
        #tool_bar.addWidget(tool_bar_button_file)
        
        self.setLayout(grid_layout)
        #self.connect(self.btn_normal_encoding, QtCore.SIGNAL('clicked()'), self.normal_encoding_line_edit)
        #self.connect(self.btn_file_encoding, QtCore.SIGNAL('clicked()'), self.image_encoding_line_edit)