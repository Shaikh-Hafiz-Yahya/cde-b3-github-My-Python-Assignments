# Modify the above question to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print(f"Percentage of classes attended: {attendance_percentage:2f}%")

if attendance_percentage >= 75:
    print("Student is allowed to sit in the exam.")
else:
    medical_cause = input("Do you have a medical cause? (Y/N):").strip().upper()  #str method 2 use kre
    if medical_cause == "Y":
        print("Student is allowed to sit in the exam due to medical cause.")
    else:
        print("Student is NOT allowed to sit in the exam.")
