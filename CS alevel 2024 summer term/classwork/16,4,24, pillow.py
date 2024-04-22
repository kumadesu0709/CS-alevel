from PIL import Image

image = Image.open("landscape.png") #load an image
"""image.show() #display the image"""

"""print(f'Formate:{image.format}, size: {image.size}, mode:{image.mode}')#display some information about the image, RGBA means red green alpha, whdre alpha is how opaque the colour is"""

"""new_image = Image.new ("RGB", (255,255))

pixels = new_image.load() # creates a PixelAccess object which allows you to read and modify individual pixels

for y in range (255):
    for x in range(255):
        pixels[x,y] = (x, y, 255)
        print(f'x:{x}, y:{y}, RBG: {pixels[x,y]}')

new_image.show()"""

"""new_image = Image.new("RGB", (512,346))
orig = image.load()
pixels = new_image.load()
for y in range (346):
    for x in range(512):
        r,g,b = orig[x,y][0],orig[x,y][1],orig[x,y][2]
        pixels[x,y] = (r, 0, 0)
new_image.show()"""

"""new_image = Image.new("RGB", (512,346))
orig = image.load()
pixels = new_image.load()
for y in range (346):
    for x in range(512):
        r,g,b = orig[x,y][0],orig[x,y][1],orig[x,y][2]
        average = 0
        average = r + g + b
        average = average // 3
        pixels[x,y] = (average, average, average)
new_image.show()"""

new_image = Image.new("RGB", (512,346))
orig = image.load()
pixels = new_image.load()
for y in range (346):
    for x in range(512):
        r,g,b = orig[x,y][0],orig[x,y][1],orig[x,y][2]
        pixels[512 - x - 1, y] = orig[x,y]
new_image.show()