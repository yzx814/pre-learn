a = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]]
print(a[0])  # 取第0个数据
print(a[1][0])  # 取第1个数据中的第0个数据
print(a[2:])  # 取第二个数据以后的所有数据
print(a[:4])  # 取第0个数据到第4个数据
print(a[::2])  # 按步长为2取数据
print(a[2:7:2])  # 取第2个到第7个之间的数据，步长为2
print(a[::-1])  # 步长为-1取数据，相当于颠倒顺序
print(a[-1:2:-1]) # 从最后条数据反着取到第2条数据