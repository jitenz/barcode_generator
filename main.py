# installing the library
pip install python-barcode

# importing necessary library
import barcode
from barcode.writer import ImageWriter
from PIL import Image

# make sure numeric nos. to be used to generate the code
# 11 digit nos can only be used to generate the code

number = input("Enter the code to generate the barcode : ")
barcode_format = barcode.get_barcode_class('upc')
my_barcode = barcode_format(number, writer=ImageWriter())

#saving the generated barcode
my_barcode.save('generated_barcode')

# opening the saved barcode image
Image.open('generated_barcode')