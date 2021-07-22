def solution(n):
    answer = 0
    n_string = str(n)
    n_map = map(int, n_string)
    n_list = list(n_map)
    for i in n_list:
        answer = sum(n_list)

    print(answer)

if __name__ == '__main__':
    solution(123)