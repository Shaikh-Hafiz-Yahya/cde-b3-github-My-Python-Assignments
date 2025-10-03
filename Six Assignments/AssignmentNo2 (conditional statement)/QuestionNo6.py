# Q:6) Write a program to display the last digit of a number.

int_num = 1004
if int_num > 1003 or int_num < 1005:
    print('is exist' , 1004 is int_num) 

    if int_num % 100 == 4:
        print('Last Digit = ' , 4)
    else:
        print('!!!')    

else:
    print('4 does not exist..')    

# OR..

int_num = int(input('Enter integer number but Reminder 4 milay...'))

if int_num == 1004:
    print('4 is exist as a last digit.' , int_num) 

    if int_num % 100 == 4:
        print('Last Digit = ' , 4 , 'Reminder = ' , 4)
    else:
        print('!!!')    

else:
    print('4 does not exist as a last digit..' , int_num)        
