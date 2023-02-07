import sys
length = (int)(input())
list = list(map(int, (sys.stdin.readline()).split()))
find = (int)(input())
cnt = 0
for i in range(length):
    if list[i] == find:
        cnt = cnt + 1
print(cnt)