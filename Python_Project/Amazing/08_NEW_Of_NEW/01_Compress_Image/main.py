import PIL
from PIL import Image
from tkinter.filedialog import *

file_name=askopenfilename()
img=PIL.Image.open(file_name)
myHeight,myWidth=img.size

img=img.resize((myHeight,myWidth) ,PIL.Image.ANTIALIAS)
save_path=asksaveasfilename()
img.save(save_path+"_compressed.JPEG")