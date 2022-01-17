import numpy as np
import os
import cv2
from PIL import Image, ImageOps
import imageio

def noisy(image, sig):
      row,col,ch= image.shape
      mean = 0
      sigma = sig
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      noisy = np.clip(noisy, a_min=0, a_max=255)
      noisy = noisy.astype('uint8')
      return noisy


path = 'Data/test/original_png/'
files = os.listdir(path)
size = (180,180)

for f in files:

    im1 = Image.fromarray(np.array(Image.open(path+f)))
    #im1 = Image.fromarray(noisy(im1, sig=25))
    im1 = ImageOps.grayscale(im1)

    #im1 = im1.resize(size)
    im1.save('Data/test/original_b/'+f[:-3]+'png')
