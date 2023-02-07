import sys
ssr = sys.stdin.readline

def isGroupWord(word):
    
    """check whether given string is group word or not

    store all alphabets that are successive.
    get the character set and find if indices are successive.

    input : (string) word
    output: (boolean) is this group word?
    """
    
    setChar = list(set(word))

    for index, char in enumerate(setChar):
        
        # index of a particular character
        testList = [wordIndex for wordIndex, pivot in enumerate(word) if pivot == char]
        minVal = min(testList)

        # make it start from 0
        checkList = [val - minVal for val in testList]

        # generate truth list
        truthList = list(range(0, len(checkList)))

        # check if two lists are the same.
        if checkList == truthList:
            continue
        else:
            return False
    
    return True


N = (int)(ssr())

words = []
answer = 0
for i in range(N):
    words.append(ssr().rstrip())
    if isGroupWord(words[i]): answer += 1

print(answer)