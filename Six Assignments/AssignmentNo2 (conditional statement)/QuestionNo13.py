# Write a program to check if a year is leap year or not.Write a program to check 
# if a year is leap year or not. If a year is divisible by 4 then it is leap year 
# but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

year_from_user = int(input("Enter a year:"))

if (year_from_user % 400 == 0) or (year_from_user % 4 == 0 and year_from_user % 100 != 0):
    print(f"{year_from_user} is a Leap Year.")
else:
    print(f"{year_from_user} is not a Leap Year.")
