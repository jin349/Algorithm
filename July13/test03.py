#리티스를 인자값으로 받아 리스트 값들의 합을 구하는 함수를 만들어보자.


def hap(get_lst):
    print(type(get_lst))
    pass

def get_sum(my_lst): #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total=0
    for i in my_lst:
        total +=i #1~10까지의 합
    return total #55를 리턴

def make_lst_a(n): # n=10
    lst=[]
    for i in range(1, n+1): #1~10
        lst.append(i) #리스트에 1부터 10까지 추가된다.

    print(lst)
    total = get_sum(lst) #total=55
    return total

def make_lst(n):
    lst=[]
    for i in range(1, n+1):
        lst.append(i) #n(1~10)까지 숫자가 담긴 리스트를 만든다.

    my_even = make_even(lst) #1~10까지 숫자가 담긴 리스트를 짝수만 담긴 리스트로 바꿔준다.
    return my_even

def make_even(lst):
    lst_even = []
    for i in lst:
        if i%2==0:
            lst_even.append(i)
    #짝수가 담긴 리스트를 만든다.
    return lst_even

def get_total(n1, n2):
    total=0
    for i in range(n1, n2+1):
        total+=i
    return total

if __name__ == '__main__':
    result = get_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #짝수의 합 함수 호출
    #홀수의 합 함수 호출
    print(result)
    print("------------------------------------")
    #n이라는 점수를 받아서 1부터 n까지의 수를 리스트로 만드는 함수를 만들고, 이 함수를 가지고 리스트의 합을 구하는 함수를 만들자.
    # m_result=make_lst_a(10)
    # print(m_result)

    #make_lst와 make_even 연결된 문제
    # m_result01=make_lst(10)
    # print(m_result01)

    #get_total 문제
    # total = get_total(5,10)
    # print(total)

