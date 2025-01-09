from PIL import Image
orig_image = Image.open("green screen.png")
school = Image.open("abingdon school.png")
orig_image = orig_image.convert("HSV")
school = school.convert("HSV")
school = school.resize((2326,1448))
pixels = orig_image.load()
school_pixels = school.load()
testing = Image.open("testing.png")
testing = testing.convert("HSV")
test = testing.load()
print(f"{testing.size}, {pixels[0,0]}")

def tolerance(value, lower_tolerate, upper_tolerate):
    ret_list = []
    for i in range(value-lower_tolerate, value+upper_tolerate):
        ret_list.append(i)
    return ret_list
h = tolerance(85,60,90)
s = tolerance(74,40,90)
v = tolerance(216,50,49)
for y in range(1448):
    for x in range(2326):
        h1,s1,v1 = pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]
        if h1 in h and s1 in s and v1 in v:
            pixels[x,y] = school_pixels[x,y]
orig_image.show()