my_numbers = (1, 1, 2, 3, 5, 8, 13, 21)
print(my_numbers[2:5])        # 取得索引 2 到 5 的元素
# (2, 3, 5)
print(my_numbers[:3])         # 取得索引 0 到 3 的元素
# (1, 1, 2)
print(my_numbers[3:])         # 取得索引 3 到最後的元素
# (3, 5, 8, 13, 21)
print(my_numbers[::])         # 取得所有元素
# (1, 1, 2, 3, 5, 8, 13, 21)
print(my_numbers[1:7:2])      # 取得索引 1 到 7 的元素，間隔 2 個元素
# (1, 3, 8)