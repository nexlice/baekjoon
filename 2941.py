import sys

ssr = sys.stdin.readline
word = ssr().rstrip()
word = word[::-1]

"""
read it reversely.

case 0:
    does it starts with =?
    if it does, is the following character (c, zd, s, z) ?

case 1:
    does it starts with -?
    if it does, is the following character (c, d) ?

case 2:
    does it starts with j?
    if it does, is the following character (l, n) ?
"""

case1 = ["=c", '=zd', '=s', '=z']
case2 = ['-c', '-d']
case3 = ['jl', 'jn']

# count the croatia alphabets
count = 0
index = 0

# add '\n'
word = word + '\n'

while(word[index] != "\n"):
    if word[index : index + 3] == '=zd':
        # print(word[index : index + 3])
        index = index + 3
        count = count + 1
        continue
    elif word[index : index + 2] == '=c' or word[index : index + 2] == '=s' or word[index : index + 2] == '=z' or word[index : index + 2] == '-c' or word[index : index + 2] == '-d' or word[index : index + 2] == 'jl' or word[index : index + 2] == 'jn':
        # print(word[index : index + 2])
        index = index + 2
        count = count + 1
        continue
    else:
        index = index + 1
        count = count + 1

print(count)


