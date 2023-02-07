import sys

C = (int)(sys.stdin.readline().rstrip())
student = []
for i in range(C):
    student.append(list(map(int, sys.stdin.readline().rstrip().split())))

    # seperate the values
    num = student[i][0]
    score = student[i][1:]

    # get the average
    avg = sum(score) / num

    # count the students who have a score higher than avg
    cnt = 0
    for j in range(num):
        if score[j] > avg:
            cnt = cnt + 1
    
    # get the percentage
    student[i] = (cnt / num) * 100

for i in range(C):
    print(f"{student[i]:.3f}%")