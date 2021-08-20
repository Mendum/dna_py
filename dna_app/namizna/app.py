import sys
import namizna.widgets.main as widget_main
import namizna.widgets.encode_normal as widget_encode_normal
import namizna.widgets.file_drop as widget_file_drop
import namizna.style as style
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMenu, QGridLayout, QVBoxLayout, QToolBar, QToolButton, QPlainTextEdit
from PySide6.QtGui import QIcon

#---------------------------------- Application ---------------------------------------

class dna_app(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle('Diplomsko_delo_Blaz_Vidovic')
        #self.setAligment(QtCore.AlignCenter)
        self.setGeometry(1000, 100, 900, 600)
        
        user_interface_main_window_style = (
            'background-color: #1e1f25;'
            'color: #ccced1;' # primary_color
           #'color: #61656a;' # secondary_colo

           'font-size: 16px;' 
        )
        
        self.setStyleSheet(user_interface_main_window_style)

        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        central_widget_main = widget_main.main(self)
        self.central_widget.addWidget(central_widget_main)
        
        central_widget_main.btn_normal_encoding.clicked.connect(self.change_central_widget_encode)
        central_widget_main.btn_file_encoding.clicked.connect(self.change_central_widget_file_drop)

    def change_central_widget_encode(self):
        central_widget_encode_normal = widget_encode_normal.encode_normal(self)
        self.central_widget.addWidget(central_widget_encode_normal)
        self.central_widget.setCurrentWidget(central_widget_encode_normal)

        central_widget_encode_normal.btn_back.clicked.connect(self.change_central_back_main)

        
    def change_central_widget_file_drop(self):
        central_widget_file_drop = widget_file_drop.file_drop(self)
        self.central_widget.addWidget(central_widget_file_drop)
        self.central_widget.setCurrentWidget(central_widget_file_drop)

        central_widget_file_drop.btn_back.clicked.connect(self.change_central_back_main)
        

    def change_central_back_main(self):
        central_widget_main = widget_main.main(self)
        self.central_widget.addWidget(central_widget_main)
        self.central_widget.setCurrentWidget(central_widget_main)
        
        central_widget_main.btn_normal_encoding.clicked.connect(self.change_central_widget_encode)
        central_widget_main.btn_file_encoding.clicked.connect(self.change_central_widget_file_drop)
        
#---------------------------------- main -----------------------------------------

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main_window = dna_app()
    main_window.show()
    sys.exit(app.exec_())

#---------------------------------- TODO: -----------------------------------------

#https://learndataanalysis.org/how-to-implement-image-drag-and-drop-feature-pyqt5-tutorial/
#https://www.geeksforgeeks.org/pyqtgraph-getting-maximum-width-height-of-image-view/
#https://stackoverflow.com/questions/44712193/how-to-get-filepath-from-droped-file-with-pyqt5

#https://coderslegacy.com/python/pyqt5-qlabel-widget/
#https://stackoverflow.com/questions/17466046/qtextedit-vs-qplaintextedit


# preveri file type

# ko stisnes na gumb preveri prazna polja

