''' 1부터 입력된 수 n까지의 수 중에서 n의 짝수 첫번째 배열에, 홀수 두번쩨 배열에 담아 출력해라 '''

# lst1 = []   # 짝수 배열
# lst2 = []   # 홀수 배열
# # i = 1
# n = 50
#
# for i in range (1, n+1):
#     if i%2==0:
#         lst1.append(i)
#     else:
#         lst2.append(i)
#
# print(lst1)
# print(lst2)

def prn(n):
    lst1=[] #홀수 배열
    lst2=[] #짝수 배열

    for i in range(1, n+1):
        if i % 2==0:
            lst2.append(i)
        else:
            lst1.append(i)

    # print(lst1)
    # print(lst2)
    return lst1, lst2

if __name__ == '__main__':
    n=50
    # prn(n)
    odd_lst, even_lst=prn(n)
    print(odd_lst)
    print(even_lst)