# Bad
my_list = ['apple', 'banana', 'cat']
for i in range(len(my_list)):
    print(i, my_list[i])

# Good
my_list = ['apple', 'banana', 'cat']
for i, item in enumerate(my_list):
    print(i, item)