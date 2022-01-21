
from PIL import Image ,ImageOps
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


files = os.listdir('Data/BSDS300/test_b')

psnr_ = []
for i in range(len(files)):

    noisy = np.array(Image.open('Data/BSDS300/test_b/'+files[i]))
    denoised1 = np.array(Image.open('Data/BSDS300/test_b_denoised/'+files[i][:-4]+'_N2V.png'))
    original = np.array(ImageOps.grayscale(Image.open('Data/BSDS300/test_b_clean/'+files[i])))

    psnr = PSNR(original, denoised1)
    psnr_.append(psnr)
    print(f'image {i} psnr = {psnr}')


print(f'Mean PSNR is = {sum(psnr_)/len(psnr_)}')


