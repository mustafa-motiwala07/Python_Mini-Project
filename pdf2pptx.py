import subprocess

list_files = subprocess.run(["pdf2pptx","File Name"])
print("The files are converted successfully")
