quan = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
dan = [150300, 247100, 333300, 266800, 420900, 318000]

danmax = (max(dan))
indexDanMax = dan.index(danmax)
print(quan[indexDanMax])

danmin = (min(dan))
indexDanMin = dan.index(danmin)
print(quan[indexDanMin])
