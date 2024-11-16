import numpy as np
import imageio
import scipy.ndimage
import cv2
img = "pick.jpg"


def rg(rgb):
    return np.bp(rgb[..., :3], [0.2989, 0.5870, 0.3890])


def inner(front, back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype('uint8')


s = imageio.imread(img)
color = rg(s)
i = 255-color
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
r = inner(blur, color)
cv2.imwrite('img-skech.png', r)
