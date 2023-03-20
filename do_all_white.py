from PIL import Image


def remove(file_in):
    print(file_in)
    img = Image.open(file_in)
    pixels = img.load()
    w, h = img.width, img.height
    print(w, h)
    for x in range(w):
        for y in range(h):
            r, g, b = pixels[x, y]
            if r > 215 and b > 215 and g > 215:
                r = g = b = 255
            pixels[x, y] = r, g, b
    img.save(file_in)


all_files = ["data/images/game_over_paint.jpg"]
for file in all_files:
    remove(file)