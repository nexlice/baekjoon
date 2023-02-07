import sys
A, B = sys.stdin.readline().split()

def addStringNum(a, b):
    """Add two numbers that are string.

    Args:
        a(String): big number that integer cannor contain.
        b(String): big number that integer cannor contain.
    
    Return:
        (String): sum of the two given parameters.
    """

    reversedA = a[::-1]
    reversedB = b[::-1]
    answer = ""

    # find the longer value
    longer = ""
    shorter = ""
    if len(reversedA) >= len(reversedB):
        longer = reversedA
        shorter = reversedB
    elif len(reversedA) < len(reversedB):
        longer = reversedB
        shorter = reversedA

    # match the indices
    for i in range(len(longer) - len(shorter)):
        shorter += "0"

    # make one more room for each numbers
    longer +="0"
    shorter += "0"

    # add two numbers
    carry = 0
    for i in range(len(longer)):
        sum = int(longer[i]) + int(shorter[i]) + carry
        residue = (int(longer[i]) + int(shorter[i]) + carry) % 10
        carry = 1 if sum >= 10 else 0
        answer += str(residue)
    
    answer = answer[::-1]
    if answer[0] == '0':
        print(answer[1:])
    else:
        print(answer)

        
    
addStringNum(A, B)