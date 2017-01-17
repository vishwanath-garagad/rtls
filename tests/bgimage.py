import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.misc
from scipy.misc import imread
#import scipy.misc.imread
import matplotlib.cbook as cbook
import os

MYDIR = os.path.dirname(__file__)

np.random.seed(0)
x = np.random.uniform(0.0,10.0,15)
y = np.random.uniform(0.0,10.0,15)

#datafile = cbook.get_sample_data('C:\\Users\\WeiboP\\git\\rtls\\tests\\ShimmerOffice1.jpg')
datafile = cbook.get_sample_data(os.path.join(MYDIR, 'ShimmerOffice1.jpg')
img = imread(datafile)
plt.scatter(x,y,zorder=1)
plt.imshow(img, zorder=0, extent=[0.5, 8.0, 1.0, 7.0])
plt.show()