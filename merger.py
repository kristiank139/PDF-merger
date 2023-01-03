from pypdf import PdfMerger
import os

pdfs = []
for file in os.listdir():
    if file[-3:] == "pdf":
        pdfs.append(file)
        print(file)

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)
    print(pdf)

filename = input("\nEnter the naem for the file: ")
merger.write(f"{filename}.pdf")
merger.close()