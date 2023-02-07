a = (int)(input())
for i in range(a):
    arr = ""
    for j in range(i + 1):
        arr = arr + "*"
    print(arr.rjust(a))