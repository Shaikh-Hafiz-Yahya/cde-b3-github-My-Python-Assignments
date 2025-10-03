# Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.

# if employee is a male and age is in between 20 to 40 then he may work in anywhere

# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

# And any other input of age should print "ERROR"

age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").strip().upper()
marital_status = input("Enter marital status (Y/N): ").strip().upper()
 
if gender == "F":
    print("Employee will work only in urban area.")

elif gender == "M":
    if 20 <= age <= 40:
        print("Employee may work anywhere.")

    elif 40 < age <= 60:
        print("Employee will work only urban area.")

    else:
        print("ERROR")

else:
    print("ERROR: Invalid gender.")
