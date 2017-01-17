import SocketServer, time

   
class MyTCPHandler(SocketServer.BaseRequestHandler):
   """
   The request handler class for our server.

   It is instantiated once per connection to the server, and must
   override the handle() method to implement communication to the
   client.
   """
   def __init__(self, request, client_address, server):
      self.idint = 0
      self.idstr = "Shimmer haha"   
      SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
      return

   def handle(self):
      # self.request is the TCP socket connected to the client
      self.data = self.request.recv(1024)#.strip()
      #print "{} wrote:".format(self.client_address[0])
      print "{} bytes from {}".format(len(self.data), self.client_address[0])
      # print self.data
      # just send back the same data, but upper-cased
      # self.request.sendall(self.data.upper())
      #self.unpack()
      self.callback()
      self.request.sendall(self.idstr)
      return
      
   def unpack(self):
      if (len(self.data) == 11):
         #print "correct length"
         self.idint = int(self.data[0])*256 + int(self.data[1])
         self.idstr = "Shimmer " + str(self.idint)
      return
      

if __name__ == "__main__":
   HOST, PORT = "192.168.0.129", 9999

   # Create the server, binding to localhost on port 9999
   server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

   # Activate the server; this will keep running until you
   # interrupt the program with Ctrl-C
   server.serve_forever()
