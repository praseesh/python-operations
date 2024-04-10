class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"i am {self.name}.I have {self.age}year old. I can eat")
class Cat(Animal):
    def walk(self):
        print(f"i am {self.name}.I have {self.age}year old. I can Walk")
x = Animal("Jimmy", 7)
y = Cat("jack", 5)
x.eat()
y.eat()
y.walk()
