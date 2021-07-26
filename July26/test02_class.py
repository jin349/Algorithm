#단일 클래스
#파이썬 클래스 이름은 대문자로 시작한다.
#함수는 단어마다 _를 써서 이어준다.
#e.g. def make_string
class UserInfo:
    #java 예) this.name = name
    def __init__(self, name): #생성자
        self.name = name

    def user_info(self):
        print("Name: ", self.name)

user1 = UserInfo("Kim") #line 6. 생성자를 생성할 때 name을 담는 다고 했기 때문에 ()안에 name에 대한 걸(예: Kim) 담아줘야 함.
                        #객체를 인스턴스화 시킨다. --> 메모리에 올려 놓는다.
#print(user1) #메모리에 올라온 걸 출력, <__main__.UserInfo object at 0x0000023E83045850>
print(user1.name)
user1.user_info()

#다른 사람으로 관리하고 싶을 때 똑같이 하나 더 만들어준다.
#UserInfo("Kim", "Lee", "Park")은 Kim, Lee, Park 각각 다른 사람이라고 구분하지 못함.
user2=UserInfo("Lee")
print(user2.name)
user2.user_info()

class SelfTest:
    def function_1(): #클레스 메소드. 인자가 담아져 있지 않은 메소드
        print("funtional called")

    def function_2(self):
        print("function2 called")

SelfTest.function_2()
test = SelfTest()
test.function_2()