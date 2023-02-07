"""
A : 고정 비용
B : 생산 비용
C : 판매가

A + B * n < C * n 이 되는 자연수 n 구하기.

->

A < (C - B) * n

-> if B is bigger or equal to C, return -1.

"""

import sys
A, B, C = list(map(int, sys.stdin.readline().rstrip().split()))

if B >= C:
    print(-1)
else:
    print(f"{A // (C - B) + 1}")