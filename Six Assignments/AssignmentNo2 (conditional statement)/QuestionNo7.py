# Q:7 Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

LengthFromUser = float(input("Enter the length of the rectangle: "))
BreadthFromUser = float(input("Enter the breadth of the rectangle: "))


if (LengthFromUser == BreadthFromUser):
    print("It is a Square.")

else:
    print("It is a Rectangle.")