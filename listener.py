import socket

# Default size for receiving stuff on a socket
chunk_size = 128

while True:
    response = None
    data = raw_input( "Send to server (type END to exit):" )

    #create an INET, STREAMing socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        # Log something like server error?
        s = None
        break

    try:
        s.connect(('localhost',5800))
        s.sendall(data)
        # Wait for a response from the server so we don't
        # get input from the mic while the speaker is still
        # talking.
        response = s.recv(chunk_size)
    except socket.error as msg:
        # Log something like server error
        s.close()
        break

    # Close the socket. It's a one time use.
    s.close()

    # If we said END, break
    if data.upper() == "END":
        break

    # If our server is not ok or something, break
    if response is not None and response != 'OK':
        break

print "END OF CLIENT"
