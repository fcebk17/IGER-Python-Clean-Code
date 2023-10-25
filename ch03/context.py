# Bad
myfile = open('data.txt')

try:
    for line in myfile:
        print(line)

finally:
    myfile.close()

# Good
with open('data.txt') as myfile:
    for line in myfile:
        print(line)