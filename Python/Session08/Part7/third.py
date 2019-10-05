import random

while True:
    listword = ["try", "to", "guess", "what", "is", "in", "here"]

    suffle = random.randint(0, len(listword)-1)
    word2 = listword[suffle]
    word = list(listword[suffle])
    listnone = []
    print ("What is this word?")
    for i in range (len(word)):
        while True:
            suffle2first = random.randint(0, len(word)-1)
            if suffle2first in listnone:
                suffle2first = random.randint(0, len(word)-1)
            else:
                listnone.append(suffle2first)
                break

        wordsecond = (word[suffle2first])
        print (wordsecond, end='')

    while True:
        print (" ")
        answer = input("Your answer:")
        if answer == word2:
            print ("Right")
            break
        else:
            print ("Wrong")
    yn= input ("Want to continue? (y/n)")
    if yn == "y":
        print ("Ok")
    elif yn == "n":
        break
