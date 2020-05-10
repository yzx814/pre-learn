#列表推导
a_list = [1, 2, 3, 4, 5, 6, 7]
b_list=[]#创建一个空的list 用于存放运算后的数据

for i in a_list:
    b_list.append(i*2)

print(b_list)

c_list = [i*2 for i in a_list]
print(c_list)

#输出10以内的偶数
evens = []
for i in range(10):
    if i%2 == 0:
        evens.append(i)
print(evens)

#打印字符串的每一个字符    先用len计算字符串的数目，然后再通过range把x变成列表    然后由索引打印
x = "hfjgrf"
for i in range(len(x)):
    print(x[i])
#这个好像不太能能用推导式

#把一个矩阵展开为一个列表
matrix = [
    [0, 2, 4],
    [1, 2, 3],
    [1, 5, 3],
    ]

flattend = []
for row in matrix:
    for i in row:
        flattend.append(i)
        print(flattend)

'''flattend = [
    i
    for row in matrix
    for i in row   #此处没有；双引号
]

changed = {value: key for key, value in input_dict.items()}
chars = {w[0] for w in words_list}'''

