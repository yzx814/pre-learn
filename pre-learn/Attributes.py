class Person:
    def __init__(self,name):
        self.name = name
        self.height = 1.66
        self.sex = "man"

    def show(self):
        print(self.name)
        print(self.height)
        print(self.sex)

yzh = Person("yy")
yzh.show()


class Person:

    def __call__(self):
        print("what is worth doing is worth doing well")

yzh = Person()
yzh()
