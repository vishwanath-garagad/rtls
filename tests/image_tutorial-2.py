import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import time
img = mpimg.imread('pic.png')
imgplot = plt.imshow(img)
plt.show()

while 1:
   imgplot = plt.imshow(img)
   time.sleep(1)
lum_img = img[:, :, 0]
plt.imshow(lum_img)

  