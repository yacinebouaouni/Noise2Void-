from PIL import Image
import os
path = 'Data/Train/'
files = os.listdir(path)

size = (180,180)
for f in files:

    im1 = Image.open(path+f)
    im1 = im1.resize(size)
    im1.save(path+f)
