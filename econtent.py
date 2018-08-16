import requests
for i in range(1,101,1):
    image_url =" http://econtent.edu.mn/content/12rangi/mzui7/pagetom/p%20(" + str(i) + ").jpg"
    img_data = requests.get(image_url).content
    with open("mzui/mzui"+str(i)+".jpg", 'wb') as handler:
        handler.write(img_data)
