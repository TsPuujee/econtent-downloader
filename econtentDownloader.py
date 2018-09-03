import requests
from os import listdir
from fpdf import FPDF
import sys
import os
import glob
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
img_path = "http://econtent.edu.mn/content/12rangi/eng8/pagetom/p%20"
page_count = 198
print("Downloading pages...")
for i in range(1,page_count,1):
    image_url = img_path + "(" + str(i) + ").jpg"
    try:
        img_data = requests.get(image_url).content
    except requests.ConnectionError, e:
        print (e)
    drawProgressBar(i*100/page_count,20)
    with open("temp/img"+str(i)+".jpg", 'wb') as handler:
        handler.write(img_data)
drawProgressBar(100,20)
print("\nDownloading pages done.")
print("Merging pages...")
imagelist = listdir(path) 
pdf = FPDF('P','mm','A4')
x,y,w,h = 0,0,200,250
for j in range(1,page_count,1):
    image ="img" + str(j) + ".jpg"
    drawProgressBar(j*100/page_count,20)
    pdf.add_page()
    pdf.image(path+image,x,y,w,h)
drawProgressBar(100,20)
print("\ncreating pdf")
pdf.output("book.pdf","F")
files = glob.glob(path + '*')
for f in files:
    os.remove(f)
print("\ndone.")

