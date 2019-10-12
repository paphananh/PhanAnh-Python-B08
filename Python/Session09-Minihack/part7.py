highscore = [45, 67, 56, 78, 31, 65, 35]
print(*highscore)

while True:
    new = int(input("New highscore: "))
        highscore.append(new)
        sortList = (sorted(highscore, reverse=True))
        for i in range (5):
            print(sortList[i])
