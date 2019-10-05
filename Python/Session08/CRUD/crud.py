crudlist = ["C", "R", "U", "D"]

while True:
    crud = input("C, R, U or D?")
    if crud == "C":
        C = input("Add at the end: ")
        crudlist.append(C)
    elif crud == "R":
        for i in range (0,len(crudlist)):
            print (crudlist[i])

    elif crud == "U":
        print (*crudlist)
        rwe = int(input("Replace where? Have "+ str(len(crudlist))+ ": "))
        rwh = input("Replace what?")
        crudlist[rwe] = rwh
    elif crud == "D":
        print (*crudlist)
        delete = int(input("Remove where?"))
        crudlist.pop (delete)
    elif crud == "end":
        break
