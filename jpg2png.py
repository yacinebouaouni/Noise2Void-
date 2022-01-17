from PIL import Image
import os
path = 'Data/Train/'
files = os.listdir(path)

for f in files:

    im1 = Image.open(path+f)
    im1.save(path+f[:-3]+'.png')
