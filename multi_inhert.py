# Multilevel Inheritance

# Base class
class Grandparent:
    def __init__(self,name):
        self.name = name

    def tell_story(self):
        print(f"{self.name} tells a story.")
# Intermediate class
class Parent(Grandparent):
    def work(self):
        print(f"{self.name} is working.")

# Derived class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# create an instance of child
child = Child("Charlie")
child.tell_story()
child.work()
child.play()


