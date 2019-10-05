a = [ "u", "y", "e"]
for i in range (3):
    print (a[i])

a = [ "u", "y", "e"]
a = [x.upper() for x in a]
for i in range (3):
    print (a[i])

a = [ "u", "y", "e"]
for i , item in enumerate (a):
    print (i,a[i])

a = [ "u", "y", "e","ye"]
for i in range(len(a)):
    if "e" in a[i] :
        print (a[i])
