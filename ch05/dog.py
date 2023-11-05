class Dog:
    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
    
    def bark(self):
        print("汪汪汪!")

    def run(self):
        print("狗狗跑!")

# 建立一個 Dog 的實例
my_dog = Dog("小黑", "拉布拉多", "黑色", 5)

# 呼叫實例的方法
my_dog.bark()
my_dog.run()

# 印出實例的屬性
print(my_dog.name)