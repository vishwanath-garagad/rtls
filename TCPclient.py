import socket
import sys

HOST, PORT = "192.168.0.129", 9999
# HOST, PORT = "113.210.186.68", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.settimeout(1)
try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
    print "Sent:     {}".format(data)
    print "Received: {}".format(received)
except:
    sock.close()
finally:
    sock.close()
