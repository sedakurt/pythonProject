"""
There are some features of a class which will require more explanation including:

The "__init__" method, which allows every instance of a class to be created with specific parameters

The "self" variable which allows information to be shared easily and efficiently.

"proper syntax" Python classes always have the keyword class followed by a space and the name of the class.

"""

class Person:
    def __init__(self, firstname, lastname, health, status):
        "initialize attributes to be used in/available for all class methods in this class, and for class objects created by this class."
        #that will allow our people to introduce themselves

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today.".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))

Seda = Person("Seda", "Kurt", 100, status=True)
Maria = Person("Maria", "Jones", 77, status=False)
Lee = Person("Lee", "Williams", 40, status=True)

print("{} is my friend? {}".format(Seda.firstname, Seda.status))
print("{} is my friend? {}".format(Maria.firstname, Maria.status))

Seda.introduce()
Maria.introduce()
Lee.introduce()
'''
Result:
Hello, my name is Seda Kurt
Hello, my name is Maria Jones
Hello, my name is Lee Williams
'''

Seda.status_change()
Maria.status_change()
Lee.status_change()




