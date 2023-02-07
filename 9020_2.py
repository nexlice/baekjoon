import sys
ssr = sys.stdin.readline

def Goldbach(N):

    #1929_1.py
    numbers = [i for i in range(2, N + 1)]
    sieve = [True] * len(numbers)
    upperBound = int(N ** (1/2)) + 1

    for index, number in enumerate(numbers):

        # when number is higher than upper bound, break.
        if number > upperBound: break

        # when sieve value is false, continue
        elif not sieve[index]: continue

        # change all of it mutiples into False.
        elif sieve[index]:
            for i in range(number * 2, N + 1, number):
                sieve[i - 2] = False

    LHS, RHS = N // 2, N // 2
    while(True):
        if sieve[LHS - 2] and sieve[RHS - 2]:
            return LHS, RHS
        else:
            LHS -= 1
            RHS += 1

for i in range(int(ssr())):
    N = int(ssr())
    a, b = Goldbach(N)
    print(f"{a} {b}")
