# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:

    def add(self,a,b):
         return a+b
    def sub(self,a,b):
         return a-b
    def mul(self,a,b): 
        return a*b
    def div(self,a,b): 
        return a/b if b!=0 else "Error"

obj_c:Calculator = Calculator()
print(obj_c.add(4,2), obj_c.sub(4,2), obj_c.mul(4,2), obj_c.div(4,2))
