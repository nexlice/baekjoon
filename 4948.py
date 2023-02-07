import sys
ssr = sys.stdin.readline

# 1929_1.py
def BertrandPostulate(num):
    if num == 1: return 1

    M = num + 1
    N = 2 * num
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

    sumList = sieve[M - 2 : N]
    # for i in numbers: print(i) if sieve[i - 2] else print()
    return sum(sumList)

while(True):
    num = int(ssr())
    if num == 0: break
    print(BertrandPostulate(num))