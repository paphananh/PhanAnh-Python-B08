num = ["5", "1", "8", "92", "-1", "30"]

check = input("Enter a number: ")
if check not in num:
    print ("Not found in our list")
else:
    for i in range (len(num)):
            if num[i] == check:
                print ("Found, position", i+1)

sum = 0
for i in range(len(num)):
    sum = sum + int(num[i])
print(sum)
