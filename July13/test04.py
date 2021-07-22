def get_even_total(even_lst):
    # 짝수를 가져온다 -> get_even()함수를 사용해서 짝수를 가져온다.
    even =0
    for i in even_lst:
        even+=i
    return even


def get_odd_total(odd_lst):
    # 홀수를 가져온다 -> get_odd()함수를 사용해서 홀수를 가져온다.
    odd = 0
    for i in odd_lst:
        odd+=i
    return odd


def get_even():
    lst_even=[]
    for i in range (get_total()):
        if i%2 ==0:
            lst_even.append(i)

    even = get_even_total(lst_even)
    return even

def get_odd():
    lst_odd=[]
    for i in range(get_total()):
        if i%2 !=0:
            lst_odd.append(i)

    odd=get_odd_total(lst_odd)
    return odd


def get_total(n):
    # 짝수의 합을 가져온다   -> get_even_total() 함수를 이용한다.
    # 홀수의 합을 가져온다   -> get_odd_total() 함수를 이용한다.
    even_hap = get_even_total(n)
    odd_hap = get_odd_total(n)


    return 0    # 짝수와 홀수의 합을 리턴한다.


if __name__ == '__main__':
    total = get_total([5, 7, 2, 9, 11, 56, 34, 21, 6, 3, 1])
    print(total)