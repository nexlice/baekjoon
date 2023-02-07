import sys

word = sys.stdin.readline().rstrip()

alphabet = ['ABC', "DEF", 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

sum = 0
for i in alphabet:
    for c in word:
        if c in i:
            sum += alphabet.index(i) + 3

print(sum)