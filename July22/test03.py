def u_l(up_low):
    for i in up_low:
        make_uplow(i)

def make_uplow(ul_list):
    #print(ul_list)
    #for j in ul_list:
    if ul_list.isupper() == True:
        print(ul_list.lower())
    else:
        print(ul_list.upper())

if __name__ == '__main__':
    q3=['A','B','c','D','e','F','G','h']
#함수호출 -> 소문자를 대문자로, 대문자를 소문자로 만들어주는 함수!
#호출은 한 번! 함수는 2개를 만들어 보자!
    u_l(q3)