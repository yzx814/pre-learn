print("==========list数组操作")

a = [1, 2, 3, 4, 5, 6]
print(len(a))

print(a[3])

a[3] = 5
print(a)

a.remove(a[3])  #删除操作  what.remove（what[元素序号]）  what 是指数组名  只有删除操作比较特殊一点

print(a)
a.append(8)  #a.append(a[99])  这样是不对的形式，向尾部添加what 元素 直接就是   what.append（元素）

print(a)

'''在第二个元素前插入一个数字7'''
a.insert(2, 7)
print(a)

'''将另外一个集合添加到尾部'''
a.extend([5, 8, 9])#这个和 a.append类似  只不过是将数字换成了数组，道理是一样的，那针对其他类型应该也是这个思想
print(a)


'''查看数组元素的索引'''

print(a.index(7))  #what.index()


# 排序
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 清空元素
a.clear()
print(a)






