"""
사실 몇 겹에 있는지만 알면 됨.

layer : count : number
1 : 1  : 1
2 : 6  : 2 ~ 7
3 : 12 : 8 ~ 19
4 : 18 : 20 ~ 37

n : 6 * (n - 1) : 등차수열의 합  - 개수 ~ 등차수열의 합
>> n == 1 일 때 : 1
>> n > 1 일떄
n * ((n - 1) * 6) / 2 + 1 - (6 * (n - 1) - 1) ~ n * ((n - 1) * 6) / 2 + 1
3n(n-1)+1-(6n-6-1) <= s <= 3n(n-1)+1
3n^2-3n+1-6n+7 <= s <= 3n^2-3n+1
3n^2-9n+8 <= s <= 3n^2-3n+1
"""
N = (int)(input())
layer = 1

if N == 1:
    layer = 1    
    print(layer)
    exit()
else:
    while(3 * (layer) * (layer) - 9 * layer + 8 <= N):
        # print(3 * (layer) * (layer) - 9 * layer + 8)
        layer = layer + 1
print(layer-1)
