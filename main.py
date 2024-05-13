from tkinter.filedialog import *

import PIL
from PIL import Image

file_path = askopenfilename()
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth), PIL.Image.Resampling.LANCZOS)
img = img.convert('RGB')
save_path = asksaveasfilename()
img.save(save_path + "compressed.jpg")
