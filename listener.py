import socket

#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost',12345))

s.sendall("HEY THIS IS A MESSAGE")

s.close()

#print "END OF CLIENT"
