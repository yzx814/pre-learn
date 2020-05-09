
class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):    #不要self name 参数都有，要一个自身就行
        print(self.name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)  #在父类的基础上加什么东西，加名字所以name，而不是self


cat1 = Cat("big white")
cat1.show()   #show 继承了父类show的方法，即打印自己的name的属性

'''class Person:
    def say(self, content):
        print(content)
yzh = Person()
yzh.say("ithe dictonary is the only place where success comes before work")

cxq = Person()
cxq.say("At 18 our conviction are the hills form which we look ;at 45 they are caves in which we hide")
'''
























