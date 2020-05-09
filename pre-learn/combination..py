class Eye:
    def __init__(self, color):
        self.color = color


class Person:
    def __init__(self, yzheye):
        self.yzheye = yzheye

    def show(self):
        print(self.yzheye.color)


yzheye = Eye("black")
p = Person(yzheye)
p.show()


























