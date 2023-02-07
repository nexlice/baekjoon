import sys
ssr = sys.stdin.readline
    # Args:
    #     a(int): an integer value
    
    # Return:
    #     (Boolean): output of verification

T = (int)(ssr())

result = []
for i in range(T):
    H, W, N = list(map(int, ssr().rstrip().split()))
    floor = str(N % H if N % H != 0 else H)
    room = str((N // H + 1) if N % H != 0 else (N // H))
    result.append(floor + (room if len(room) != 1 else ('0' + room)))

for a in result:
    print(a)