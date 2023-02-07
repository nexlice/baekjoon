import sys

S = sys.stdin.readline().rstrip()

# ASCII 97 : a

# get the set of the components
setS = list(set(S))

# set the alphabet orders
alphabet = [-1] * 26

# find the index
for i in range(len(setS)):
    for j in range(len(S)):
        if setS[i] == S[j]:
            alphabet[ord(S[j]) - 97] = j
            break

# generate answer
answer = ""
for i in range(len(alphabet)):
    answer = answer + str(alphabet[i]) + " "

# print answer
print(answer.rstrip())