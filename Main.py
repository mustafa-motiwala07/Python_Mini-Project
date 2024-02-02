from base64 import b64encode
from tkinter import *
from tkinter import font   
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from PyPDF2 import PdfFileMerger, PdfFileReader
import re
from pathlib import Path
import os
import subprocess
import tabula
from pdf2docx import Converter
from docx2pdf import convert
from PyPDF2 import PdfFileWriter, PdfFileReader

proot= Tk()
proot.title("Validation Window")
proot.geometry("800x800")
proot.maxsize(800,800)
proot.minsize(500,500)
px=Label(proot, text="ENTRY GATE", font=("Calibri",15, "italic"), bg="White", fg="Black", width=12, height=1, relief=SUNKEN, padx= 20, pady=10)
px.pack()
key1=Label(proot, text='To convert your files, Enter the Passkey:', font=("Calibri", 15))
key1.pack()
pa1= StringVar() 
pa1e= Entry(proot,textvariable=pa1)
pa1e.pack()

photo= PhotoImage(file="Trust(1).png")
z_label=Label(image=photo)
z_label.pack()

def check():
    a=pa1.get()
    pattern = r"\A(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@%&])[A-Za-z\d@%&]{5,10}$"
    x = re.search(pattern,a)
    
    if x:
        window_root = Tk()
        #window specifications
        window_root.geometry("1000x1000")
        window_root.minsize(300,300)
        window_root.maxsize(800,800)
        window_root.configure(background='Grey')
        window_root.title("FILE CONVERTER SYSTEM")
        tx= Label(window_root,text="Convert your Files!" , font={"Arial", 20, "bold"},  background="Red", foreground="White" , width="12", height="1", relief=SUNKEN, padx=20, pady=10)
        tx.pack()
        window_root.mainloop()
        
        #Pdf to word conversion
        def p():
            docx_file='Converted Word file.docx'
            filp = askopenfile(filetypes=[('Pdf Files', '*.pdf')])
            pv = Converter(filp.name, r'C:\Users\lenovo\Desktop\Mini project python')
            pv.convert(docx_file)
            showinfo("Converted to Word")
            pv.close()
        frame1 = Frame(window_root)
        frame1.pack( padx=20, pady = 20)
        b1=Button(frame1, fg='red', text="Convert Pdf file to Word file", relief="sunken", command=p)
        b1.pack(side=TOP, padx=10, pady=10)
        
        #Word to pdf conversion
        def w():
            filw = askopenfile(filetypes=[('Word Files', '*.docx')])
            wv= convert(filw.name, r'C:\Users\lenovo\Desktop\Mini project python')
            showinfo("Converted to pdf")
            wv.close()
        frame2 = Frame(window_root)
        frame2.pack(padx=20, pady = 20)
        b2=Button(frame2, fg="red", text="Convert Word file to Pdf file", relief="sunken", command= w)
        b2.pack(side=TOP, padx=10, pady=10)
        
        #Pdf to excel conversion
        def e():
            tabula.convert_into("XYZ.pdf","Converted Excel file.csv",pages="all",output_format="csv")
            showinfo("Converted to Excel")
        frame3 = Frame(window_root)
        frame3.pack( padx=20, pady = 20)
        b3=Button(frame3 , fg='red', text="Convert Pdf file to Excel file", relief="sunken", command=e)
        b3.pack(side=TOP, padx=10, pady=10)
        
        #Merging two pdfs
        def m():
            #Create and instance of PdfFileMerger() class
            merger = PdfFileMerger()
            #Create a list with file names
            pdf_files = ['ABC.pdf', 'XYZ.pdf']
            #Iterate over the list of file names
            for pdf_file in pdf_files:
                #Append PDF files
                merger.append(pdf_file)
            #Write out the merged PDF
            merger.write("Merged Pdf file.pdf")
            showinfo("Merged your pdfs")
            merger.close()
        
        frame4 = Frame(window_root)
        frame4.pack(padx=20, pady = 20)
        b4=Button(frame4, fg="red", text="Merge two Pdf files", relief="sunken", command=m )
        b4.pack(side=TOP, padx=10, pady=10)
        
        # Converting image to PDF
        def i():
            filename = 'minipp.png'
            image = Image.open(filename)
            
            if image.mode == "RGBA":
                image = image.convert("RGB")
            
            output = "Your converted image.pdf"
            if not os.path.exists(output):
                image.save(output,"PDF",resolution=100.0)
            
            showinfo("Converted Image to Pdf")
            
        frame5= Frame(window_root)
        frame5.pack(padx = 20, pady = 20)
        b5=Button(frame5, fg="red", text="Convert Image to PDF file", relief="sunken",command=i)
        b5.pack(side=TOP, padx=10, pady=10)
        
        
        # Spliting of two PDF's
        def s():
            input_pdf = PdfFileReader("merged_file.pdf")
            output = PdfFileWriter()
            output.addPage(input_pdf.getPage(0))
            with open("Split Pdf file.pdf", "wb") as output_stream:
                output.write(output_stream)
            showinfo("Split successfully")
        
        frame6= Frame(window_root)
        frame6.pack(padx = 20, pady = 20)
        b6=Button(frame6, fg="red", text="Split a PDF file", relief="sunken",command=s)
        b6.pack(side=TOP, padx=10, pady=10)
        
        #Conversion pdf to pptx
        def ptx():
            list_files = subprocess.run([ "pdf2pptx", "ABC.pdf" ])
            showinfo("The files are converted successfully")
        
        frame7= Frame(window_root)
        frame7.pack(padx = 20, pady = 20)
        b7 = Button(frame7, fg="red", text ="Convert PDF file to pptx file", relief="sunken",command=ptx)
        b7.pack(side=TOP, padx=10, pady=10)

        window_root.mainloop()
    else:
        showinfo("INVALID")
        
pb=Button(proot, text='Validate', command=check)
pb.pack()

proot.mainloop()
