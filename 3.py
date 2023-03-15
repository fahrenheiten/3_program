from PyPDF2 import PdfReader,PdfWriter

reader = PdfReader(" ")
writer = PdfWriter( )

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("qwert")

with open("", "wb") as file:
    writer.write(file)