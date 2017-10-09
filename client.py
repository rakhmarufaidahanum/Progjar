import socket
import sys

HOST = 'localhost'    # server name goes in here
PORT = 10000

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((HOST, PORT))

def get(commandName):
	socket1.send(commandName)
	string = commandName.split(' ', 1)
	inputFile = string[1]
	data = socket1.recv(1024)
	print 'Data> %s' %(data)
	print 'GET Successful'
	socket1.close()
	return

def put(commandName):
    socket1.send(commandName)
    string = commandName.split(' ', 1)
    inputFile = string[1]
    with open(inputFile, 'wb') as file_to_write:
        data = socket1.recv(1024)
            # print data
        file_to_write.write(data)
    	file_to_write.close()
    print 'PUT Successful'
    socket1.close()
    return

#msg = raw_input('Enter your name: ')
print 'Instruction'
print '"get [filename]" to download the file from the server '
print '"put [filename]" to send the file to the server '
print '"quit" to exit'
#sys.stdout.write('%s> ' % msg)
inputCommand = sys.stdin.readline().strip()
if (inputCommand == 'quit'):
	socket1.send(inputCommand)
	socket1.close()
else:
	string = inputCommand.split(' ', 1)
	if (string[0] == 'get'):
		get(inputCommand)
	elif (string[0] == 'put'):
		put(inputCommand)
