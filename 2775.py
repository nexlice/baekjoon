def boonyeo(k , n):
    if k == 0:
        return n
    else:
        sum = 0
        for i in range(n):
            sum += boonyeo(k - 1, i + 1)
        return sum
    

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