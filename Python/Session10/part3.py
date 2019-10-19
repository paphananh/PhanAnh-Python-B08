dict = {
    'thing1' : 'nothing',
    'thing2' : 'nothingn2',
    'thing3' : 'nothingn3',
}

dict['thing4'] = 'nothingn4'

newk = input("Key?")
newv = input("Value?")
dict[newk] = newv

for i in dict:
    print(i, dict[i])

dict['thing4'] = 'nothingn44'
newkk = input("Edit key?")
newvv = input("Value?")
dict[newkk] = newvv

for i in dict:
    print(i, dict[i])

del dict ["thing4"]
for i in dict:
    print(i, dict[i])
deldict = input("Detele what?")
del dict [deldict]
for i in dict:
    print(i, dict[i])
