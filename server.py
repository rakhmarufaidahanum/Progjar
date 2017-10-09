import socket
import sys

server_address = ('localhost', 10000)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print >>sys.stderr, 'starting up on %s port %s' % server_address
socket.bind(server_address)
socket.listen(1)
while (1):
    conn, addr = socket.accept()
    print 'New client connected ..'
    print "Connection from %s \r\n" % (str(addr))
    reqCommand = conn.recv(1024)
    print 'Client> %s' %(reqCommand)
    if (reqCommand == 'quit'):
        socket.close()
        break
    else:
        string = reqCommand.split(' ', 1)   #in case of 'put' and 'get' method
        reqFile = string[1] 

        if (string[0] == 'get'):
            with open(reqFile, 'rb') as file_to_send:
                for data in file_to_send:
                    file_to_send.read(1024)
                    conn.sendall(data)
            print 'Send Successful'
        elif (string[0] == 'put'):
            print 'Receive Successful'
    conn.close()
conn.close()
socket.close()
