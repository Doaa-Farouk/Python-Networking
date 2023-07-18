import socket
import nmap
import sys

# one way not working
# # begin scanning on this protocol
# begin = 70
# # end scanning on this protocol
# end = 80
# # ip to be scanned
# target = '127.0.0.1'
# # scanner = nmap.PortScanner()
# # for i in range(begin, end):
# #     response_ = scanner.scan(target, str(i))
# #     response_ = response_['scan'][target]['tcp'][i]['state']
# #     print(f'Port {i} is {response_}.')

#     target = socket.gethostbyname('www.eiu-edu.info')
try:

    target = '127.0.0.1'
    for port in range(130, 140):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()