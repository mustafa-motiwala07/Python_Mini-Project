#option 1
#import pdf2docx
from pdf2docx import Converter

pdf_file = input("Enter the file name:")
docx_file ='sample_1.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
