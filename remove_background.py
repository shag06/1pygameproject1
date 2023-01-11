from PIL import Image


def remove(file_in):
    print(file_in)
    img = Image.open(file_in)
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]
            if r > 240 and b > 240 and g > 240:
                r = g = b = 255
                a = 0
            pixels[x, y] = r, g, b, a
    img.save(file_in)


all_files = [f'face{i}.png' for i in range(4)] + [f'back{i}.png' for i in range(4)] \
            + [f'right{i}.png' for i in range(4)] + [f'left{i}.png' for i in range(4)] + ["bullet.png"]
for file in all_files:
    remove(file)