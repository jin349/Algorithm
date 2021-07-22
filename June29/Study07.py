number = [11, 2, 6, 9, 25, 7, 3, 23]

def num():
    for i in range(len(number)):
        if number[i]%2==0:
            print(str(number[i])+"은 2의 배수 입니다.")
        if number[i]%3==0:
            print(str(number[i])+"은 3의 배수 입니다.")
        elif number[i]%2 !=0 and number[i]%3 !=0:
            print(str(number[i])+"은 2와 3의 배수가 아닙니다")

if __name__ == '__main__':
    num()