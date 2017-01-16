import socket
import sys, struct, serial, datetime, time

HOST, PORT = "192.168.0.129", 9998
# HOST, PORT = "113.210.186.68", 9999
#data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser = serial.Serial(sys.argv[1], 115200)
ser.flushInput()
print "port opening, done."

txdata = ""
# id = sys.argv[2]
id = "2"
         
try:
   while 1:
      buf_len = ser.inWaiting()
      if buf_len>=8:
         rxdata = ser.read(8)
         ser.flushInput()
         data_calib, = struct.unpack('d',rxdata)
         print datetime.datetime.now(), data_calib
         
         data_str = str(int(data_calib*100))
         # Connect to server and send data
         txdata = id.zfill(2)+data_str.zfill(4)+"\n"
         
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
         sock.settimeout(1)
         try:
             # Connect to server and send data
             sock.connect((HOST, PORT))
             sock.send(txdata)
         except:
             sock.close()
         finally:
             sock.close()

         # Receive data from the server and shut down
         # received = sock.recv(2)
         # print "Sent: {}".format(txdata), "Received: {}".format(received)
            
except KeyboardInterrupt:
   sock.close()
