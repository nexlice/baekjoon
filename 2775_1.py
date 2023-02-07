def boonyeo(k , n):
    apartment = []
    firstFloor = [i for i in range(1, n + 1)]
    tmpFloor = firstFloor
    # print(tmpFloor)
    apartment.append(firstFloor)
    for floor in range(k):
        for num in range(1, n):
            tmpFloor[num] += tmpFloor[num - 1]
        # print(tmpFloor)
        apartment.append(tmpFloor)
    return apartment[k][n - 1]

    

import sys
ssr = sys.stdin.readline

T = int(ssr())

answer = []
for i in range(T):
    k = int(ssr())
    n = int(ssr())
    answer.append(boonyeo(k, n))

for val in answer:
    print(val)