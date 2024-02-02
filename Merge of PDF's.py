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
