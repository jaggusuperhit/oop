# Simple inheritance


# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound .")


# Derived class
class Dog(Animal):
    # when you use constructor in child class then it could not call the parent constructor attributes its called constructor overloading.
    # def __init__(self):
    #     self.behaviour = "friendly"
    # It can use parent class method
    # def speak(self):

    # Also create new method
    # Method overloading
    def speak1(self):
        print(f" {self.name} barks.")


# create an instance of Animal
# animal = Animal("Genric Animal")
# animal.speak()

# Create an instance of Dog
dog = Dog("Buddy")
# dog.speak1()
dog.speak()
