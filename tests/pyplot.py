import matplotlib.pyplot as plt
import numpy as np
import time, random

def mod(x, max): 
   if x > max:
      x -= max
   return x
   
max = 20      
inc_size = 4

fig = plt.figure()
ax = fig.add_subplot(111)

# some X and Y data
x = np.arange(100)
y = np.random.randn(100)

li, = ax.plot(x, y, 'r.')

# draw and show it
fig.canvas.draw()
plt.ylim((-5,25))
plt.show(block=False)

# loop to update the data
while True:
   try:
      y[:-inc_size] = y[inc_size:]
      if inc_size == 1:
         x = random.random()
         #print x,
         y[-1] += x
         y[-1] = mod(y[-1], max)
      else:
         x = random.random()
         #print x,
         y[-inc_size] = y[-inc_size-1] + x
         y[-inc_size] = mod(y[-inc_size], max)
         for i in range(inc_size-1):
            x = random.random()
            #print x,
            y[-inc_size+i+1] = y[-inc_size+i] + x
            y[-inc_size+i+1] = mod(y[-inc_size+i+1], max)

      # set the new data
      li.set_ydata(y)

      fig.canvas.draw()

      time.sleep(0.01)
   except KeyboardInterrupt:
      break