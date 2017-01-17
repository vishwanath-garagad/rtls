import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
import os

MYDIR = os.path.dirname(__file__)
FILENAME = os.path.join(MYDIR, 'ShimmerOffice1.jpg')

np.random.seed(0)
x = np.random.uniform(0.0,10.0,15)
y = np.random.uniform(0.0,10.0,15)
print FILENAME
img = imread(FILENAME)
plt.scatter(x,y,zorder=1)
plt.imshow(img,zorder=0)
plt.show()