import requests
from os import listdir
from fpdf import FPDF
import sys
def drawProgressBar(percent, barLen = 20):
    sys.stdout.write("\r")
    progress = ""
    for i in range(barLen):
        if i < int(barLen * percent):
            progress += "="
        else:
            progress += " "
    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent))
    sys.stdout.flush()

path = "/home/pc/econtent/temp/"
img_path = "http://econtent.edu.mn/content/12rangi/eng8/pagetom/"
page_count = 198
print("Merge pages")
imagelist = listdir(img_path) 
pdf = FPDF('P','mm','A4')
x,y,w,h = 0,0,200,250
for j in range(1,page_count,1):
    image ="p%20" + str(j) + ".jpg"
    drawProgressBar(j*100/page_count,20)
    pdf.add_page()
    pdf.image(path+image,x,y,w,h)
print("\ncreating pdf")
pdf.output("book.pdf","F")
print("\ndone.")

