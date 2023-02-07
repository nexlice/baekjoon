import sys
T = (int)(sys.stdin.readline().rstrip())

result = []
for i in range(T):
    iter, word = sys.stdin.readline().rstrip().split()
    iter = (int)(iter)
    tmp = ""
    for j in range(len(word)):
        tmp = tmp + word[j] * iter
    result.append(tmp)

for i in range(T):
    print(result[i])