 # Part -2 Python Basics (Conditional Statements)

'''Q:1) A company decided to give bonus of 5% to employee if his/her year 
of service is more than 5 years. Ask user for their salary and year 
of service and print the net bonus amount.'''

employee_salary = float(input('Enter your salary..'))
employee_year_of_service = int(input('kitny saal hogye company ko service dyty hoe..'))

if employee_salary >= 100000 and employee_year_of_service > 5:
    print('Most Probabily bonus mil skta ha')
    if employee_salary >= 100000:
        print(f'CongratualationsBonus = {employee_salary*0.5}')

else: 
    print('Year Of Service < 5 Years..\t SO You_are_not_eligible_for_Bonus' )  