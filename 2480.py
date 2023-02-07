a, b, c = input().split()
if (a == b and b == c):
    print(f"{10000 + (int)(a)*1000}")
elif (a == b or b == c or a == c):
    if (a == b or b == c):
        print(f"{1000 + (int)(b)*100}")
    else:
        print(f"{1000 + (int)(a)*100}")
else:
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    print(f"{(int)(max)*100}")