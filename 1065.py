import sys

def isHanSoo(a):
    """Check if given integer a is hansoo

    Args:
        a(int): an integer value
    
    Return:
        (Boolean): output of verification
    """

    # change the integer value into string
    string = (str)(a)

    # only check 3 digit (or more) numbers
    if len(string) == 1 or len(string) == 2:
        return True
    else:
        for i in range (len(string) - 2):
            if (int)(string[i]) - (int)(string[i+1]) != (int)(string[i+1]) - (int)(string[i+2]):
                # print((int)(string[i]) - (int)(string[i+1]))
                # print((int)(string[i+1]) - (int)(string[i+2]))
                return False
        return True

N = (int)(sys.stdin.readline().rstrip())
numbers = list(range(1, N + 1))
cnt = 0
for i in range(N):
    if isHanSoo(numbers[i]):
        cnt = cnt + 1

print(cnt)
