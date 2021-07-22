#리스트를 인자값으로 받아 리스트 값들의 합을 구하는 함수를 만들어보자.
def hap(get_lst):
    get_hap=0
    for i in get_lst:
        get_hap+=i
    return get_hap


if __name__ == '__main__':
    result = hap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(result)