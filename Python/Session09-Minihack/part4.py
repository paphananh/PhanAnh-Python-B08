num = ["6", "7", "9", "2", "10"]
for i in range (len(num)):
    if int(num[i])%2 == 0:
        print (num[i])

numuser = input ("Enter a number: ")
num = numuser.split(' ')
for i in range (len(num)):
    if int(num[i])%2 == 0:
        print (num[i])
