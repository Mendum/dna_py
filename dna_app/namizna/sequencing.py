import re
import sys
import base64
from io import StringIO
from PIL import Image

# ===============================
# text v DNA

def fromTextToDna(u_input):
    bytes_user_input =''.join(format(ord(znak), '08b') for znak in u_input)
    dna_sequence = fromBytesToDna(bytes_user_input)
    
    return dna_sequence

def fromBytesToDna(user_input):
    temp_bytes = ''
    temp_dna_sequence = ''
    i = 0

    while i < len(user_input)-1:
        temp_bytes += str(user_input[i]) + str(user_input[i + 1])
        temp_dna_sequence += setSugarValue(temp_bytes)
        temp_bytes = ''
        i += 2
    
    return temp_dna_sequence

def setSugarValue(bytes_to_sugar):
    if(bytes_to_sugar == '00'):
        return 'C'
    if(bytes_to_sugar == '01'):
        return 'T'
    if(bytes_to_sugar == '10'):
        return 'A'
    if(bytes_to_sugar == '11'):
        return 'G'

# ===============================
# DNA v text

def DnaSequenceToText(user_input):

    decoded_dna_sequence = fromBitiToText(user_input)
    #print(decoded_dna_sequence)
    ascii_string = "".join([chr(int(binary, 2)) for binary in decoded_dna_sequence[:-1].split(" ")])

    return ascii_string

def fromBitiToText(user_input):
    decoded_sequence = ''
    j = 0
    # preveri kaj so GTAC
    
    print(decoded_sequence)
    for simple_sugar in user_input:
        j += 1

        decoded_sequence += fromDnaToBytes(simple_sugar)

        if(j % 4 == 0):
            decoded_sequence += ' '
            j = 0     

    return decoded_sequence

def fromDnaToBytes(dna_value):
    if(dna_value == 'C'):
        return '00'
    if(dna_value == 'T'):
        return '01'
    if(dna_value == 'A'):
        return '10'
    if(dna_value == 'G'):
        return '11'


# ===============================
# image v DNA
def fromImageToDna(image_path):

    user_image = Image.open(image_path)
    user_image.save('C:\\Users\\Bobby\\Desktop\\slikca.png', 'PNG', optimize=True, quality=75)

    #https://stackoverflow.com/questions/30771652/how-to-perform-jpeg-compression-in-python-without-writing-reading
    #https://stackoverflow.com/questions/10607468/how-to-reduce-the-image-file-size-using-pil
    with open('C:\\Users\\Bobby\\Desktop\\slikca.png', 'rb') as img_file:
        b64_string  = base64.b64encode(img_file.read())
    
    print(b64_string)
    #base64_decoded = base64.decodebytes(b64_string)
    bytes_image = ''.join(format(znak, '08b') for znak in b64_string)
    dna_sequence = fromBytesToDna(bytes_image)
    return dna_sequence

def DnaSequenceToImage(user_input):

    decoded_dna_sequence = fromBitiToText(user_input)
    print(decoded_dna_sequence)
    
    #base64_decoded = base64.decodebytes(b64_string)
    b64_string = "".join([chr(int(binary, 2)) for binary in decoded_dna_sequence[:-1].split(" ")])
    img_data = base64.b64decode(b64_string)
    with open('C:\\Users\\Bobby\\Desktop\\test.png', 'wb') as f:
        f.write(img_data)

#
#video 
#https://stackoverflow.com/questions/17686698/python-how-to-read-a-video-file-as-binary-data#17686777