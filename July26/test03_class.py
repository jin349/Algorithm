class Calculator:
    def add(self,a,b):
        #return a+b  #self를 붙이지 않아도 a, b 자체만으로 값을 불러 올 수 있음.
    #또는
        self.a = a
        self.b = b
        self.a += 5
        self.b += 5
        print(a,b)
        return self.a + self.b

    def sub(self,a,b):
        self.a = a
        self.b = b

        self.a +=5
        self.b +=5

        a+= 6
        b+= 6

        print(self.a, self.b)
        self.result = self.a + self.b
        print(a,b)
        return self.result
    def multy(self, a,b):
        pass
    def div(self, a,b):
        pass

my_cal = Calculator()
print(my_cal.add(10,5))

print(my_cal.sub(20,11))
