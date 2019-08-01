pet = {
    "name": "Doggo",
    "animal": "dog",
    "species": "labrador",
    "age": 5
}

class Pet(object):
    def __init__(self, name, age, mood):
        self.name = name
        self.age = age
        self.mood = "happy"

    def move(self):
        if self.mood == "happy":
            print("%s is %s, he jumps around" % (self.name, self.mood))
        else:
            self.mood = "tired"
            print("%s is %s, so he naps" % (self.name, self.mood))

my_pet = Pet("Buddy", 3, "happy")
my_pet.move()
my_pet.mood = "sad"
my_pet.move()

# class Pet(object):
#     def __init__(self, name, age, animal):
#         self.name = name
#         self.age = age
#         self.animal = animal
#         self.is_hungry = False
#         self.mood = "happy"
#
#     def eat(self):
#         print("> %s is eating ..." % self.name)
#         if self.is_hungry:
#             self.is_hungry = False
#         else:
#             print("> %s may have eaten too much." % self.name)
#             self.mood = "lethargic"
#
# my_pet = Pet("Fido", 3, "dog")
#
# my_pet.is_hungry = True
# print("Is my pet hungry? %s" % my_pet.is_hungry)
# my_pet.eat()
# print("How about now? %s" % my_pet.is_hungry)
# print("My pet is feeling %s" % my_pet.mood)


# my_pet2 = Pet("Fido", 3)
# print("My pet %s is %s years old" % (my_pet2.name, my_pet2.age))
#
# my_pet3 = Pet("Spot", 6)
# print("My pet %s is %s years old" % (my_pet3.name, my_pet3.age))
#
# my_pet4 = Pet("Buddy", 2)
# print("My pet %s is %s years old" % (my_pet4.name, my_pet4.age))
