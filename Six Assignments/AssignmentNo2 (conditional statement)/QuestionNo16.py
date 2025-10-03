# Take input of age of 3 people by user and determine oldest and youngest among them.

age_1 = int(input("Enter age of first_person: "))
age_2 = int(input("Enter age of second_person: "))
age_3 = int(input("Enter age of third_person: "))

oldest = max(age_1, age_2, age_3)
youngest = min(age_1, age_2, age_3)

print(f"The oldest age is: {oldest}")
print(f"The youngest age is: {youngest}..")
