# Base class
class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound")

# Intermediate class 1(Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal,Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()