from PIL import Image
image = Image.open("IMG_3341.JPG")
image = image.convert("HSV")
image = image.resize((170,100))
pixels = image.load()
showing_image = ""
for y in range(100):
    for x in range(170):
        v = pixels[x,y][2]
        if v in range(0,64):
            showing_image = showing_image + " "
        if v in range(64,128):
            showing_image = showing_image + "."
        if v in range(128,192):
            showing_image = showing_image + "="
        if v in range(192,256):
            showing_image = showing_image + "#"
        if x == 169:
            showing_image = showing_image + "\n"
print(showing_image)