from PIL import Image, ImageDraw
from wavelength_to_rgb import wavelength_to_rgb

def generate_spectra(spectra):
    im = Image.new(mode = "RGB", size = (740, 100))
    draw = ImageDraw.Draw(im)

    for i in spectra:
        color = wavelength_to_rgb(i, gamma=.7)
        x = (i - 380) * 2
        draw.line([(x,0), (x,100)], color, 2)
    
    return im
