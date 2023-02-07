import sys
ssr = sys.stdin.readline

maxVal = 100
# dowhazi = [[0] * (maxVal + 1)] * (maxVal + 1)
# shallow copy occurs.

rows = cols = maxVal + 1

dowhazi = [[0 for j in range(cols)] for i in range(rows)]

length = 10
ans = 0

N = int(ssr())
for i in range(N):
    X, Y = list(map(int, ssr().rstrip().split()))
    for x in range(length):
        for y in range(length):
            dowhazi[X + x][Y + y] = 1
            
for i in range(maxVal):
    ans += sum(dowhazi[i])

print(ans)