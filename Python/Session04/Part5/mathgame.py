import random


for i in range (10):
    x = random.randint(30, 60)
    y = random.randint(40, 80)
    a = random.randint(-1, 1)
    z = x + y + a
    print (x , "+", y, "=", z)
    t = input("True or False?")
    if t == "T" and z == x + y:
        print("Right")
    elif t == "F" and z != x + y:
        print ("Right")
    else:
        print("Wrong")
