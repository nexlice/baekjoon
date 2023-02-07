"""
when searching diagonally,
the sum of the numerator and denominator are the same.

n : 1
X : 1
fraction : 1/1

n : 2
X : 2 ~ 3
fraction : 2/1 1/2

n : 3
X : 4 ~ 6
fraction : 1/3 2/2 3/1

n : 4
X : 7 ~ 10
fraction : 4/1 3/2 2/3 1/4

again, denominator or numerator forms arithematic progression.

n : n
X : n(n+1)/2 - (n - 1) ~ n(n+1)/2
fration : 
if n is odd, numerator starts from 1.
if n is even, denominator starts from 1.
1/n ~ n/1

"""
import sys

X = (int)(sys.stdin.readline())

n = 1

while(X > n * (n + 1) / 2):
    n = n + 1

start = n * (n + 1) / 2 - (n - 1)
index = X - start

if n % 2 == 0:
    print(f"{(int)(index + 1)}/{(int)(n - index)}")
else:
    print(f"{(int)(n - index)}/{(int)(index + 1)}")