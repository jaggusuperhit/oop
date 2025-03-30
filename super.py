# Parent class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound")


# Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()  # call the base class method. Super can only use through child class.
        print(f"{self.name} barks.It is a {self.breed}")


# create an instance of Dog
dog = Dog("Golden Retreiver")
dog.speak()
