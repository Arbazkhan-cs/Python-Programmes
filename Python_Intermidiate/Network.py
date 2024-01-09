# # Method 1 To Connect with web and taking the data.
# import socket
#
# my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# my_sock.connect(('data.pr4e.org', 80))
#
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# my_sock.send(cmd)
#
# while True:
#     data = my_sock.recv(1024)
#     if len(data) < 1:
#         break
#     print(data.decode())
#
# my_sock.close()
#
#
# # Method 2 To Connect with the web and taking the data from it.
import urllib.request, urllib.parse, urllib.error
#
# my_data = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for lines in my_data:
#     print(lines.decode().strip())


# Method 3 To Connect with the web and taking the data from it.

from bs4 import BeautifulSoup as BS

my_data = urllib.request.urlopen('https://www.msijanakpuri.com/')
lines_list = BS(my_data, 'html.parser')
print(lines_list)



