import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('www.pythonlearn.com',80))

mySock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1/0\n\n')

while True:
	data = mySock.recv(512)
	if (len(data) < 1):
		break
	print data

mySock.close()

		