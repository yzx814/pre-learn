class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):     #加法重载操作
        return self.age + other.age


yzh = Person("YZH", 23)#不能用双引号23，是整形数字
cxq = Person("CXQ", 27)
print(yzh + cxq)