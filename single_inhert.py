# Single Basic Inheritance
# Parent class
class Parent:
    def __init__(self,name):
        self.name = name 

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Derived class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Create an instance of child
child = Child("Alice")
child.greet()
child.play()

