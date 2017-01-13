import PlotDrawer, ShimmerPos2
import time, random
import SocketServer, time,threading,datetime

HOST, PORT = "192.168.0.129", 9999
max = 10.0
margin = max/10
pos = ShimmerPos2.ShimmerPos2(max)

   
class MyTCPHandler(SocketServer.BaseRequestHandler):
   def handle(self):
      global pos
      self.data = self.request.recv(1024)#.strip() # strip() to kill \n in the end of string
      print "{} bytes from {}".format(len(self.data), self.client_address[0])
      pos.update(self.data)
      pos.calc()
      #self.request.sendall("ok")
      return

if __name__ == "__main__":
   print __name__, "start ..."
   
   # ====================
   # init the plot drawer
   # ====================
   print "starting drawer..."
   drawer = PlotDrawer.PlotDrawer()
   drawer.setmax(max)
   drawer.xlim(-margin,max+margin)
   drawer.ylim(-margin,max+margin)
   drawer.init()
   drawer_thread = threading.Thread(target=drawer.run)
   # Exit the server thread when the main thread terminates
   drawer_thread.daemon = True
   drawer_thread.start()
   
   # ===================
   # init the TCP Server
   # ===================
   print "prepare Server..."
   # Create the server, binding to localhost on port 9999
   server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

   # Activate the server; this will keep running until you
   # interrupt the program with Ctrl-C
   server_thread = threading.Thread(target=server.serve_forever)
   # server_thread = threading.Thread(target=server.handle_request)
   # Exit the server thread when the main thread terminates
   server_thread.daemon = True
   server_thread.start()    
   
   cnt = 0
   print "start loop..."
   while 1:
      drawer.shiftin1(pos.x,pos.y)
      time.sleep(0.1)   
      if cnt >= 10:
         cnt = 0
         print datetime.datetime.now(),  "x = %0.2f, y = %0.2f" %pos.position()
      
   
   a = 5.0
   b = 5.0
   while 1:
      try: 
         a += random.random()/10
         b += random.random()/10
         if(a>max):
            a-=max/2
         if(b>max):
            b-=max/2
         a_f = drawer.mod(a)
         b_f = drawer.mod(b)
         a_str = str(int(a_f*100))
         b_str = str(int(b_f*100))
         str1 = "01"+a_str.zfill(4)+"\r"
         str2 = "02"+b_str.zfill(4)+"\r"
         # print a, a_f, a_str, str1
         # print b, b_f, b_str, str2
         pos.update(str1)
         pos.update(str2)
         pos.calc()
         print "x = %0.2f, y = %0.2f" %pos.position()
         x,y = pos.position()
         drawer.shiftin1(x,y)
         time.sleep(0.1)   
      except KeyboardInterrupt:
         break