import sys

N = (int)(sys.stdin.readline().rstrip())
numbers = sys.stdin.readline().rstrip()

sum = 0
for i in range(len(numbers)):
    sum = sum + (int)(numbers[i])

print(sum)