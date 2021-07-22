#리스트를 인자값으로 받아 리스트 값들의 합을 구하는 함수를 만들어보자.


def hap(get_lst):
    get_evenhap=0
    get_oddhap=0
    for i in get_lst:
        if i%2==0:
            get_evenhap+=i
            print(get_evenhap)

        else:
            get_oddhap+=i
            print(get_oddhap)

    #pass와 continue의 차이
    #pass: 아래의 명령문을 실행하도록
    #continue: for문이 계속 반복 실행할 수 있도록 하여, 반복문을 탐색하는 속도를 높여줌.

    #홀수의 합을 구하는 함수
    #짝수의 합을 구하는 함수


def get_sum(my_lst):
    pass

def make_lst_a(n):
    pass

if __name__ == '__main__':
    result = hap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #짝수의 합 함수 호출
    #홀수의 합 함수 호출
    print(result)
    print("------------------------------------")