import tkinter as tk
import os
from pathlib import Path
from tkinter import ttk, filedialog    
    
allowed_file_types_text = (
    ('text file', '*.txt')
)
 
allowed_file_types_image = (
    ('Image', '*.png'),
    ('Image', '*.jpg'),
    ('Image', '*.jpeg'),
    ('text file', '*.txt')
)


def read_file_lines(file_path):
    file_data = ''
    
    with open(file_path) as file:
        while (line := file.readline().rstrip()):
            file_data += line

    return file_data


def open_file(QTextEdit, type):
    root = tk.Tk()
    root.withdraw()

    if(type == 'txt'):
        file_path = filedialog.askopenfilename(filetypes=(('Text Files', '*.txt')))
    elif (type == 'img'):
        print('a')
        #file_path = filedialog.askopenfilename(filetypes=[('Image', '*.png'), ('Image', '*.jpg'), ('Image', '*.jpeg'), ('Text Files', '*.txt')])
    else:
        err = 'Wrong type given'
        return err
    
    file_size = os.path.getsize(file_path)

    if (file_size < 20000):
        file_data = read_file_lines(file_path)
    
    QTextEdit.setText(file_data)


def save_file(self):
    file_data = ''

    file_data = self.user_result_form.toPlainText()
    if file_data is None:
        return
    
    root = tk.Tk()
    root.withdraw()

    #if(type == 'txt'):
    file_path = filedialog.asksaveasfilename(initialfile = 'sequence_dna_image.txt',filetypes=(('Text Files', '*.txt')))
    if file_path is None:
        return
    #elif (type == 'img'):
        #print('a')
        #file_path = filedialog.asksaveasfilename(initialfile = 'sequence_dna_image.png',filetypes=[('Image', '*.png'), ('Image', '*.jpg'), ('Image', '*.jpeg'), ('Ttext Files', '*.txt')])
        #if file_path is None:
            #return
    #else:
    #    err = 'Wrong type given'
    #    return err

    with open(file_path, 'w') as f:
        f.write(file_data)