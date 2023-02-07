import sys
num = (int)(input())
list = list(map(int, sys.stdin.readline().split()))

max = -1000000
min = 1000000

for i in range(num):
    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]
print(f"{min} {max}")