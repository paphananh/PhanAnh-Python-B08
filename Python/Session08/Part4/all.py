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

a.remove("y")
print (a[0], a[1])
if "u" in a:
    print("Have u, so I delete it.")
    a.remove("u")
    print(a[0])

a = [ "u", "y", "e"]
print(a)
ind = int(input("Delete where?"))
a.pop(ind)
print (a[0], a[1])

a = [ "u", "y", "e"]
print(a)
inw = input("Remove what?")
a.remove(inw)
print (a[0], a[1])
