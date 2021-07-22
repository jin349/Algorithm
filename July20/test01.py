import numpy as np

np.random.seed(1)
myArr = np.random.randint(1, 30, 16).reshape(4, 4)
print(myArr)

# 1.각 열의 합을 출력해라.
# total=0
# for i in myArr:
#     for j in i: #[ 6 12 13  9]
#         total += j
# print(total)
# print(sum(myArr))

# 2.값이 2인 곳의 위치를 출력해라
# for i in range(len(myArr)):
#     for j in range(len(myArr)): #[ 6 12 13  9]
#         if myArr[i][j] ==2:
#             print("2의 위치는 ", i,',',j,"입니다")
#
# print(np.where(myArr==2))

# 3.각 요소들이 짝수인지 홀수인지 출력해라
# for i in myArr:
#     for j in i:
#         if j%2==0:
#             print("짝수")
#         else:
#             print("홀수")
#     print()

# print(np.where(myArr%2==0,'짝수', '홀수'))

# 4.각 요소들의 합이 짝수인지 홀수인지 출력해라. sum()사용X
# for i in myArr:
#     hap = 0
#     for j in i:
#         hap+=j
#
#     if hap%2==0:
#         print('짝수')
#     else:
#         print('홀수')

# 5.각 행의 인덱스2,3 인 수를 출력해라.
# for i in myArr:
#     for j in i[2:]:
#         print(j, end=' ')
#     print()

# 6. 홀수행끼리의 합, 짝수행끼리의 합을 출력해라.(다시 풀어보기)
# for i in range(len(myArr)):
#     hap_even_line = 0
#     hap_odd_line = 0
#     if i % 2 != 0:
#         for j in i:
#             hap_even_line += j
#         print(hap_even_line)
#
#     else:
#         for j in i:
#             hap_odd_line += j
#         print(hap_odd_line)

# 7.각 열의 합을 출력해라. 단, 함수 사용X
hap=0
for i in range(len(myArr)):
    for j in range(len(myArr[i])): #[ 6 12 13  9]
        hap+=myArr[j][i]
    print(hap)

# myEye = np.eye(3, k=-1, dtype=int)
# print(myEye)
