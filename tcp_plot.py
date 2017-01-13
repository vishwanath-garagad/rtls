import matplotlib.pyplot as plt
import numpy as np
import time, random
import SocketServer, time, MyTimer

x = np.arange(10)
y = np.arange(10)
   
class MyTCPHandler(SocketServer.BaseRequestHandler):
   """
   The request handler class for our server.

   It is instantiated once per connection to the server, and must
   override the handle() method to implement communication to the
   client.
   """

   def handle(self):
      global x,y
      # self.request is the TCP socket connected to the client
      self.data = self.request.recv(4)#.strip()
      #print "{} wrote:".format(self.client_address[0])
      timer.relTime()
      print "{} bytes from {}".format(len(self.data), self.client_address[0])      
      
      x[:-1] = x[1:]
      y[:-1] = y[1:]
      
      x0 = self.data[0]+self.dataself.data[1]
      x[-1] = x0

      # print self.data
      # just send back the same data, but upper-cased
      # self.request.sendall(self.data.upper())
      
    
class PlotDrawer():        
   def __init__(self):
      global x,y
      fig = plt.figure()
      ax = fig.add_subplot(111)
      # some X and Y data
      li, = ax.plot(x, y, 'r.')
      # draw and show it
      fig.canvas.draw()
      plt.xlim((-5,25))
      plt.ylim((-5,25))
      plt.show(block=False)
      
   def run(self):
      while 1:  
         # set the new data
         li.set_ydata(y)
         fig.canvas.draw()
         time.sleep(0.1)
   

if __name__ == "__main__":
   print __name__, "start ..."

   max = 20      

   fig = plt.figure()
   ax = fig.add_subplot(111)
   # some X and Y data
   li, = ax.plot(x, y, 'r.')
   # draw and show it
   fig.canvas.draw()
   plt.ylim((-5,25))
   plt.show(block=False)

   HOST, PORT = "192.168.0.123", 9998

   timer = MyTimer.MyTimer()

   print timer
   
   print "start server"
   # Create the server, binding to localhost on port 9999
   server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
   server_thread = threading.Thread(target=server.serve_forever)
   # Exit the server thread when the main thread terminates
   server_thread.daemon = True
   server_thread.start()
   
   print "start drawer"
   drawer = PlotDrawer()
   drawer_thread = threading.Thread(target=drawer.run)
   # Exit the server thread when the main thread terminates
   drawer_thread.daemon = True
   drawer_thread.start()
    
   