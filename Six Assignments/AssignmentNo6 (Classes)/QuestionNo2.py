# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date, datetime

class Person:
    def __init__(self, name, country, dob):

        self.name, self.country = name, country
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))



obj:Person = Person("Andrew Ng", "USA", "1999-06-15")
print(f'\n Name:{obj.name}\n Country:{obj.country}\n Age:{obj.age()}')
