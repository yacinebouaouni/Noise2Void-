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


path = 'Data/BSDS300/'





files = os.listdir(path+'test/')

for f in files:

    im1 = np.array(Image.open(path+'test/'+f))
    im1 = ImageOps.grayscale(Image.fromarray(im1))
    im1.save(path+'test_b_clean/'+f[:-3]+'png')

for f in files:

    im1 = np.array(Image.open(path+'test/'+f))
    if len(im1.shape)<3:
        continue
    im1 = noisy(im1, sig=25)
    im1 = ImageOps.grayscale(Image.fromarray(im1))

    im1.save(path+'test_b/'+f[:-3]+'png')
