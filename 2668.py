import sys

# readline method
ssr = sys.stdin.readline

# get integer value
num = int(ssr())

# generate num * 2 grid
grid = [[_ + 1 for _ in range(num)] for _ in range(2)]

# input the numbers accordingly.
for i in range(num):
    grid[1][i] = int(ssr())

setGrid = list(set(grid[1]))
setGrid.sort()

print(len(setGrid))
print(setGrid)
# for element in setGrid:
#     print(element)