import sys
import math

def isPrime(number):
    """
    Determine whether given number is prime or not.
    
    Args:
        number : (int) a number to be checked if it is prime or not.
                    it is bigger than or equal to 2

    Output:
        (Boolean) : True if the parameter is prime, otherwise False.
    """
    if number == 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    upperBound = int(math.sqrt(number)) + 1
    for i in range(3, upperBound, 2):
        if number % i == 0:
            return False
    
    return True


# read numbers and initialize
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
M, N = list(map(int, sys.stdin.readline().rstrip().split()))
numbers = [i for i in range(2, N + 1)]
sieve = [True] * len(numbers)

for index, number in enumerate(numbers):

    # when sieve value is true, check if it is prime or not.
    if sieve[index]:
        
        # if the value is prime, change all of it mutiples into False.
        if isPrime(number):
            for i in range(number * 2, N + 1, number):
                sieve[numbers.index(i)] = False
                """
                이 .index()함수가 순회라서 매우 느림.
                """
        
        # if the value is not prime, change sieve's value into False
        else:
            sieve[index] = False

# print all primes from M to N
for index, boolVal in enumerate(sieve):
    if boolVal and numbers[index] >= M: print(numbers[index])