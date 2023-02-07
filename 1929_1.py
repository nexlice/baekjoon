import sys

# read numbers and initialize
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
M, N = list(map(int, sys.stdin.readline().rstrip().split()))
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

# print all primes from M to N
for index, boolVal in enumerate(sieve):
    if boolVal and numbers[index] >= M: print(numbers[index])