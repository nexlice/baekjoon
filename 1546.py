import sys
num = int(sys.stdin.readline().rstrip())
score = list(map(int, sys.stdin.readline().rstrip().split()))

avg = 0
max = 0
# get the max value
for i in range(num):
    if score[i] > max:
        max = score[i]

# manipulate the scores
for i in range(num):
    score[i] = score[i] / max * 100

# get the new avg
newAvg = 0
for i in range(num):
    newAvg = newAvg + score[i]
newAvg = newAvg / num
print(newAvg)