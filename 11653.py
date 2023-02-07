import sys
N = int(sys.stdin.readline())

if N == 1:
    exit()

primes = []

while(N % 2 == 0):
    N = int(N / 2)
    primes.append(2)

while(N != 1):
    for i in range(3, N + 1, 2):
        if N % i == 0:
            primes.append(i)
            N = int(N / i)
            break

for n in primes:
    print(n)