ans = input()

result = ""
cnt = 0

if len(ans) < 2:
        ans = "0" + ans

cal = ans

while result != ans:
    tmp = (str)((int)((cal)[0]) + (int)((cal)[1]))
    if len(tmp) < 2:
        tmp = "0" + tmp
    # print(tmp)
    cal = (cal)[-1] + (tmp)[-1]
    # print(cal)
    cnt = cnt + 1
    result = cal
print(cnt)