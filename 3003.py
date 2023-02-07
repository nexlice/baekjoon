correct = [1,1,2,2,2,8]
answer = []
input = input().split()

for i in range(6):
    answer.append(correct[i] - (int)(input[i]))

for i in range(6):
    print(answer[i])

