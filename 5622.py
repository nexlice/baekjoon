import sys

# 주어지는 단어: 숫자 2~9에 매핑..

"""
a,b,c 
>> 97, 98, 99
>> 0, 1, 2
>> 3으로 나눈 몫 : 0 
>> 몫 + 3초

몫이 6,7,8 일 때 예외 발생
초 몫 알파벳
3 : 0 : ABC
4 : 1 : DEF
5 : 2 : GHI
6 : 3 : JKL
7 : 4 : MNO
8 : 5 : PQR
9 : 6 : (S >> 8)TU
10 :7 : (V >> 9)WX
10 :8 : (Y >> 10) (Z >> 10)

몫이 8 인가? 
>> 몫 - 1초 + 2초
>> 몫 + 1초

몫이 6,7일 때 나머지 0 인가? 
>> 몫 + 2초  - 1초
>> 몫 + 1초
"""

word = sys.stdin.readline().rstrip().lower()

def charToSec(c):
    """ convert character into seconds

    input : (character) single character
    output : (integer) corresponding seconds according to dial

    """
    val = ord(c) - ord('a')
    quota = val // 3
    remainder = val % 3

    # 몫이 6,7일 때 나머지 0 인가? 
    if (quota == 6 or quota == 7) and remainder == 0:
        return quota + 2

    # 몫이 8 인가?
    elif quota == 8:
        return quota + 2

    else:
        return quota + 3


sum = 0
for i in range(len(word)):
    # print(charToSec(word[i]))
    sum = sum + charToSec(word[i])

print(sum)