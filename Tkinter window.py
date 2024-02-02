from tkinter import *
from tkinter import font   
from PIL import ImageTk, Image

window_root = Tk()

#window specifications
window_root.geometry("1000x1000")
window_root.minsize(300,300)
window_root.maxsize(800,800)
window_root.configure(background='White')
window_root.title("FILE CONVERTER SYSTEM")
tx= Label(text="Convert your Files!" , font={"Arial", 20, "bold"},  background="Red", foreground="White" , width="12", height="1", relief=SUNKEN, padx=20, pady=10)
tx.pack()

#file converter image
photo= PhotoImage(file="minipp.png")
z_label=Label(image=photo)
z_label.pack(anchor= "center")

#Pdf to word conversion
def p():
    from pdf2docx import Converter
    pdf_file = input("Enter the file name:")
    docx_file ='sample_1.docx'
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()
    
b1=Button(window_root, fg='red', text="Convert file to PDF", command=p)
b1.pack(side=TOP, anchor="center")

#Word to pdf conversion
def w():
    from docx2pdf import convert
    docx_file = input("Enter the name of the Word Document: ")
    convert(docx_file)

b2=Button(window_root, fg="red", text="Convert to Docx", command= w)
b2.pack(side=TOP, anchor="center")

#Pdf to excel conversion
def e():
    import tabula
    tabula.convert_into("xlsdemo1.pdf","xlsdemo1.csv",pages="all",output_format="csv")

b3=Button(window_root, fg='red', text="Convert pdf to excel", command=e)
b3.pack(side=TOP, anchor='Center')

#Merging two pdfs
def merger():
    from PyPDF2 import PdfFileMerger
    # create an instance of PdfFileMerger() class
    merger=PdfFileMerger()
    # Create a list with the file paths
    file1=input("Enter the first file:")
    file2=input("Enter the second file:")
    pdf_files = [file1,file2]
    # Iterate over the list of the file paths
    for pdf_file in pdf_files:
        # Append PDF files
        merger.append(pdf_file)
        # Write out the merged PDF file
        merger.write("merged_2_pages.pdf")
    merger.close()

b4=Button(window_root, fg='red', text="Merge two pdf files", command=merger)
b4.pack(side=TOP, anchor="center")

#To view a protected file
def passw():
    import re
    PASSWORD=input("Input your password")
    def check(x):
        while True:
            if (len(x)<5 or len(x)>10):
                break
            elif not re.search("[0-9]",x):
                break
            elif not re.search("[a-z]",x):
                break
            elif not re.search("[@&%]",x):
                break
            elif not re.search("[A-Z]",x):
                break
            elif re.search("\s",x):
                break
            else:
                print("Valid Password")
            break
        if False:
            print("Not a valid Password")
        print(check(PASSWORD))

b5=Button(window_root, fg='red', text="View the File", command=passw)
b5.pack(side=TOP, anchor='center')


window_root.mainloop()
