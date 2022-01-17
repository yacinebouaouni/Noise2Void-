

from PIL import Image
import numpy as np

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr


original = np.array(Image.open('Data/test/original_png/0001.png'))
denoised1 = np.array(Image.open('DenoisedData/0001_N2V.png'))

noisy = np.array(Image.open('Data/test/noisy25/0001.png'))

print(f'Denoised1 Image PSNR = {PSNR(original,denoised1)}')


print(f'Noisy PSNR = {PSNR(original,noisy)}')


