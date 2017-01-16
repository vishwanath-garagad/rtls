import matplotlib.pyplot as plt
import numpy as np
import random, time, threading, datetime
    
class PlotDrawer():  
   def __init__(self):
      self.size = 10  
      self.x = [0.0] * self.size
      self.y = [0.0] * self.size
      self.max = 200.0
      self.x_min = -5.0
      self.x_max = self.max+5.0
      self.y_min = -5.0
      self.y_max = self.max+5.0
      
      return
      
   def init(self):      
      self.fig = plt.figure()
      self.ax = self.fig.add_subplot(111)
      # some X and Y data
      self.li, = self.ax.plot(self.x, self.y, '-r.')
      # draw and show it
      self.fig.canvas.draw()
      plt.xlim((self.x_min,self.x_max))
      plt.ylim((self.y_min,self.y_max))
      plt.show(block=False)
      return
      
   def run(self):
      while 1:  
         try: 
            self.li.set_ydata(self.y)
            self.li.set_xdata(self.x)
            self.fig.canvas.draw()
            time.sleep(0.1)
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
      
   def ylim(self, y1, y2):
      self.y_min = y1
      self.y_max = y2
      return
   
   def shiftin1(self, x1, y1):
      self.x[:-1] = self.x[1:]
      self.y[:-1] = self.y[1:]
      # self.x[-1] = self.mod(x1)
      # self.y[-1] = self.mod(y1)
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
            # self.x[-1] = self.mod(self.x[-1])
            # self.y[-1] = self.mod(self.y[-1])

            time.sleep(0.1)
         except :
            break
      return
   

if __name__ == "__main__":
   print __name__, "start ..."
   
   print "start drawer"
   max = 20.0
   margin = 2.0
   drawer = PlotDrawer()
   drawer.setmax(max)
   drawer.xlim(-margin,max+margin)
   drawer.ylim(-margin,max+margin)
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