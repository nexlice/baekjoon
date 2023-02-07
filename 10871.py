import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
lis = list(map(int, sys.stdin.readline().rstrip().split()))

ans = ""
for i in range(n):
    if lis[i] < x:
        ans = ans + (str)(lis[i]) + " "

print(ans.rstrip())