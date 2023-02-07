import sys

# numbers = [[0] * 9] * 9
row, col, maxVal = 1, 1, 0

for i in range(9):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    tmp.append(maxVal)
    if max(tmp) > maxVal:
        maxVal = max(tmp)
        row = i + 1
        col = (tmp.index(maxVal) + 1) if tmp.index(maxVal) != 9 else 9
    else:
        continue

print(maxVal)
print(f"{row} {col}")
