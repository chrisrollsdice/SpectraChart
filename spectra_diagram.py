from spectra_generator import generate_spectra
from label import get_label, get_title
from photo import get_concat_v, get_border

if __name__ == "__main__":
    spectra = []
    name = input("Enter the name of the spectra chart: ")
    fname = input("Enter the file name of the spectra chart: ")
    value = int(input("Enter a wavelength on the chart (-1 to stop): "))
    while value != -1:
        spectra.append(value)
        value = int(input("Enter a wavelength on the chart (-1 to stop): "))
    dia = generate_spectra(spectra)
    lbl = get_label()
    ttl = get_title(name)
    im = get_concat_v(dia, lbl)
    im = get_concat_v(ttl, im)
    im = get_border(im, (255, 255, 255), 5)
    im.show()
    im.save("Diagrams/" + fname + ".png")