from PIL import Image, ImageDraw

min = 380
max = 750
rnge = max-min
interval = 50
width = 2
lines = int(rnge / interval)

def get_label() -> Image:
    im = Image.new(mode = "RGB", size = (740, 20), color = (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(lines + 1):
        x = (i * width * interval)
        draw.line([(x,0), (x,10)], (0, 0, 0), 4)
        draw.text((x,11), str(int(x/2 + min)), (0,0,0))
    return im

def get_title(title: str) -> Image:
    im = Image.new(mode = "RGB", size = (740, 12), color = (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.text((0,0), title, (0,0,0))
    return im