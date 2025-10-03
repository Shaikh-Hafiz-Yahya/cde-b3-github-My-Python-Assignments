# Q:3) Write a program in which use all the operators we can use in Python

# 1. ARTHEMATIC OPERATORS (+ , - , * , / , //)
var_for_int_1 , var_for_int_2 = 12 , 20

print('SUM = ' , var_for_int_1 + var_for_int_2)

print('product = ' , var_for_int_1 * var_for_int_2)

print('quotient = ' , var_for_int_1 / var_for_int_2)

print('difference = ' , var_for_int_2 - var_for_int_1) 

print('floor division = ' , var_for_int_1 // var_for_int_2)

print('exponent = ' , var_for_int_1 ** 2)

# 2. LOGICAL OPERATORS  (and , or , not)
num1 , num2 = 11 , 22

# and operator
print('False and False = ',num1 == num2 and num1 > num2)  #False

print(f'False and False = {num1 == num2 and num2 < num1}') #False

print(f'False and False = {num1 > num2 and num2 <= num1}') #False

print(f'True and True = {num1 == num1 and num1 < num2}') #True

print(f'False and True = {num1 != num1 and num1 == num1}') #False

# or operator
print('False or True = ',num1 == num2 or num1 < num2)  # True

print(f'False or False = {num1 == num2 or num2 < num1}') # False

print(f'False or False = {num1 > num2 or num2 <= num1}') # False

print(f'True or True = {num1 == num1 or num1 < num2}') # True

# not operator
print(not (num1 < num2)) #False

# 3. Comparision operators (> , < , >= , <= , == !=)
x , y = 5 , 10
print('F',x > y) 

print('T',x < y) 

print('F',x >= y) 

print('T',x <= y)

print('F',x == y)

print('T',x != y)

# (Assignment Operators / ADVANCE ARTHEMATIC OPERATORS)-->(Augment Statement(+= , -= , *= , /= , //= , %=))
# Arithmetic operator ko assignment operator k saath combined kr k Augment statement tyyar.
a , b , c , d , e , f , g = 3 , 5 , 20 , 25 , 30 , 32 , 64

a += 2
print('(a += 2) => (a = a + 2) =' , a)

b -= 1
print('(b -= 1) => (b = b - 1) =' , b)

c *= 2
print('(c *= 2) => (c = c * 2) =' , c)

d /= 5
print('(d /= 5) => (d = d / 5) =' , d)

e //= 10
print('(e //= 10) => (e = e // 10) =' , e) 

f %= 2                
print('(f %= 2) => (f = f % 2) =' , f ,' = Reminder!')

g **= 1
print('(g **= 1) => (g = g ** 1) =' , g)

# identity operators (is , is not)
x = 15 
y = 15

# is 
print(f'x = y {x is y}')

# is not 
print(f'x != y {x is not y}')

# Bitwise operators (in , not in)
x = 'Hello Python'
y = {1:'a' , 2:'b'}

# in
print('H is exist x' , 'H' in x)

# not in
print('1 is not exist y' , 1 not in y)

