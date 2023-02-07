a, b = input().split()
a = int(a)
b = int(b)

if b >= 45:
    b = b - 45
elif b < 45 and a >= 1:
    a = a - 1
    b = b + 15
elif b < 45 and a == 0:
    a = 23
    b = b + 15

print(str(a)+ " " + str(b))