# %%

'''
Exercise 3.2:
Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
'''

# prompt for hours until it's a float
while True:
    try:
        hour = float(input('Enter Hours:'))
        break
    except:  # noqa
        print('Error, please enter numeric value')
        continue

# prompt for rate until it's a float
while True:
    try:
        rate = float(input('Enter Rate:'))
        break
    except:  # noqa
        print('Error, please enter numeric value')
        continue

# compute the pay as usual
if hour <= 40:
    pay = hour*rate
else:
    pay = 40*rate+(hour-40)*rate*1.5
print(pay)
