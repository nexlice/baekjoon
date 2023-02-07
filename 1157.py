import sys

word = sys.stdin.readline().rstrip().upper()

setWord = list(set(word))
count = [0] * len(setWord)

for i in range(len(setWord)):
    for j in range(len(word)):
        if setWord[i] == word[j]:
            count[i] = count[i] + 1

maxCnt = max(count)
maxIndex = [i for i, x in enumerate(count) if x == maxCnt]

# print(word)
# print(count)
# print(maxIndex)

if len(maxIndex) != 1:
    print("?")
else:
    print(setWord[maxIndex[0]])

