# Bad
names = ['John', 'Tom', 'Tina']
ages = [17, 23, 20]

for i in range(len(names)):
    print(names[i], ages[i])

# Good
names = ['John', 'Tom', 'Tina']
ages = [17, 23, 20]

for x, y in zip(names, ages):
    print(x, y)