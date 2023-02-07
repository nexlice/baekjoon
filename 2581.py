import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
Prime = list(range(M, N + 1))

# 읽는 중에 리스트를 조작하면 문제가 생기는 듯 하다..........
nonPrime = []

for number in Prime:
    if number == 2:
        continue
    elif number == 1 or number % 2 == 0:
        nonPrime.append(number)
    else:
        for i in range(number - 2, 1, -2):
            if number % i == 0:
                nonPrime.append(number)
                break

for i in nonPrime: Prime.remove(i)

if len(Prime) == 0 : print(-1)
else:
    print(sum(Prime))
    print(min(Prime))