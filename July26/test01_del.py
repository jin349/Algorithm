my_lst = [1,2,3,4,5]
str_lst=['a','b','c','d','e','f']

print(my_lst, str_lst)
#형식 -> del my_lst[index]
#del은 예약어 (함수x) --> my_lst.del

del my_lst[4] #del를 이용해 특정 인덱스, 범위 인덱스를 지울 수 있다.
print(my_lst)

del str_lst[4]
print(str_lst)

del str_lst[2:]
print(str_lst)

str_lst.remove('b') #del과 달리 범위값으로 지우지 못하고 특정 값만 지울 수 있다.
print(str_lst)

