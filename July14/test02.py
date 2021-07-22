# 슬라이싱
a = [10, 100, ['pen', 'banana', 'orange']]
print(a[0:2])   # 0번째부터 1번째(2는 포함 안됨) 인덱스까지 출력
print(a[2][0:2])    # 2번 인덱스에서 0번째부터 1번째까지 값 출력
print(a[:-1])   # a의 마지막 인덱스 출력
print(a[-1])
a[1:2] = [1001, 10001, 100001]  # a의 1번에 값 추가
print(a)
del a[-1]  # 해당 인덱스의 값을 지움
print(a)
a.reverse() # 역방향으로 정렬
print(a)
a.insert(2, 7)  # 2번 인덱스에 값 7을 추가함
print(a)
a.remove(1001)  # 값 1001을 지움
print(a)
ex = [88, 77]
a.append(ex)    # append는 리스트 자체를 마지막 인덱스에 추가함
print(a)
a.extend(ex)    # extend는 마지막 인덱스에 값을 추가함
print(a)
# 튜플은 삭제가 안된다
b = (10, 100, ('a', 'b', 'c'))
print(b[2][1])
print(b[2][0:2])
# del b[0]    # 이 명령문은 오류남 !! 삭제가 안된다 !
c = (1, 2, 3)
print(c + b)
print(b + c)
print(3 in c)   # 3이 c에 있는가? 있으면 true가 출력됨, 없으면 false
print(b.index(100))  # 100의 인덱스를 반환
# 순서 x 중복 x, 수정O, 삭제O
d = {'name': 'kim', 'city': 'seoul', 'tel': '0000'}  # key를 숫자로 잘 사용하지 않음
print(d['name'])    # key가 name인 값을 출력
print(d.get('city'))  # key가 name인 값을 출력  ->  안전한 접근 방법
e = {'a': [1, 2, 3, 4, 5]}
print(e['a'][1:3])
e['b'] = (7, 8, 9)  # key 'b'를 추가
print(e)
print(e.keys())     # e의 키 값들을 출력
temp = list(d.keys())   #  d의 키값을 리스트로 변환
print(temp[1:3])
for key in d:
    print("myinfo :", key)
print("----------")
for key in d.values():
    print("myinfo :", key)
print("----------")
for key in d.keys():
    print("myinfo :", key)
print("----------")
for key, value in d.items():
    print("myinfo :", key, value)
print(e.values())
print(list(e.values()))
print('name' in d)
print(2 in e)
# 집합  순서x, 중복x
s1 = set()
s2 = {1, 2, 3, 4, 4, 4}
s3 = {1, 2, 4}
print(s2)
print(s2.difference(s3))    # s2 와 s3의 차집합
print(s3)
s3.add(7)
print(s3)
words = "dream"
for s in words:
    print(s)
for n in words:
    if n.isupper():     # 해당 문자가 대문자일 때
        print(n.lower())    # 소문자로 바꾸기
    else:
        print(n.upper())    # 대문자로 바꾸기
q1 = {"봄": "딸기", "여름": "수박", "가을": "사과", "겨울": "귤"}
for k in q1.keys():
    if k == '가을':
        print(q1[k])
for k,v in q1.items():
    if k == '가을':
        print(v)

