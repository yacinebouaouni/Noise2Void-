

from PIL import Image,ImageOps
import numpy as np
import os

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr


files = os.listdir('Data/Set14/test_b')

for i in range(len(files)):

    original = np.array(ImageOps.grayscale(Image.open('Data')))
    denoised1 = np.array(Image.open('Data/DATA4b_den/Normal_N2V.png'))

    noisy = np.array(Image.open('Data/DATA4_b/Normal.png'))

    im1 = ImageOps.grayscale(Image.fromarray(original - denoised1))


    #print(f'Denoised1 Image PSNR = {PSNR(original,denoised1)}')

    #print(f'Noisy PSNR = {PSNR(original,noisy)}')


