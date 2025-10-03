#Q:15 Write a program to calculate the electricity bill (accept number of unit from user) according 
# to the following criteria : Unit Price uptp 100 units no charge Next 200 units Rs 5 per unit 
# After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is 
# Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 
# (For example if input unit is 150 than total bill amount is Rs.

units = int(input("Enter number of units consumed: "))
bill = 0

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + ((units - 300) * 10)

print(f"Total bill amount Rs = {bill}..")
