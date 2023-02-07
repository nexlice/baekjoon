def DRK(a):
    # input a is integer.
    string = (str)(a)

    # get the sum of each digits
    sum = 0
    for i in range (len(string)):
        sum = sum + (int)(string[i])
    
    # return value
    answer = sum + a
    return answer

answerSet = list(range(1, 10000))
nonSelfSet = []

# get the non self numbers
for i in range(10000):
    nonSelfSet.append(DRK(i))

answerSet = list(set(answerSet) - set(nonSelfSet))
answerSet.sort()

for i in range(len(answerSet)):
    print(answerSet[i])