#정수형
a = 1000
print(a)

a = -7
print(a)

a = 0
print(a)

#실수형
a = 157.40
print(a)

a = -183.23
print(a)

a = 5.
print(a)

a = -.7
print(a)

# 지수표현방식
a = 1e9
print(a)

a = 75.25e1
print(a)

a = 3954e-3
print(a)

#실수형 더 알아보기
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

a = 0.3 + 0.6
print(round(a, 2))
if round(a,2) == 0.9:
    print(True)
else:
    print(False)

#수 자료형의 연산
a = 5
b = 3
print(a ** b)
print(a ** 0.5)

#리스트 자료형
# C/C++: int a[] = {3,2,5,1}
# Java : int[] a = {3,2,5,1}    이렇게 {}를 이용해서 초기화 한다.
a = [1,2,3,4,5,6,7]
print(a)

n = 10
a = [0] * n
print(a)

#인덱싱
a = [1,2,3,4,5]
print(a[-1])
a[3] = 7
print(a)

#슬라이싱
a = [1,2,3,4,5]
print(a[1:4])

#리스트 컴프리헨션
#0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)
#1부터 9까지의 수들의 제곱값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

#0부터 9까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(10) if i % 2 == 1]
print(array)
#일반코드와의 비교
a = []
for i in range(10):
    if i % 2 == 1:
        a.append(i)
print()

