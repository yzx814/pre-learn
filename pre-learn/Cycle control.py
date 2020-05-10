#打印0-9
a = []
for i in range(10):
    a.append(i)
    print(a[i], end=" ")

for i in range(9):  #range()就是一堆数字
    print(i, end=" ")


#遍历列表

a_list = {4, 5, 6, 7, 8, 9}
for i in a_list:
    print(i, end=" ")

print("\n================")

#带索引的遍历

for i, a in enumerate(a_list):
    print(i, ":", a)
print("\n================")

a_list = {4, 5, 6, 7, 8, 9}
for i, a in enumerate(a_list, 2):
    print(i, ":", a)

print("\n================")




#遍历字典
print("\n================")

b_dict = {"name": "yzh", "sex": "men", "height": "1.66m"}
for i, j in b_dict.items():
    print(i, ":", j)


