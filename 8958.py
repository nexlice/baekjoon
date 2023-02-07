import sys

def lenIntoScore(a):
    if a == 0:
        return 0
    value = a * (a + 1) / 2
    return value

numCase = int(sys.stdin.readline().rstrip())
listAnswer = []

for i in range (numCase):
    listAnswer.append(sys.stdin.readline().rstrip())
    # print(listAnswer[i])
    listAnswer[i] = listAnswer[i].split('X')
    # print("splitted")
    # print(listAnswer[i])
    listAnswer[i] = list(map(len, listAnswer[i]))
    # print("length")
    # print(listAnswer[i])
    listAnswer[i] = list(map(lenIntoScore, listAnswer[i]))
    # print("lenIntoScore")
    # print(listAnswer[i])
    listAnswer[i] = sum(listAnswer[i])

for i in range (numCase):
    print((int)(listAnswer[i]))
