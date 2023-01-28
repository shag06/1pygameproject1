from PIL import Image


def repl(file_in):
    print(file_in)
    img = Image.open(file_in)
    pixels = img.load()
    w, h = img.width, img.height
    print(w, h)
    const1 = 9
    const2 = 4
    print(w // const1, h // const2)
    for i in range(const1):
        for j in range(const2):
            img_new = Image.new(img.mode, (w // const1, h // const2), "white")
            pixel = img_new.load()
            for x in range(w // const1):
                for y in range(h // const2):
                    pixel[x, y] = pixels[i * (w // const1) + x, j * (h // const2) + y]
            name = ["left", "right", "face", "back"][j % 4] + str(i) + ".png"
            if j >= 4:
                name = "aboba.png"
            img_new.save(name)
    img.save(file_in)


all_files = ["rr.png"]
for file in all_files:
    repl(file)