from PIL import Image

def save_otl_image(image: Image.Image, filename: str):
    pixels = image.load()
    width, height = image.size
    with open(filename, 'w') as file:
        file.write(f'{width} {height}')
        for y in range(height):
            for x in range(width):
                r,g,b = pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]
                file.write(f'\n{r} {g} {b}')
    print(f'Image saved to OTL format.\nSize: {width}x{height}\nFilename: {filename}')


def load_otl_image(filename: str) -> Image.Image:
    with open(filename, 'r') as file:
        meta_data_str = file.readline().strip().split(' ')
        width = int(meta_data_str[0])
        height = int(meta_data_str[1])
        return_image = Image.new('RGB', (width,height))
        pixelData = []
        for line in file:
            string = line.strip().split(' ')
            if len(string) == 2:
                 pass
            else:
                r,g,b = int(string[0]),int(string[1]),int(string[2])
                new = (r,g,b)
                pixelData.append(new)
        return_image.putdata(pixelData)
    return return_image

loaded_image = load_otl_image('image.otl')
loaded_image.save("testing1.png")

saved_image = save_otl_image(Image.open("rose1.jpg"),"rose1.otl")

loaded_image = load_otl_image('rose1.otl')
loaded_image.save('testing2.png')
