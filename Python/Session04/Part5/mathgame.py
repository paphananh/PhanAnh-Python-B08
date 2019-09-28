import random

fs = 0
for i in range (10):
    x = random.randint(3, 10)
    y = random.randint(4, 12)
    a = random.randint(-1, 1)
    op = random.randint(0,3)
    if op == 0 :
        z = x + y + a
        print (x , "+",y , "=",z)
        t = input ("True or False?")
        if t == "T" and z == x + y:
            print("Right")
            fs = fs + 1
            print ("Score: ",fs)
        elif t == "F" and z != x + y:
            print ("Right")
            fs = fs + 1
            print ("Score: ",fs)
        else:
            print("Wrong")
            print ("Score: ",fs)
    elif op == 1:
        z = x - y + a
        print (x , "-" ,y, "=",z)
        t = input ("True or False?")
        if t == "T" and z == x - y:
            print("Right")
            fs = fs + 1
            print ("Score: ",fs)
        elif t == "F" and z != x - y:
            print ("Right")
            fs = fs + 1
            print ("Score: ",fs)
        else:
            print("Wrong")
            print ("Score: ",fs)
    elif op == 2:
        z = x*y + a
        print (x , "*", y, "=",z)
        t = input ("True or False?")
        if t == "T" and z == x * y:
            print("Right")
            fs = fs + 1
            print ("Score: ",fs)
        elif t == "F" and z != x * y:
            print ("Right")
            fs = fs + 1
            print ("Score: ",fs)
        else:
            print("Wrong")
            print ("Score: ",fs)
    elif op == 3:
        z = x/y + a
        print (x , "/" , y, "=",z)
        t = input ("True or False?")
        if t == "T" and z == x / y:
            print("Right")
            fs = fs + 1
            print ("Score: ",fs)
        elif t == "F" and z != x / y:
            print ("Right")
            fs = fs + 1
            print ("Score: ",fs)
        else:
            print("Wrong")
            print ("Score: ",fs)
