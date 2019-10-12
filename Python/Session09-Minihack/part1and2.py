colorlist =["blue", "red", "green"]
print (*colorlist)
add = input("What do you want to add?")
colorlist.append(add)
print (*colorlist)
location = int(input("Where do you want to see?"))
print (colorlist[location-1])

deteleitem = input("What do you want to remove?")
if deteleitem.isdigit() :
    colorlist.pop(int(deteleitem)-1)
elif deteleitem.isalpha():
    colorlist.remove(deteleitem)
print (*colorlist)

from turtle import *
for i in range (len(colorlist)):
    color(colorlist[i])
    forward(100)
mainloop()
