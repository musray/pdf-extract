# coding: utf-8
import csv
from pyPdf import PdfFileWriter, PdfFileReader

lst = []
csvfile = file('pages.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
	a = int(line[0])	
	lst.append(a)

csvfile.close() 

output1 = PdfFileWriter()
input1 = PdfFileReader(file("after.pdf", "rb"))

output2 = PdfFileWriter()
input2 = PdfFileReader(file("before.pdf", "rb"))

output3 = PdfFileWriter()

for i in lst:
	output1.addPage(input1.getPage(i-1))
        output2.addPage(input2.getPage(i-1))
        output3.addPage(input2.getPage(i-1))
        output3.addPage(input1.getPage(i-1))
# finally, write "output" to document-output.pdf
outputStream1 = file("after_extracted.pdf", "wb")
output1.write(outputStream1)

outputStream2 = file("before_extracted.pdf", "wb")
output2.write(outputStream2)

outputStream3 = file("cin.pdf", "wb")
output3.write(outputStream3)

outputStream1.close()
outputStream2.close()
outputStream3.close()

