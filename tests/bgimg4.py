#minimal example...

import matplotlib, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pylab as plt
from scipy import ndimage

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
    
root = Tk.Tk()
root.wm_title("minimal example")

root.image = plt.imread('ShimmerOffice1.png')
fig = plt.figure(figsize=(16,9))
im = plt.imshow(root.image) # later use a.set_data(new_data)
ax = plt.gca()
ax.set_xticklabels([]) 
ax.set_yticklabels([])

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(fig, master=root)
x = range(5)
y = range(5)
ax.semilogx(x,y,'o-')
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def rotate(*args):
    print 'rotate button press...'
    root.image = ndimage.rotate(root.image, 90)
    im.set_data(root.image)
    canvas.draw()
    
def quit(*args):
    print 'quit button press...'
    root.quit()     
    root.destroy() 

button_rotate = Tk.Button(master = root, text = 'Rotate', command = rotate)
button_quit = Tk.Button(master = root, text = 'Quit', command = quit)

button_quit.pack(side=Tk.LEFT)
button_rotate.pack()

Tk.mainloop()

