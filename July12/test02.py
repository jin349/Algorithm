# 문장 안에서 t의 개수를 출력해라
# my_first_string = "In type annotations you can now use built-in collection types such as list " \
#                   "and dict as generic types instead of importing the corresponding capitalized types (e.g. List or Dict) from typing. " \
#                   "Some other types in the standard library are also now generic, for example queue.Queue."
# 내꺼
# for i in range(len(my_first_string)):
#     num=0
#     if my_first_string[i] =='t':
#         num += 1
#         print()

def t_count(char):
    cnt = 0
    my_first_string = "In type annotations you can now use built-in collection types such as list " \
                      "and dict as generic types instead of importing the corresponding capitalized types (e.g. List or Dict) from typing. " \
                      "Some other types in the standard library are also now generic, for example queue.Queue."

    for i in my_first_string:
        if i ==char:
            cnt +=1
        print(cnt)
if __name__ == '__main__':
    char = 't'
    t_count(char)
