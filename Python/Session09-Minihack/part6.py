quan = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
dan = [150300, 247100, 333300, 266800, 420900, 318000]
km2 = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
matdolist = []
for i in range (len(dan)):
    matdo = dan[i]/km2[i]
    matdolist.append(int(matdo))
print (*matdolist, sep=', ')
sum = 0
for i in range(len(matdolist)):
    sum = sum + int(matdolist[i])
    sum = sum/len(matdolist)
print(sum)
