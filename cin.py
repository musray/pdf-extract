# coding: utf-8
import csv
from pyPdf import PdfFileWriter, PdfFileReader

lst = []
csvfile = file('pages.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
	a = int(line[0])	
	lst.append(a)

print lst

csvfile.close() 

output = PdfFileWriter()
input1 = PdfFileReader(file("after.pdf", "rb"))

for i in lst:
	output.addPage(input1.getPage(i-1))

# finally, write "output" to document-output.pdf
outputStream = file("after_extracted.pdf", "wb")
output.write(outputStream)
outputStream.close()
