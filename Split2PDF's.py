from PyPDF2 import PdfFileWriter, PdfFileReader
input_pdf = PdfFileReader("File Name")
output = PdfFileWriter()
output.addPage(input_pdf.getPage(0))
with open("first_page.pdf", "wb") as output_stream:
    output.write(output_stream)
