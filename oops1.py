# initiate a class
class employee:
    # special method/magic method/ dunder method - constructor
    def __init__(self):
        # print(id(self))
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.desiganation = "SDE"
        print("attributes/data have been initiated")

    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")


# create an obj/instance of the class
# self = object
sam = employee()
# sam.name = "sam kumar"
# print(sam.name)
# print(id(sam))

# shaktiman = employee()
# print(id(shaktiman))
# printing the attribute


# calling the method
# sam.travel("Kerala")

# print(type(sam))
