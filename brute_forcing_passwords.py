import  requests
url = 'http://192.168.1.1/login.htm'
username = 'admin'

with open('500-worst-passwords.txt','r') as password:
    bruteforce(url,password)
