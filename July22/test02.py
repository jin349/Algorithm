
def five_letters(five_str):

    for i in five_str:
        prn(i)


def prn(i):
    if len(i) >= 5:
        print(i)

if __name__ == '__main__':
    q2= ["nice", "study", "python", "anaconda", "!"]
    #함수 호출 -> 글자가 5개 이상인 문자열만 출력하자.
    five_letters(q2)