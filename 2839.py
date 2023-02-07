import sys
ssr = sys.stdin.readline
N = int(ssr())

answer = 0
while(N >= 0):
    if N % 5 == 0:
        answer += N // 5
        print(answer)
        exit()
    else:
        N -= 3
        answer += 1
print(-1)