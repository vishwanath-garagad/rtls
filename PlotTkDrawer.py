#!/usr/bin/env python

#minimal example...

import matplotlib, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pylab as plt
from scipy import ndimage
import random, time, threading, datetime
import Tkinter as Tk
    
root = Tk.Tk()
root.wm_title("minimal example")

root.image = plt.imread('ShimmerOffice1.png')
fig = plt.figure(figsize=(10,10))
im = plt.imshow(root.image) # later use a.set_data(new_data)
ax = plt.gca()
ax.set_xticklabels([]) 
ax.set_yticklabels([])

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(fig, master=root)
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



class PlotDrawer():  
   def __init__(self):
      self.size = 10  
      self.x = [0.0] * self.size
      self.y = [0.0] * self.size
      self.mod_en = 0
      self.max = 200.0
      self.x_min = -5.0
      self.x_max = self.max+5.0
      self.y_min = -5.0
      self.y_max = self.max+5.0
      self.extent = (self.x_min, self.x_max, self.y_min, self.y_max)
      
      self.im = plt.imread("ShimmerOffice.png")
      
      return
      
   def init(self):      
      self.fig = plt.figure()
      self.ax = self.fig.add_subplot(111)
      self.ax.set_title("Shimmer Office RTLS")
      self.ax.set_xlabel("X (m)")
      self.ax.set_ylabel("Y (m)")
      # some X and Y data
      self.li, = self.ax.plot(self.x, self.y, '-r.')
      # draw and show it
      if 1:
         plt.switch_backend('TkAgg') #TkAgg (instead Qt4Agg)
         # print '#1 Backend:',plt.get_backend()
         mng = plt.get_current_fig_manager()
         ### works on Ubuntu??? >> did NOT working on windows
         # mng.resize(*mng.window.maxsize())
         mng.window.state('zoomed') #works fine on Windows!
         
      canvas = FigureCanvasTkAgg(self.fig, master=root)
      #canvas.show()
      canvas.get_tk_widget().pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

      self.fig.canvas.draw()
      plt.xlim((self.x_min,self.x_max))
      plt.ylim((self.y_min,self.y_max))

      self.extent = (self.x_min, self.x_max, self.y_min, self.y_max)
      
      canvas.show()
      #plt.show(block=False)#True      
      



      return
      
   def run(self):
      while 1:  
         try: 
            self.li.set_ydata(self.y)
            self.li.set_xdata(self.x)
            self.fig.canvas.draw()
            if 1:
               #im = plt.imread("ShimmerOffice.png")
               implot = plt.imshow(self.im, extent=self.extent)
            plt.show(block=False)#True
            #time.sleep(0.1)
         except :
            break
      return
         
   def xlim(self, x1, x2):
      self.x_min = x1
      self.x_max = x2
      return
      
   def setmax(self, m):
      self.max = m
      return
      
   def setModular(self, en):
      self.mod_en = en
      return
      
   def ylim(self, y1, y2):
      self.y_min = y1
      self.y_max = y2
      return
   
   def shiftin1(self, x1, y1):
      self.x[:-1] = self.x[1:]
      self.y[:-1] = self.y[1:]
      if self.mod_en == 1:
         self.x[-1] = self.mod(x1)
         self.y[-1] = self.mod(y1)
      else:
         self.x[-1] = x1
         self.y[-1] = y1
      return
      
   def mod(self, val):
      while(val>self.max):
         val -= self.max
      return val
               
   def updateAuto(self):
      while 1: 
         try: 
            self.x[:-1] = self.x[1:]
            self.y[:-1] = self.y[1:]
            n1 = random.random()
            n2 = random.random()
            self.x[-1] += n1
            self.y[-1] += n2
            if self.mod_en == 1:
               self.x[-1] = self.mod(self.x[-1])
               self.y[-1] = self.mod(self.y[-1])

            time.sleep(0.1)
         except :
            break
      return
   

if __name__ == "__main__":
   print "start drawer"
   max = 9.0
   margin = 2.0
   drawer = PlotDrawer()
   drawer.setmax(max)
   drawer.setModular(1)
   # drawer.xlim(-margin,max+margin)
   # drawer.ylim(-margin,max+margin)
   #shimmer office
   drawer.xlim(-13.2,10.8)
   drawer.ylim(-5.1,22.1)
   drawer.init()

   drawer_thread = threading.Thread(target=drawer.run)
   # Exit the server thread when the main thread terminates
   drawer_thread.daemon = True
   drawer_thread.start()
   
   print "start Auto updater"
   drawer_ua_thread = threading.Thread(target=drawer.updateAuto)
   # Exit the server thread when the main thread terminates
   drawer_ua_thread.daemon = True
   drawer_ua_thread.start()
   
   a = 1
   b = 2
   while 1:
      try:
         print datetime.datetime.now()
         time.sleep(1)   
      except KeyboardInterrupt:
         break