from PIL import Image, ImageDraw
import math
image = Image.new("RGB", (200,200)) #hue, saturation, value
pixels = image.load()
angle = 0
while angle < 2 * (math.pi):
    r = 80
    x = r * math.cos(angle) + 100
    y = r * math.sin(angle) + 100
    pixels[x,y] = (255,255,255)
    angle += 0.01

image.show()

draw = ImageDraw.Draw(image)
draw.ellipse([(100,50),(150,100)],fill = (255,255,255))
pixels = image.load()
for y in range(200):
    for x in range(200):
        if pixels [x,y] == (255,255,255):
            pixels[x,y] = (x+50,y+50,255)
image.show()