# coding: utf-8
import csv
from PyPDF2 import PdfFileWriter, PdfFileReader

lst = []
csvfile = file('pages.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
	a = int(line[0])	
	lst.append(a)

csvfile.close() 

input1 = PdfFileReader(file("before.pdf", "rb"))
input2 = PdfFileReader(file("after.pdf", "rb"))
output = PdfFileWriter()


for i in lst:
	output.addPage(input1.getPage(i-1))

for i in lst:
        output.addPage(input2.getPage(i-1))

outputStream1 = file(r"Merged.pdf", "wb")
output.write(outputStream1)
outputStream1.close()
