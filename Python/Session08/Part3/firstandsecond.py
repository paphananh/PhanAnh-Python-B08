a = [ "u", "y", "e"]
a[0] = "n"
print (a[0], a[1], a[2])

a = [ "u", "y", "e"]
a[2] = "n"
print (a[0], a[1], a[2])

a = [ "u", "y", "e"]
ind = int(input("Replace where?"))
inw = input("Replace what?")
a[ind] = inw
print (a[0], a[1], a[2])
