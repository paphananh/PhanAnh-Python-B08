import random

word = input ("Enter the word:")
listword = list(word)
for i in range (len(listword)):
    suffle = random.randint(0, len(listword))
    listword = [x.upper() for x in listword]
    print (listword[suffle])
