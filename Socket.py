import imp
import socket
import sys

ip = socket.gethostbyname("www.google.com") # getting the ip of a website
print(ip)

# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("Succeed")
# except socket.error as er:
#     print("Failed")
# port = 80
# try:
#     host_ip = socket.gethostbyname("www.github.com")
# except socket.gaierror :
#     print("Failed")
#     sys.exit()

# s.connect((host_ip, port))
# print(f"Connected succeed in port {host_ip}")