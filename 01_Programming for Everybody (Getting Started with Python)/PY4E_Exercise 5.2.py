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
