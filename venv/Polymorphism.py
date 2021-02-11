# Parent class 1
class Person:
    def __init__(self, firstname, lastname, health, status):

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
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

#Seda.introduce()
#Seda.status_change()

#inheritance example
class Enemy(Person):
    def __init__(self, weapon, firstname,lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

        """
        Polymorphism occurs when we want to allow the child class to have a method with the same name and a similar implementation as the parent class and we wish for that method you override the parent class method.
        """

    def introduce(self):
        print("You are my mortal enemy!!!")

        """
        When we make a method in the child's class with the same name as the one in the parent class, the child class method overrides the parent class method.
        """

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print("{}'s health => ".format(other.firstname), other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))



Alex = Enemy('rock', 'Alex', 'Wayne', 75, status=False)
Alex.introduce()


Alex.hurt(Seda)
Alex.insult(Maria)
Alex.steal(Lee)



