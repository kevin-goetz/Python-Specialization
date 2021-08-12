# %%

'''
Exercise 2.1:
Write a program that uses input to prompt a user for their
name and then welcomes them.
'''

name = input('Enter your Name:')    # prompt the user for a name
print('Hello', name)                # print the results

# %%
'''
Exercise 2.2:
Write a program to prompt the user for hours and rate per
hour to compute gross pay.
'''

hour = float(input('Enter Hours:'))     # prompt for working hours
rate = float(input('Enter Rate:'))      # prompt for hourly rate


def payroll(hour, rate):                # define the payroll function
    return round(hour*rate, 2)


print(payroll(hour, rate))              # print the gross pay

# %%

'''
# Exercise 2.3:
Assume that we execute the following assignment statements:

width = 17
height = 12.0

For each of the following expressions, write the value of the expression and
the type (of the value of the expression).

1. width//2
2. width/2.0
3. height/3
4. 1 + 2 * 5
'''

width = 17                          # initialize variable
height = 12.0                       # initialize variable

print(width//2, type(width//2))     # Test 1
print(width/2.0, type(width/2.0))   # Test 2
print(height/3, type(height/3))     # Test 3

sum = 1 + 1 * 5
print(sum, type(sum))               # Test 4
# %%

'''
Exercise 3.1:
Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
'''

hour = float(input('Enter Hours:'))     # prompt for working hours
rate = float(input('Enter Rate:'))      # prompt for hourly pay

if hour <= 40:                          # pay normal rate for hours <= 40
    pay = hour * rate
else:
    pay = 40*rate+(hour-40)*rate*1.5    # pay 50% bonus for hours > 40

print(pay)                              # print total pay

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

# %%

'''
Exercise 3.3:
Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:
Score       Grade
>= 0.9      A
>= 0.8      B
>= 0.7      C
>= 0.6      D
< 0.6       F

Enter score: 0.95
A
Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F

Run the program repeatedly as shown above to test the various different values
for input.
'''

# prompt for a score until it is a float ranging between 0.0 and 1.0
while True:
    try:
        score = float(input('Enter Score:'))
        if 0 <= score <= 1:
            break
        else:
            print('Bad Score')
            continue
    except:  # noqa
        print('Bad Score')
        continue

# grading the score
if score >= 0.9:
    Grade = 'A'
elif score >= 0.8:
    Grade = 'B'
else:
    Grade = 'Loser'

print(Grade)

# %%

"""
Exercise 4.1: Run the program on your system and see what numbers you get.
Run the program more than once and see what numbers you get.
"""

import random  # noqa
for i in range(10):
    x = round(random.random()*100)
    print(x)

# %%

'''
Exercise 4.6:
Write a program to prompt the user for hours and rate per hour using input
to compute gross pay.
Pay should be the normal rate for hours up to 40 and time-and-a-half for the
hourly rate for all hours worked above 40 hours.
Put the logic to do the computation of pay in a function called computepay()
and use the function to do the computation.
The function should return a value. Use 45 hours and a rate of 10.50 per hour
to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to
a number.
Do not worry about error checking the user input unless you want to -
you can assume the user types numbers properly.
Do not name your variable sum or use the sum() function.
'''


# Prompting and converting Hours/week
hours = input('Please enter weekly hours:')

try:
    h = float(hours)

except:  # noqa
    print('Only Numbers Please.')
    quit()

# Prompting and converting pay/week
rate = input('Please enter hourly pay:')
try:
    r = float(rate)
except:  # noqa
    print('Only Numbers Please.')
    quit()


def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay = 40*r+(h-40)*r*1.5
    return(pay)


print('Pay', computepay(h, r))

# %%

'''
Exercise 5.1:
Write a program which repeatedly reads numbers until theuser enters “done”.
Once “done” is entered, print out the total, count, and average of the numbers.
If the user enters anything other than anumber, detect their mistake
using try and except and print an error message and skip to the next number.
'''

# initialize variables
number = '0'
count = 0
sum = 0
avg = 0

# prompt until user writes 'done'
while number != 'done':
    number = input('Please enter a number:')
    try:
        if number != 'done':
            num = float(number)
        else:
            break
    except:  # noqa
        print('please only numbers!')
        continue

    # compute the (intermediate) results
    count = count+1
    sum = sum+num
    avg = sum/count

# print the results
print(sum, count, avg)


# %%

'''
Exercise: 5.2
Write a program that repeatedly prompts a user for integer numbers until
the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a
try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.
'''

# initialize variables
large = None
small = None
number = '0'

# configure the new loop with error handling
while number != 'done':
    number = input('Enter a number:')

    # error handling
    try:
        if number != 'done':
            num = float(number)
        else:
            break

    except:  # noqa
        print('Invalid input')
        continue

    # conditional loop
    if large is None:
        large = num

    elif large < num:
        large = num

    if small is None:
        small = num

    elif small > num:
        small = num

# print the results
print('Maximum is', int(large))
print('Minimum is', int(small))
