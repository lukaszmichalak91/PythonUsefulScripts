import os

from PyPDF2 import PdfMerger

merger = PdfMerger()

allPdfs = os.listdir(os.getcwd())

for pdfs in allPdfs:
    print(pdfs)
    if pdfs.endswith('.pdf'):
        merger.append(pdfs)

merger.write("merged.pdf")
merger.close()
