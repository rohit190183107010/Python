import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = Image.open(file_path)
myHeight, myWidth = img.size
print(myHeight, myWidth)

img = img.resize((myHeight, myWidth), Image.ANTIALIAS)

save_path = askopenfilename()
img.save(save_path+"_compressed.PNG")
