def add(a, b):
    c = a + b
    return c


if __name__ == '__main__':   #运算不出结果，多半是这里出问题了  只执行下面这个函数  别人调用的不执行
    d = add(1, 58)
    print(d)
'''import function as F

print(F.add(3, 9))
'''