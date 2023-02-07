sum = (int)(input())
num = (int)(input())
for i in range(num):
    item, stock = input().split()
    item = (int)(item)
    stock = (int)(stock)
    sum = sum - item*stock

if sum == 0:
    print("Yes")
else:
    print("No")