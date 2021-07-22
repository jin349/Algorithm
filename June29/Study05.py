# number = [11, 2, 6, 9, 25, 7, 3, 23]
#
# a=[]
# b=[]
# for i in range(len(number)):
#     if number[i]%2==0:
#         #print("짝수:"+str(number[i]))
#         a.append(number[i])
#         #print(a)
#     else:
#         #print("홀수:"+str(number[i]))
#         b.append(number[i])
#         #print(b)
# print("a="+str(a))
# print("b="+str(b))

a=[]
b=[]
def odd():
    for i in range(len(number)):
        if number[i]%2==0:
            a.append(number[i])
        else:
            b.append(number[i])
if __name__ == '__main__':
    number = [11, 2, 6, 9, 25, 7, 3, 23]
    print(a)
    print(b)