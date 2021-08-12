# %%

'''
Exercise  12.5:
Change the socket program so that it only shows the data after the headers
and a blank line have been received.
'''

# import the relevant libraries
import socket  # noqa

# connection and get-request
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)

# receiving end decoding the socket answer
data = my_sock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4   # end of header
print(message[header_end_pos:], end='')

# receive the first 512 characters and print them
while True:
    data = my_sock.recv(512)
    if not data:
        break
    print(data.decode())

# close the connection
my_sock.close()
