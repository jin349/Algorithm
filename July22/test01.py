
def combine_list(str_list): # 문자열을 한 번에 프린트
    my_str = ' '.join(map(str, str_list))
    prn(my_str)


def prn(combine_str): #단순 출력
    print(combine_str)

if __name__ == '__main__':
    string_lst = ['Hi', 'My', 'name', 'is', 'HJ']
    combine_list(string_lst)
