import requests
for i in range(1,198,1):
    image_url =" http://econtent.edu.mn/content/12rangi/eng8/pagetom/p%20(" + str(i) + ").jpg"
    img_data = requests.get(image_url).content
    with open("mzui/mzui"+str(i)+".jpg", 'wb') as handler:
        handler.write(img_data)
