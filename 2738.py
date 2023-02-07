import sys
N, M = list(map(int, sys.stdin.readline().rstrip().split()))

a = []
b = []
for i in range(N):
    a.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    b.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = [[0]* M] * N

printStr = ""
for n in range(N):
    for m in range(M):
        result[n][m] = a[n][m] + b[n][m]
        printStr += str(result[n][m]) + " "
    print(printStr)
    printStr = ""

