h, m = input().split()
h = (int)(h)
m = (int)(m)
p = (int)(input())

# c를 시간 + 분으로 나눌 것.
ph = p // 60
pm = p % 60

finalh = 0
finalm = 0

# 분끼리 더했을 때 시간이 나오는지 확인할 것.
if m + pm >= 60:
    finalh = h + ph + 1
    finalm = m + pm - 60
else:
    finalh = h + ph
    finalm = m + pm

# 시끼리 더했을 때 24로 나눈 나머지를 사용할 것.
finalh = finalh % 24
print(f"{finalh} {finalm}")