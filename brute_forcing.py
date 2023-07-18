import requests
dictionary = open('dictionary.txt', 'r')
url = input("Enter URL: ")

for i in dictionary:
    r = requests.get(url +'/'+ i.rstrip())
    if r.status_code == 200:
        print("The page "+ url +'/'+ i +" is found")

print("Done")