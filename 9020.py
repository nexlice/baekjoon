import sys
ssr = sys.stdin.readline

T = int(ssr())
LHS = []
RHS = []

def generatePrimes(N):

    #1929_1.py
    numbers = [i for i in range(2, N + 1)]
    sieve = [True] * len(numbers)
    upperBound = int(N ** (1/2)) + 1

    for index, number in enumerate(numbers):

        # when number is higher than upper bound, break.
        if number > upperBound: break

        # when sieve value is true, check if it is prime or not.
        if not sieve[index]: continue

        # change all of it mutiples into False.
        for i in range(number * 2, N + 1, number):
            sieve[i - 2] = False

    # generate prime list
    primes = []
    for index, boolVal in enumerate(sieve): 
        if boolVal : primes.append(numbers[index])

    return primes

def GoldbachConjecture(N, primes):
    """
    꼭 가운데 인덱스 값이 중간 값이라고 보장할 수 없음.
    mid = int(len(primes) / 2) if len(primes) % 2 == 0 else int(len(primes) / 2) + 1 
    for i in range(mid, len(primes)):
        if (N - primes[i]) in primes:
            return primes[i], N - primes[i]
    return -1, -1
    """
    LHS, RHS = N // 2, N // 2
    while(LHS > 0):
        if LHS in primes and RHS in primes:
            return LHS, RHS
        else:
            LHS -= 1
            RHS += 1
    return -1, -1



for i in range(T):
    N = int(ssr())
    primes = generatePrimes(N)
    a, b = GoldbachConjecture(N, primes)
    LHS.append(min(a, b))
    RHS.append(max(a, b))

for i in range(T):
    print(f"{LHS[i]} {RHS[i]}")