import sys

N = int(sys.stdin.readline().rstrip())
numList = list(map(int, sys.stdin.readline().rstrip().split()))

# 읽는 중에 리스트를 조작하면 문제가 생기는 듯 하다..........
nonPrime = []

for number in numList:
    if number == 2:
        continue
    elif number == 1 or number % 2 == 0:
        nonPrime.append(number)
    else:
        for i in range(number - 2, 1, -2):
            if number % i == 0:
                nonPrime.append(number)
                break

print(len(numList) - len(nonPrime))