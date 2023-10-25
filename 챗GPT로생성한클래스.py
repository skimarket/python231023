class Person:
    def __init__(self, id, phoneNumber):
        self.id = id
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print(f"ID: {self.id}")
        print(f"Phone Number: {self.phoneNumber}")

class Manager(Person):
    def __init__(self, id, phoneNumber, skill):
        super().__init__(id, phoneNumber)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

class Employee(Manager):
    def __init__(self, id, phoneNumber, skill, title):
        super().__init__(id, phoneNumber, skill)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

# Sample usage of the classes:
person1 = Person(id=1, phoneNumber="123-456-7890")
person1.printInfo()

manager1 = Manager(id=2, phoneNumber="987-654-3210", skill="Leadership")
manager1.printInfo()

employee1 = Employee(id=3, phoneNumber="555-123-4567", skill="Programming", title="Software Engineer")
employee1.printInfo()
