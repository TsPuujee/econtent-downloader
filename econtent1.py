from os import listdir
from fpdf import FPDF

path = "/home/pc/mzui/" # get the path of images

imagelist = listdir(path) # get list of all images

pdf = FPDF('P','mm','A4') # create an A4-size pdf document 

x,y,w,h = 0,0,200,250

for i in range(1,101,1):
    image ="mzui" + str(i) + ".jpg"
    pdf.add_page()
    pdf.image(path+image,x,y,w,h)

pdf.output("mzui12.pdf","F")
